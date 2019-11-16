# -*- encoding=utf8 -*-
__author__ = "QQ"

from airtest.core.api import *
using("web_common.air")
from web_common import login
auto_setup(__file__)

image_path = r"C:/Users/QQ/Downloads/AirtestIDE_2019-09-10_py3_win64/AirtestIDE_2019-09-11_py3_win64/invech/web_七夕登录/airtpl1573023048248.png"
login(image_path)