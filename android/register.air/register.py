# -*- encoding=utf8 -*-
__author__ = "QQ"


from airtest.core.api import *
import time
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
def register():
    start_app('com.csy.cai66')         
    poco("com.csy.cai66:id/home_regist_tv").wait_for_appearance(timeout=500)
    poco("com.csy.cai66:id/home_regist_tv").click()
    touch(Template(r"tpl1573006052446.png", record_pos=(0.235, -0.812), resolution=(1080, 2340)))
    sleep(1.5)
    poco("com.csy.cai66:id/register_username").set_text("achinotest05")
    poco("com.csy.cai66:id/register_name").set_text("韩寒")
    poco("com.csy.cai66:id/register_password").set_text("1234qwer")
    poco("com.csy.cai66:id/register_repassword").set_text("1234qwer")
    poco("com.csy.cai66:id/register_verifycode").set_text("1111")

    touch(Template(r"tpl1573007402976.png", record_pos=(0.005, 0.403), resolution=(1080, 2340)))



register()
