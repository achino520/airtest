# -*- encoding=utf8 -*-
__author__ = "QQ"

from airtest.core.api import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(8)
using("web_header.air")
from web_header import *
import win32gui,win32con
import win32api
import multiprocessing
import win32process
import time
import functools
from airtest.cli.runner import AirtestCase
auto_setup(__file__)
ST.FIND_TIMEOUT = 6 #全局变量设置找图超时
data = readyaml()

def click(func):
	@functools.wraps(func)
	def wraper(*args,**kw):
		return func(*args,**kw).click()
	return wraper

def send_keys(words):
	def text(func):
		@functools.wraps(func)
		def wraper(*args,**kw):
			return func(*args,*kw).send_keys(words)
		return wraper
	return text

def get_text(func):
	@functools.wraps(func)
	def wraper(*args,**kw):
		return func(*args,**kw).text
	return wraper

def clear(func):
	@functools.wraps(func)
	def wraper(*args,**kw):
		return func(*args,**kw).clear()
	return wraper

@click
def el_click(xpath):
	aa = driver.find_element_by_xpath(xpath)
	return aa

@send_keys("韩寒")
def el_regname(xpath):
	aa = driver.find_element_by_xpath(xpath)
	return aa


@send_keys("1111")
def el_yanzhenma(xpath):
	aa = driver.find_element_by_xpath(xpath)
	return aa

@clear
def el_clear(xpath):
	aa = driver.find_element_by_xpath(xpath)
	return aa

@get_text
def el_gettext(xpath):
	aa = driver.find_element_by_xpath(xpath)
	return aa

@send_keys("4567898576435644446")
def el_bankcard(xpath):
	aa = driver.find_element_by_xpath(xpath)
	return aa

@send_keys("深圳南山")
def el_bankaddr(xpath):
	aa = driver.find_element_by_xpath(xpath)
	return aa

class Web():
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
		el_clear(data['web']['register']['regaccount'])
		driver.find_element_by_xpath(data['web']['register']['regaccount']).send_keys(account)
		el_clear(data['web']['register']['regname'])
		el_regname(data['web']['register']['regname'])
		el_clear(data['web']['register']['regpassword'])
		driver.find_element_by_xpath(data['web']['register']['regpassword']).send_keys(password)
		el_clear(data['web']['register']['regsurepassword'])
		driver.find_element_by_xpath(data['web']['register']['regsurepassword']).send_keys(password)
		el_clear(data['web']['register']['regcheckcode'])
		el_yanzhenma(data['web']['register']['regcheckcode'])
		el_click("//*[@id=\"app\"]/div/div[3]/div/form/div[6]/div/button")
		if driver.appearence_xpath("//div[contains(@class,'el-form-item__error')]"):
			raise ValueError("请检查注册信息是否符合")
		else:
			self.drwen_touch(Template(r"tpl1573279080428.png", record_pos=(11.315, 2.885), resolution=(100, 100)))
			time.sleep(1)


	def login(self,account,password):
		driver.find_element_by_xpath(data['web']['login']['username']).send_keys(account)
		driver.find_element_by_xpath(data['web']['login']['password']).send_keys(password)
		el_yanzhenma(data['web']['login']['checkcode'])
		el_click(data['web']['login']['loginbutton'])
		if driver.appearence_xpath("//i[contains(@class,'el-icon-warning')]"):
			raise ValueError("请检查登录用户信息是否正确")
		else:
			el_click(data['web']['login']['agree_contract'])
			self.drwen_touch(Template(data['web']['login']['unannouncement'], record_pos=(12.01, 2.64), resolution=(100, 100)))

	def youkelogin(self):		
		el_click(data['web']['login']['youkelogin'])
		alert = driver.switch_to_alert()
		time.sleep(1)
		alert.accept()
		el_click(data['web']['login']['agree_contract'])
		self.drwen_touch(Template(data['web']['login']['unannouncement'], record_pos=(12.01, 2.64), resolution=(100, 100)))

	def gettext(self,xpath):
		el_click(xpath)
		text = el_gettext("//table/tbody/tr/td")
		#print("aaaa:{0}".format(text))


	def banding_bankcard(self):
		self.drwen_touch(Template(r"tpl1573023563827.png", record_pos=(10.535, 3.465), resolution=(100, 100)))
		self.drwen_touch(Template(r"tpl1573023583314.png", record_pos=(11.275, 3.695), resolution=(100, 100)))
		self.drwen_touch(Template(r"tpl1573023745049.png", record_pos=(11.72, 3.075), resolution=(100, 100)))
		self.drwen_touch(Template(r"tpl1573023770706.png", record_pos=(11.69, 3.985), resolution=(100, 100)))
		el_bankcard(data['web']['banding_bankcard']['bankcard_1'])
		el_bankcard(data['web']['banding_bankcard']['bankcard_2'])
		el_bankaddr(data['web']['banding_bankcard']['bankaddr'])
		self.drwen_touch(Template(r"tpl1573023950996.png", record_pos=(11.635, 6.355), resolution=(100, 100)))
		driver.assert_exist("//div[@role='alert']", "xpath", "银行卡信息有误或者已绑定")
		time.sleep(1)

	def load_balance(self):
		el_click(data['web']['load_balance']['load1'])
		el_click(data['web']['load_balance']['load2'])
		driver.find_element_by_xpath(data['web']['load_balance']['load3']).send_keys("5000")
		el_regname(data['web']['load_balance']['load4'])
		driver.find_element_by_xpath(data['web']['load_balance']['load5']).send_keys("2019-11-06")
		el_click(data['web']['load_balance']['load6'])

	def change_password(self):
		el_click(data['web']['change_password']['change1'])
		driver.find_element_by_xpath(data['web']['change_password']['change2']).send_keys("1234qwer")
		driver.find_element_by_xpath(data['web']['change_password']['change3']).send_keys("1234qwe")
		driver.find_element_by_xpath(data['web']['change_password']['change4']).send_keys("1234qwe")
		if driver.appearence_xpath(data['web']['change_password']['change5']):
			el_click(data['web']['change_password']['change5'])
		else:
			raise ValueError("请检查用户原密码是否正确")

	def betting(self,lottery):
		el_click(lottery)
		start_time = el_gettext(data['web']['betting']['bet2'])
		end_time = el_gettext(data['web']['betting']['bet3'])
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
		el_click(data['web']['betting']['betcheck'])
		el_click(data['web']['betting']['betcheckagain'])

	def check_win_lose(self):
		pagenum = driver.find_elements_by_xpath("//ul[contains(@class,'el-pager')]/li") #查询页数
		print("------{0}".format(pagenum))
		if pagenum == []:
			lie = len(driver.find_elements_by_xpath("//table/tbody/tr")) #查询行数
			print("-----{0}".format(lie))
			for i in range(lie):
				wanfa = el_gettext("//table/tbody/tr[{0}]/td[4]/div[1]".format(i+1))
				peilv = el_gettext("//table/tbody/tr[{0}]/td[4]/div[2]/span".format(i+1))
				touzhue = el_gettext("//table/tbody/tr[{0}]/td[6]".format(i+1))
				tuishui = el_gettext("//table/tbody/tr[{0}]/td[7]".format(i+1)).split("%")[0]
				shuying = el_gettext("//table/tbody/tr[{0}]/td[8]".format(i+1))
				result = float(touzhue)*(float(peilv)-1)+float(touzhue)*float(tuishui)/100
				result = ("%.3f"%result)
				if float(result) == float(shuying):
					print("玩法：{0}核对正确".format(wanfa))
				else:
					print("玩法：{0}  输".format(wanfa))
		for j in pagenum:
			j.click()
			time.sleep(3)
			lie = len(driver.find_elements_by_xpath("//table/tbody/tr")) #查询行数
			print("-----{0}".format(lie))
			for i in range(lie):
				wanfa = el_gettext("//table/tbody/tr[{0}]/td[4]/div[1]".format(i+1))
				peilv = el_gettext("//table/tbody/tr[{0}]/td[4]/div[2]/span".format(i+1))
				touzhue = el_gettext("//table/tbody/tr[{0}]/td[6]".format(i+1))
				tuishui = el_gettext("//table/tbody/tr[{0}]/td[7]".format(i+1)).split("%")[0]
				shuying = el_gettext("//table/tbody/tr[{0}]/td[8]".format(i+1))
				result = float(touzhue)*(float(peilv)-1)+float(touzhue)*float(tuishui)/100
				result = ("%.3f"%result)
				if float(result) == float(shuying):
					print("玩法：{0}核对正确".format(wanfa))
				else:
					print("玩法：{0}  输".format(wanfa))
