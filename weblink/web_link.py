
import detection_GPU
import Business_data
import detection_RTSP
import requests
import urllib2
import random
import datetime
import time
import json
import sys
import os


#
# t1 = datetime.datetime.now()
# date_time = time.strftime("%Y-%m-%d %H:%M:%S", t1)
date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def link_code(url):
    """"""
    try:
        # request = urllib2.Request(url,headers=header.get_header())
        html_url = requests.get(url, params=None, timeout=60)

        url_code = html_url.status_code

        if url_code == 200:
            status = 'successful: ' + date_time + ', url:' + url + ', status:' + str(url_code) + ';'
            print status
            return status
        else:
            status = 'failing: ' + date_time + ', url:' + url + ', status:' + url_code + ';'
            print status
            return status

    except Exception, e:
        print(e)

# link_code('http://www.baidu.com')


def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)




# ----------------------------------------------------------------------
def input_url():
    """"""
    codeRootdir = cur_file_dir()
    deviceCount = detection_GPU.deviceCount()
    detection = detection_RTSP.detection_rtsp()
    with open('detection_RTSP_result.txt', 'a+') as w0:
        w0.writelines(detection)
        w0.write('\n')
    Business_datas = Business_data.data_business()
    try:
        with open(codeRootdir + "/json/url_list.json", "r") as f:
            cfgObj = json.loads(f.read())
    except BaseException, e:
        print e
    if cfgObj.has_key("url"):
        urls = cfgObj["url"]
        if urls:
            for i in urls:
                print i
                try:
                    url = 'http://' + i
                    url_status = link_code(url)
                    with open('target_200_url.txt', 'a+') as w1:
                        w1.writelines(Business_datas)
                        w1.write('\n')
                        w1.writelines(deviceCount)
                        w1.writelines(url_status)
                        w1.write('\n')
                    print i + '    yes!'
                except Exception, e:
                    print i + str(e)
        else:
            print "url is none!"
    else:
        print "url_list.json is none"








if __name__ == '__main__':
    input_url()

