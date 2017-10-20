from dbcxn import get_cxn


if __name__ == "__main__":
    cxn = get_cxn()
    sql ="select * from dev_rel_stats order by dt, k"
    rows = cxn.execute(sql).fetchall()
    for r in rows:
        print r[0],",",r[1],",",r[2]
