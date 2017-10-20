import pyodbc
import secrets

import datetime

def create_table(cxn):
    sql = """create table dev_rel_stats ( dt smalldatetime, k varchar(255), v bigint)"""
    return sql

def insert_update(cxn, dt, k, v ):

    sql = """
    if exists (select * from dev_rel_stats where dt = ? and k = ?)
    begin 
        update dev_rel_stats set v = ? where dt = ? and k = ?
    end
    else
    begin
        insert into dev_rel_stats values (?, ? , ?)
    end
    """

    cxn.execute(sql, (dt,k,v,dt,k,dt,k,v))
    cxn.commit()

def get_cxn():
    cxn_string = "DSN=AzureSQL;DATABASE=dev_rel_stats;UID=rich@rich;PWD=" +secrets.DB_PASSWORD
    conn = pyodbc.connect(cxn_string)
    return conn


if __name__ == "__main__":
    cxn_string = "DSN=AzureSQL;DATABASE=dev_rel_stats;UID=rich@rich;PWD=" +secrets.DB_PASSWORD

    conn = pyodbc.connect(cxn_string)

    print conn

