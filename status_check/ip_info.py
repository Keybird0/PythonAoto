#!/usr/bin/env python
# coding: utf-8

from IPy import IP

ip_s = raw_input('Please input an IP or net-range:')
ips = IP(ip_s)

if len(ips) > 1:
    print('net: %s' % ips.net())
    print('netmask: %s' % ips.netmask())
    print('broadcast: %s' % ips.broadcast())    #输出广播地址
    print('reverse address: %s' % ips.reverseNames()[0])    #地址反向解析
    print('subnet: %s' % len(ips))    #输出子网个数
else:    #单个的ip地址
    print('reverse address: %s') % ips.reverseNames()[0]

print('hexadecimal: %s' % ips.strHex())
print('binary ip: %s' % ips.strBin())
print('iptype: %s' % ips.iptype())
    
