#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import jsbeautifier

selected_text = os.getenv("POPCLIP_TEXT")

#selected_text = '{"data":{"total":98,"type":"search","events":[{"field":"appname","log_source":[{"appname":"nxlog","front_message":"2016-09-28&nbsp;09:09:42&nbsp;windows2008R2&nbsp;INFO&nbsp;5312&nbsp;NT&nbsp;AUTHORITY\\SYSTEM&nbsp;适用的组策略对象列表:&nbsp;\r","hostname":"172.16.1.74","log_source":[{"hostname":"172.16.1.74","appname":"nxlog","timestamp":"2016-09-28T01:09:43.888Z","@timestamp":"2016-09-28 09:09:33","intype":"rsyslog","logtype":"nginx_access_log","tag":"\"win\"","path":"windowsevent","message":"2016-09-28 09:09:42 windows2008R2 INFO 5312 NT AUTHORITY\\SYSTEM 适用的组策略对象列表: \r","@version":"1","port":52565}],"receivetime":1474996173000,"tag":"\"win\""},{"appname":"nxlog","front_message":"2016-09-28&nbsp;09:09:42&nbsp;windows2008R2&nbsp;INFO&nbsp;5313&nbsp;NT&nbsp;AUTHORITY\\SYSTEM&nbsp;下列组策略对象不适用，原因是它们已被筛选掉:&nbsp;\r","hostname":"172.16.1.74","log_source":[{"hostname":"172.16.1.74","appname":"nxlog","timestamp":"2016-09-28T01:09:43.888Z","@timestamp":"2016-09-28 09:09:33","intype":"rsyslog","logtype":"nginx_access_log","tag":"\"win\"","path":"windowsevent","message":"2016-09-28 09:09:42 windows2008R2 INFO 5313 NT AUTHORITY\\SYSTEM 下列组策略对象不适用，原因是它们已被筛选掉: \r","@version":"1","port":52565}],"receivetime":1474996173000,"tag":"\"win\""},{"appname":"nxlog","front_message":"2016-09-28&nbsp;09:09:42&nbsp;windows2008R2&nbsp;INFO&nbsp;5320&nbsp;NT&nbsp;AUTHORITY\\SYSTEM&nbsp;检查不属于系统的组策略客户端扩展。\r","hostname":"172.16.1.74","log_source":[{"hostname":"172.16.1.74","appname":"nxlog","timestamp":"2016-09-28T01:09:43.888Z","@timestamp":"2016-09-28 09:09:33","intype":"rsyslog","logtype":"nginx_access_log","tag":"\"win\"","path":"windowsevent","message":"2016-09-28 09:09:42 windows2008R2 INFO 5320 NT AUTHORITY\\SYSTEM 检查不属于系统的组策略客户端扩展。\r","@version":"1","port":52565}],"receivetime":1474996173000,"tag":"\"win\""}],"key":"nxlog"}],"size":1},"result_message":"execute successfully","result_code":1,"result":true}'

res = jsbeautifier.beautify(selected_text)

print res