import os
import json
import Mysql
import sys
import time

# date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


def data_business():
    """"""
    try:
        mysqlobj = Mysql.Mysql()
        mysqlobj = mysqlobj.db_connect()
        codeRootdir = cur_file_dir()
        try:
            with open(codeRootdir + "/json/sql.json", "r") as f:
                sql_dict = json.loads(f.read())
        except BaseException, e:
            print e
            if sql_dict.has_key("sql"):
                command = sql_dict["sql"]
                dataobj = mysqlobj.db_query(command)
                with open("business_data.txt", "w+") as f:
                    # f.writelines(date_time)
                    f.writelines(dataobj)
                    f.write('\n')
                    return "The business data query was successful"
            else:
                print "sql.json is none"
                return "sql.json is none"
    except BaseException, e:
            print e