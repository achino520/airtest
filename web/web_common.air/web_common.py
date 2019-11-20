# -*- encoding=utf8 -*-
__author__ = "QQ"

from airtest.core.api import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(20)
using("web_header.air")
from web_header import *
import win32gui,win32con
import win32api
import multiprocessing
import win32process
import time
from airtest.cli.runner import AirtestCase
auto_setup(__file__)

data = readyaml()

class web():
	def __init__(self,hwd=None,pid=None):
		self.hwd = hwd
		self.pid = pid

	def drwen_touch(self,v):
		hwnds = self.hwd
		for hwnd in hwnds:
			if win32process.GetWindowThreadProcessId(hwnd)[1] == self.pid:
				pos = driver.zuobiao(v)
				tmp=win32api.MAKELONG(pos[0],pos[1])
				win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,tmp)
				time.sleep(0.05)
				win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP,win32con.MK_LBUTTON,tmp)

	def show(self,hwnd):
	    win32gui.SetForegroundWindow(hwnd)

	def get_hwd(self):
		hWndList = []
		hwdl = []
		win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
		for i in hWndList:
			if "Google Chrome" in win32gui.GetWindowText(i):
				hwdl.append(i)
		self.hwd = hwdl
	def start_web(self,url):
		driver.get(url)
		self.get_hwd()
		import psutil
		self.pid = psutil.Process(driver.service.process.pid).children(recursive=True)[0].pid
		driver.maximize_window()

	def close(self):
		driver.close()

	def register(self,account,password):
		driver.find_element_by_xpath(data['web']['register']['regaccount']).clear()
		driver.find_element_by_xpath(data['web']['register']['regaccount']).send_keys(account)
		driver.find_element_by_xpath(data['web']['register']['regname']).clear()
		driver.find_element_by_xpath(data['web']['register']['regname']).send_keys("韩寒")
		driver.find_element_by_xpath(data['web']['register']['regpassword']).clear()
		driver.find_element_by_xpath(data['web']['register']['regpassword']).send_keys(password)
		driver.find_element_by_xpath(data['web']['register']['regsurepassword']).clear()
		driver.find_element_by_xpath(data['web']['register']['regsurepassword']).send_keys(password)
		driver.find_element_by_xpath(data['web']['register']['regcheckcode']).clear()
		driver.find_element_by_xpath(data['web']['register']['regcheckcode']).send_keys("1111")
		driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[3]/div/form/div[6]/div/button").click()
		self.drwen_touch(Template(r"tpl1573279080428.png", record_pos=(11.315, 2.885), resolution=(100, 100)))
		time.sleep(2)

	def login(self,account,password):
		driver.find_element_by_xpath(data['web']['login']['username']).send_keys(account)
		driver.find_element_by_xpath(data['web']['login']['password']).send_keys(password)
		driver.find_element_by_xpath(data['web']['login']['checkcode']).send_keys("1111")
		driver.find_element_by_xpath(data['web']['login']['loginbutton']).click()
		driver.find_element_by_xpath(data['web']['login']['agree_contract']).click()
		self.drwen_touch(Template(data['web']['login']['unannouncement'], record_pos=(12.01, 2.64), resolution=(100, 100)))

	def youkelogin(self):		
		driver.find_element_by_xpath(data['web']['login']['youkelogin']).click()
		alert = driver.switch_to_alert()
		time.sleep(1)
		alert.accept()
		driver.find_element_by_xpath(data['web']['login']['agree_contract']).click()
		self.drwen_touch(Template(data['web']['login']['unannouncement'], record_pos=(12.01, 2.64), resolution=(100, 100)))

	def gettext(self,xpath):
		driver.find_element_by_xpath(xpath).click()
		text = driver.find_element_by_xpath("//table/tbody/tr/td").text
		print("aaaa:{0}".format(text))

	def banding_bankcard(self):
		self.drwen_touch(Template(r"tpl1573023563827.png", record_pos=(10.535, 3.465), resolution=(100, 100)))
		self.drwen_touch(Template(r"tpl1573023583314.png", record_pos=(11.275, 3.695), resolution=(100, 100)))
		self.drwen_touch(Template(r"tpl1573023745049.png", record_pos=(11.72, 3.075), resolution=(100, 100)))
		self.drwen_touch(Template(r"tpl1573023770706.png", record_pos=(11.69, 3.985), resolution=(100, 100)))
		driver.find_element_by_xpath(data['web']['banding_bankcard']['bankcard_1']).send_keys("4567898576435644446")
		driver.find_element_by_xpath(data['web']['banding_bankcard']['bankcard_2']).send_keys("4567898576435644446")
		driver.find_element_by_xpath(data['web']['banding_bankcard']['bankaddr']).send_keys("深证南山")
		self.drwen_touch(Template(r"tpl1573023950996.png", record_pos=(11.635, 6.355), resolution=(100, 100)))
		driver.assert_exist("//div[@role='alert']", "xpath", "银行卡信息有误或者已绑定")
		time.sleep(1)

	def load_balance(self):
		driver.find_element_by_xpath(data['web']['load_balance']['load1']).click()
		driver.find_element_by_xpath(data['web']['load_balance']['load2']).click()
		driver.find_element_by_xpath(data['web']['load_balance']['load3']).send_keys("5000")
		driver.find_element_by_xpath(data['web']['load_balance']['load4']).send_keys("韩寒")
		driver.find_element_by_xpath(data['web']['load_balance']['load5']).send_keys("2019-11-06")
		driver.find_element_by_xpath(data['web']['load_balance']['load6']).click()

	def change_password(self):
		driver.find_element_by_xpath(data['web']['change_password']['change1']).click()
		driver.find_element_by_xpath(data['web']['change_password']['change2']).send_keys("1234qwer")
		driver.find_element_by_xpath(data['web']['change_password']['change3']).send_keys("1234qwe")
		driver.find_element_by_xpath(data['web']['change_password']['change4']).send_keys("1234qwe")
		driver.find_element_by_xpath(data['web']['change_password']['change5']).click()

	def betting(self):
		driver.find_element_by_xpath(data['web']['betting']['bet_chaosusaiche']).click()
		start_time = driver.find_element_by_xpath(data['web']['betting']['bet2']).text
		end_time = driver.find_element_by_xpath(data['web']['betting']['bet3']).text
		end_time = end_time.split(":")
		end_time = int(end_time[0]*60) + int(end_time[1])
		start_time = start_time.split(":")
		start_time = int(start_time[0]*60) + int(start_time[1])
		if (start_time < 5) and (start_time > 0):
			sleep(start_time + end_time+2)
		elif (start_time == 0):
			sleep(end_time+2)
		driver.find_element_by_xpath(data['web']['betting']['bet4']).send_keys("2")
		for dev in driver.find_elements_by_class_name(data['web']['betting']['betclass']):
			dev.click()
		driver.find_element_by_xpath(data['web']['betting']['betcheck']).click()
		driver.find_element_by_xpath(data['web']['betting']['betcheckagain']).click()


