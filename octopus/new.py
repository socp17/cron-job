from octopus import SQLite

octopus/SQLite.py databases/sp500.db


def main(argv):

    SQLite.setupNewDatabase('databases/' + argv + '.db')


if __name__ == "__main__":
   main(sys.argv[1])
