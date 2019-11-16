# -*- encoding=utf8 -*-
__author__ = "QQ"

from airtest.core.api import *
auto_setup(__file__)
using('register.air')
from register import register
register()