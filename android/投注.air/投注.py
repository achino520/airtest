# -*- encoding=utf8 -*-
__author__ = "QQ"

from airtest.core.api import *
using("common.air")
from common import *

try:
	start_app(data['android']['app'])
	dev  = android()
	dev.pmgrant(data['android']['app'])
	result = readcsv(__file__)
	for key,value in result.items():
		account = key
		password = value
	dev.login(account,password)
	dev.betting()
except:
	raise
finally:
	clear_app(data['android']['app'])
