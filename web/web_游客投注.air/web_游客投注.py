# -*- encoding=utf8 -*-
__author__ = "QQ"

from airtest.core.api import *
using("web_common.air")
from web_common import *

try:
	web = Web()
	web.start_web(data['web']['url'])
	web.youkelogin()
	web.betting(data['web']['lottery']['chaosusaiche'])
except:
	raise
finally:
	web.close()


