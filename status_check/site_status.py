#!/usr/bin/env python
# coding: utf-8

import os
import httplib
import dns.resolver

iplist=[]
domains="baidu.com"  #这里可以改改从文件读取

def get_iplist(domain=""): #解析域名获取ip
    try:
        A = dns.resolver.query(domain, 'A')
    except Exception, e:
        print "dns resolver error:" + str(e)
        return 
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)   #添加ip到iplist中
    return True

def checkip(ip):
    checkurl = ip + ":80"
    getcontent = ""
    httplib.socket.setdefaulttimeout(5)
    conn = httplib.HTTPConnection(checkurl)
    try:
        conn.request("GET", "/", headers={"Host": domains})
        
        r = conn.getresponse()
        getcontent = r.read(100)
    finally:
        if "<!doctype html>" in getcontent.lower():    #一些返回正常时含有的内容
            
            print ip + "(" + domains + ")" +" => [OK]"
        else:
            print ip + " => [Some thing wrong happen.]"     #可能的话,可以写短信邮件通知

if __name__ == "__main__":
    if get_iplist(domains) and len(iplist) > 0:
        for ip in iplist:
            checkip(ip)
    else:
        print "dns resolver error."
    
        