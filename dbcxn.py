import pyodbc
import secrets

cxn_string = "DSN=AzureSQL;UID=rich@rich;PWD=" +secrets.DB_PASSWORD

conn = pyodbc.connect(cxn_string)

print conn

cur = conn.cursor()

# cur.execute("create table ")





