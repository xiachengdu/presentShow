# -*- coding: gbk-*-
import re
import os
import time
import winsound
import urllib2
import ConfigParser

conf = ConfigParser.ConfigParser()
conf.read("config.conf")
stockId = conf.get("stock", "stock_id")
floatWarnPercentLowValue = float(conf.get("stock","warn_percent_low_value"))
floatWarnPercentHighValue = float(conf.get("stock","warn_percent_high_value"))

#数据请求方法
def data_api(id):
    strHtml = urllib2.urlopen('http://hq.sinajs.cn/list=' + id).read()
    return strHtml

#蜂鸣方法
def beepShortDouble():
    winsound.Beep(400,250)
    time.sleep(1/10)
    winsound.Beep(400,250)
    time.sleep(1)
    
def beepLongOne():
    winsound.Beep(2000,1500)
    time.sleep(1)
def request(stockId):
    try:
        a = data_api('sh' + stockId)
        #print re.split(';|,',a)
    
        b = re.split(';|,',a)
        c = (float(b[3]) - float(b[2]))/float(b[2])*100
        print "presentPercent:"
        print c
        print "precentValue:"
        print b[3]
        print "----"+ b[-3] +"----"
        if c < floatWarnPercentLowValue:
            beepShortDouble()
        elif c > floatWarnPercentHighValue:
            beepLongOne()    
        time.sleep(5)
        os.system('cls')
    except Exception,e:
        print Exception,":",e
        time.sleep(2)
        request(stockId)
    
#主函数，死循环
while 1:   
    request(stockId)


