# -*- encoding=utf8 -*-
__author__ = "QQ"

from airtest.core.api import *


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
start_app('com.csy.cai66')

dev =device()
#print(dev.list_app())
touch(Template(r"tpl1573006030145.png", record_pos=(0.028, -0.954), resolution=(1080, 2340)))
sleep(1.5)
#poco("com.csy.cai66:id/login_username").click()
poco("com.csy.cai66:id/login_username").set_text("achinotest01")
poco("com.csy.cai66:id/login_password").set_text("1234qwer")

touch(Template(r"tpl1573007622996.png", record_pos=(-0.001, 0.103), resolution=(1080, 2340)))