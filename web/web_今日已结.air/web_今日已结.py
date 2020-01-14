# -*- encoding=utf8 -*-
__author__ = "QQ"

from airtest.core.api import *
using("web_common.air")
from web_common import *

try:
	web = Web()
	result = readcsv(__file__)
	for key,value in result.items():
		account = key
		password = value
	web.start_web(data['web']['url'])
	web.login(account,password)
	web.gettext(data['web']['page_top']['todaygive']['button'])
	web.check_win_lose()
except:
	raise
finally:
	web.close()

