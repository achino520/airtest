# -*- encoding=utf8 -*-
__author__ = "QQ"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
using("header.air")
from header import *
from airtest.core.android.android import Android
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
data = readyaml()
ST.FIND_TIMEOUT = 6
class android():
	def __init__(self):
		pass

	def login(self,account,password):
		touch(Template(r"tpl1573006030145.png", record_pos=(0.028, -0.954), resolution=(1080, 2340)))
		sleep(1.5)
		poco("com.csy.tryplaytest:id/login_username").set_text(account)
		poco("com.csy.tryplaytest:id/login_password").set_text(password)
		poco("com.csy.tryplaytest:id/login_verifycode").set_text("1111")
		touch(Template(r"tpl1573007622996.png", record_pos=(-0.001, 0.103), resolution=(1080, 2340)))
		touch(Template(r"tpl1574649016830.png", record_pos=(0.018, 0.325), resolution=(1080, 2340)))

	def register(self,account,password):        
		poco("com.csy.tryplaytest:id/home_regist_tv").wait_for_appearance(timeout=500)
		poco("com.csy.tryplaytest:id/home_regist_tv").click()
		touch(Template(r"tpl1573006052446.png", record_pos=(0.235, -0.812), resolution=(1080, 2340)))
		sleep(1.5)
		poco("com.csy.tryplaytest:id/register_username").set_text(account)
		poco("com.csy.tryplaytest:id/register_name").set_text("韩寒")
		poco("com.csy.tryplaytest:id/register_password").set_text(password)
		poco("com.csy.tryplaytest:id/register_repassword").set_text(password)
		poco("com.csy.tryplaytest:id/register_verifycode").set_text("1111")		
		touch(Template(r"tpl1573007402976.png", record_pos=(0.005, 0.403), resolution=(1080, 2340)))
		touch(Template(r"tpl1574649016830.png", record_pos=(0.018, 0.325), resolution=(1080, 2340)))

	def betting(self):
		touch(Template(r"tpl1574646829702.png", record_pos=(-0.114, -0.372), resolution=(1080, 2340)))
		aa = poco("android.widget.LinearLayout").child("android.widget.FrameLayout")[0].offspring("com.csy.tryplaytest:id/item_right_odds_key")
		j = 0
		for i in aa:
			i.wait(1).click()
			j=j+1
			if j>3:
				break
		poco("com.csy.tryplaytest:id/game_bet_amount_input").set_text(10)
		touch(Template(r"tpl1574664137608.png", record_pos=(0.322, 0.705), resolution=(1080, 2340)))

	def charge(self):
		touch(Template(r"tpl1573020153393.png", record_pos=(0.395, 0.89), resolution=(1080, 2340)))
		touch(Template(r"tpl1573020180144.png", record_pos=(-0.286, -0.565), resolution=(1080, 2340)))
		touch(Template(r"tpl1573020200572.png", record_pos=(-0.212, -0.41), resolution=(1080, 2340)))
		poco("com.csy.tryplaytest:id/recharge_submit_amount_et").set_text("5000")
		poco("com.csy.tryplaytest:id/recharge_submit_name_et").set_text("韩寒")
		poco("com.csy.tryplaytest:id/recharge_submit_account_et").set_text("4567")
		swipe((50,500),(50,200))
		touch(Template(r"tpl1573020604901.png", record_pos=(0.01, 0.869), resolution=(1080, 2340)))

	def logout(self):
		touch(Template(r"tpl1573009945411.png", record_pos=(0.405, 0.899), resolution=(1080, 2340)))
		touch(Template(r"tpl1573009958340.png", record_pos=(-0.319, 0.863), resolution=(1080, 2340)))
		touch(Template(r"tpl1573009974014.png", record_pos=(0.319, 0.044), resolution=(1080, 2340)))

	def pmgrant(self,package):
		pmg = Android(serialno="AUY9WSEAD6DIHM95",touch_method="ADBTOUCH")
		pmg.shell('pm grant {0} android.permission.READ_EXTERNAL_STORAGE'.format(package))
		pmg.shell('pm grant {0} android.permission.WRITE_EXTERNAL_STORAGE'.format(package))

