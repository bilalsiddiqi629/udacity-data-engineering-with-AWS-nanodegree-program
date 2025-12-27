import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries, create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    Drop database tables if they already exist by executing all queries in drop_table_queries list.

    Keyword Arguments:
        cur: Database cursor object for executing queries
        conn: Database connection object for committing transactions
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

def create_tables(cur, conn):
    """
    Create database tables by executing all queries in create_table_queries list.

    Keyword Arguments:
        cur: Database cursor object for executing queries
        conn: Database connection object for committing transactions
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def load_staging_tables(cur, conn):
    """
    Loads staging tables by executing all queries in copy_table_queries list.

    Keyword Arguments:
        cur: Database cursor object for executing queries
        conn: Database connection object for committing transactions
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    Inserts data into tables by executing all queries in insert_table_queries list.

    Keyword Arguments:
        cur: Database cursor object for executing queries
        conn: Database connection object for committing transactions
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """Connect to database. Once connected, call all methods to drop, create, and insert into database tables. Additionally, create
    staging table and insert into it."""
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()