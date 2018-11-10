import os
import Mysql


def detection_rtsp():
    """rtsp Network connectivity detection"""
    try:
        mysqlobj = Mysql.Mysql()
        mysqlobj = mysqlobj.db_connect()
        command = "SELECT stream_url FROM camera"
        rtspobjs = mysqlobj.db_query(command)

        for rtspobj in rtspobjs:

            rtsp = 'ping ' + rtspobj + ' -c 5'
            print rtsp
        # rtsp = 'ping www.baidu.com -c 5'
            try:
                exit_code = os.system(rtsp)
            except Exception, e:
                print e
            if exit_code == 0:
                status = 'successful' + rtsp[3:-4]
                print status
                return status
            else:
                status = 'failing:' + str(exit_code) + rtsp[3:-4]
                print status
                return status

    except Exception, e:
        print(e)


 # detection_rtsp()


