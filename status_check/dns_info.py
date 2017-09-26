#!/usr/bin/env python
# coding: utf-8

import dns.resolver

domain = raw_input('Please input an domain: ')

A = dns.resolver.query(domain, 'A')  #指定查询类型为A记录
for i in A.response.answer:
    for j in i.items:  #遍历回应信息
        print j.address