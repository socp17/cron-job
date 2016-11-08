import sys
from yahoo_ff.yahoo_ff import yahoo_ff
from octopus import SQLite
from params import PARAMS

import pandas as pd
import numpy as np
import sqlite3
# ppprint
import pprint
pp = pprint.PrettyPrinter(indent=0).pprint

def readStocks(filename):
    with open(filename, 'r') as f:
        return f.read().split()

def update(filename):
    print 'updating ' + filename
    # read file of stocks
    tickers = sorted(readStocks(filename + '.csv'))
    print tickers

    # use the same name for the database as the csv file
    # try connecting to the database
    print 'connecting to database: ' + 'databases/' + filename + '.db'
    connection = SQLite.getConnection('databases/' + filename + '.db')
    c = SQLite.getCursor(connection)

    for ticker in tickers:
        print '********************************************************'
        print str(tickers.index(ticker) + 1) + ' / ' + str(len(tickers))
        print 'fetching data for ' + ticker
        # create yahoo_ff object for each
        companyData = yahoo_ff(ticker)

        if (companyData.flag == 0):
            # get the data frames from the yahoo_ff object
            qr = companyData.qr()
            ar = companyData.ar()
            ks = companyData.ks()
            inf = companyData.inf()
            pr = companyData.pr()
            print 'finished fetching data!'

            # get the id of the company, if not there create one
            print 'getting company id...'
            id = SQLite.getCompanyId(c, ticker)
            print id
            # update column names to fit those in the database
            paramKeys = ['REPORTS', 'REPORTS', 'KEY_STATS', 'INFO', 'PRICE']
            for data, param in zip([qr, ar, ks, inf, pr], paramKeys):
                data = data.reindex_axis(sorted(data.columns), axis=1)
                data.columns = sorted([PARAMS['REPORTS'][key]['columnName'] for key in PARAMS[param].keys()])
                data['company_id'] = int(id)

            # differentiate quarterly and annual reports
            qr['report_type'] = 0
            ar['report_type'] = 1

            # append data to the table
            print 'starting appending data to database...'
            try:
                ar.to_sql('reports', connection, if_exists='append')
                print 'annual report appended'
            except sqlite3.IntegrityError:
                print 'annual report already there'

            try:
                qr.to_sql('reports', connection, if_exists='append')
                print 'quarterly report appended'
            except sqlite3.IntegrityError:
                print 'quarterly report already there'

            try:
                inf.to_sql('info', connection, if_exists='append')
                print 'info appended'
            except sqlite3.IntegrityError:
                print 'info already there'

            try:
                ks.to_sql('key_stats', connection, if_exists='append')
                print 'key stats appended'
            except sqlite3.IntegrityError:
                print 'key stats already there'

            try:
                pr.to_sql('price', connection, if_exists='append')
                print 'price appended'

            except sqlite3.IntegrityError:
                print 'price already there'

            # if no errors, commit ticker's stuff
            print 'committing!'
            connection.commit()


    # when loop is done, close all
    print 'closing database connection'
    c.close()
    connection.close()
    print 'update finished its job'

if __name__ == "__main__":
    update(sys.argv[1])
