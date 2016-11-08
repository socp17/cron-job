import sys
import sqlite3

# TODO: call create tables from here for single create table fun in octopus
TABLES_TO_CREATE = [
    'Companies',
    'Info',
    'Reports',
    'Stats',
    'Price'
]

def readSQLFile (filename):
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()
    return sqlFile

def getConnection(databaseFile):
    return sqlite3.connect(databaseFile)

def getCursor(connection):
    return connection.cursor()

def printTable(c, table):
    for row in c.execute('SELECT * FROM ' + table):
        print row

def getMaxId(c, table):
    findLastIdQuery = 'SELECT MAX(id) FROM ' + table
    print 'executing: findLastIdQuery'
    c.execute(findLastIdQuery)
    return unwrapSingleResponse(c)

def unwrapSingleResponse(c):
    return list(c.fetchall()[0])[0]

def getCompanyId(c, ticker):
    try:
        getIdQuery = 'SELECT id FROM companies WHERE ticker=\'' + ticker + '\''
        print 'executing: getIdQuery'
        c.execute(getIdQuery)
        lastId = str(unwrapSingleResponse(c))
    except:
        lastId = getMaxId(c, 'companies')
        if lastId is None:
            lastId = '-1'
        lastId = str(int(lastId)+1)
        insertIdQuery = 'INSERT INTO companies (id, ticker) VALUES (' + lastId + ',\'' + ticker + '\');'
        print 'executing: insertIdQuery'
        c.execute(insertIdQuery)
    return lastId

def setupNewDatabase(databaseFile):
    print 'setting up tables in ' + databaseFile
    createTableQueries = [readSQLFile('octopus/.sql/createTable_' + table + '.sql') for table in TABLES_TO_CREATE]
    conn = getConnection(databaseFile)
    c = getCursor(conn)
    for query in createTableQueries:
        c.execute(query)
    c.close()
    print 'database setup done'
