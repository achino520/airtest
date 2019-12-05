# -*- encoding=utf8 -*-
__author__ = "QQ"

from airtest.core.api import *
using("web_common.air")
from web_common import *
auto_setup(__file__)


try:
	web = Web()
	result = readcsv(__file__)
	for key,value in result.items():
		account = key
		password = value
	web.start_web(data['web']['url'])
	web.login(account,password)
except:
	raise
finally:
	web.close()













