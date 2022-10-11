# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

bind = '0.0.0.0:5005'
workers = 1
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %({x-real-ip}i)s %({x-forwarded-for}i)s'
loglevel = 'debug'
capture_output = True
enable_stdio_inheritance = True
