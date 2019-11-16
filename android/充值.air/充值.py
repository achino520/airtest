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
sleep(2)
if exists(Template(r"tpl1573020807003.png", record_pos=(0.005, 0.316), resolution=(1080, 2340))):
    touch(Template(r"tpl1573020824861.png", record_pos=(0.005, 0.322), resolution=(1080, 2340)))
    
touch(Template(r"tpl1573020153393.png", record_pos=(0.395, 0.89), resolution=(1080, 2340)))
touch(Template(r"tpl1573020180144.png", record_pos=(-0.286, -0.565), resolution=(1080, 2340)))
touch(Template(r"tpl1573020200572.png", record_pos=(-0.212, -0.41), resolution=(1080, 2340)))
poco("com.csy.cai66:id/recharge_submit_amount_et").set_text("5000")
poco("com.csy.cai66:id/recharge_submit_name_et").set_text("韩寒")
poco("com.csy.cai66:id/recharge_submit_account_et").set_text("4567")

swipe((50,500),(50,200))
touch(Template(r"tpl1573020604901.png", record_pos=(0.01, 0.869), resolution=(1080, 2340)))



