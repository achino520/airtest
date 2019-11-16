# -*- encoding=utf8 -*-
__author__ = "QQ"

from airtest.core.api import *
using("web_common.air")
from web_common import *
import time
# data = readyaml()

try:
	web = web()
	result = readcsv(__file__)
	web.start_web(data['web']['url'])
	driver.find_element_by_xpath(data['web']['register']['regbutton']).click()
	for key,value in result.items():
		account = key
		password = value
		web.register(account,password)
except:
	raise
finally:
	web.close()