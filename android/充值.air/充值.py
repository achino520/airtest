# -*- encoding=utf8 -*-
__author__ = "QQ"

from airtest.core.api import *

using("common.air")
from common import *


try:
	dev  = android()
	dev.pmgrant(data['android']['app'])
	start_app(data['android']['app'])
	result = readcsv(__file__)
	for key,value in result.items():
		account = key
		password = value
	dev.login(account,password)
	dev.charge()
except:
	raise
finally:
	clear_app(data['android']['app'])