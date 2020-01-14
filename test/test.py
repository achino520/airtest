#encoding=utf-8
from airtest_selenium.proxy import WebChrome
import functools
from yamlinclude import YamlIncludeConstructor
import json
import yaml
import os
import win32gui,win32con
import win32api
import multiprocessing
import win32process
import time
from airtest.core.api import *
import psutil
ST.FIND_TIMEOUT = 6


def get_hwd():
	hWndList = []
	hwdl = []
	win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
	for i in hWndList:
		if "Google Chrome" in win32gui.GetWindowText(i):
			hwdl.append(i)
	hwd = hwdl
	return hwd

def drwen_touch(v,driver,pid):
	hwnds = get_hwd()
	for hwnd in hwnds:
		if win32process.GetWindowThreadProcessId(hwnd)[1] == pid:
			pos = driver.zuobiao(v)
			tmp=win32api.MAKELONG(pos[0],pos[1])
			win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,tmp)
			time.sleep(0.05)
			win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP,win32con.MK_LBUTTON,tmp)

YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.FullLoader, base_dir=os.path.dirname(__file__))

def readyaml():
	path = os.path.join(os.path.dirname(__file__), "testym.yaml")
	fr = open(path,'r',encoding='utf-8',errors='ignore')
	content = fr.read()
	fr.close()
	data = yaml.load(content,Loader=yaml.FullLoader)
	return data



def click(func):
	@functools.wraps(func)
	def wraper(*args,**kw):
		return func(*args,**kw).click()
	return wraper

def send_keys(words):
	def text(func):
		@functools.wraps(func)
		def wraper(*args,**kw):
			func(*args,*kw).clear()
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
#封装方法

def el_find(driver,xpath):
	aa = driver.find_element_by_xpath(xpath)
	return aa

@click
def el_click(driver,xpath):
	return el_find(driver,xpath)


@clear
def el_clear(driver,xpath):
	return el_find(driver,xpath)

@get_text
def el_gettext(driver,xpath):
	return el_find(driver,xpath)



def el_assertlogin(driver,xpath):
	if driver.appearence_xpath(xpath):
			print("请检查登录用户信息是否正确")
			return 0
	else:
		return 1


def get_target_value(key, dic, tmp_list):
    """
    :param key: 目标key值
    :param dic: JSON数据
    :param tmp_list: 用于存储获取的数据
    :return: list
    """
    if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
        return 'argv[1] not an dict or argv[-1] not an list '

    if key in dic.keys():    	
        tmp_list.append(dic) # 传入数据存在则存入tmp_list

    for value in dic.values():  # 传入数据不符合则对其value值进行遍历
        if isinstance(value, dict):
            get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
        elif isinstance(value, (list, tuple)):
            _get_value(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用_get_value

    return tmp_list


def _get_value(key, val, tmp_list):
    for val_ in val:
        if isinstance(val_, dict):  
            get_target_value(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
        elif isinstance(val_, (list, tuple)):
            _get_value(key, val_, tmp_list)   # 传入数据的value值是列表或者元组，则调用自身


def logic_betting(driver,xpath):
	start_time = driver.find_element_by_xpath(xpath[0]).text
	end_time = driver.find_element_by_xpath(xapth[1]).text
	end_time = end_time.split(":")
	end_time = int(end_time[0]*60) + int(end_time[1])
	start_time = start_time.split(":")
	start_time = int(start_time[0]*60) + int(start_time[1])
	if (start_time < 5) and (start_time > 0):
		sleep(start_time + end_time+2)
	elif (start_time == 0):
		sleep(end_time+2)

def logic_for_click(driver,xpath):
	for dev in driver.find_elements_by_class_name(xpath):
		dev.click()

def logic_checkwinlose(driver,xpath):
	pagenum = driver.find_elements_by_xpath(xpath[0]) #查询页数
	if pagenum == []:
		lie = len(driver.find_elements_by_xpath(xpath[1])) #查询行数
		for i in range(lie):
			wanfa = driver.find_element_by_xpath(xpath[2].format(i+1)).text
			peilv = driver.find_element_by_xpath(xpath[3].format(i+1)).text
			touzhue = driver.find_element_by_xpath(xpath[4].format(i+1)).text
			tuishui = driver.find_element_by_xpath(xpath[5].format(i+1)).text.split("%")[0]
			shuying = driver.find_element_by_xpath(xpath[6].format(i+1)).text
			result = float(touzhue)*(float(peilv)-1)+float(touzhue)*float(tuishui)/100
			result = ("%.3f"%result)
			if float(result) == float(shuying):
				print("玩法：{0}核对正确".format(wanfa))
			else:
				print("玩法：{0}  输".format(wanfa))
	for j in pagenum:
		j.click()
		time.sleep(3)
		lie = len(driver.find_elements_by_xpath(xpath[1])) #查询行数
		for i in range(lie):
			wanfa = driver.find_element_by_xpath(xpath[2].format(i+1)).text
			peilv = driver.find_element_by_xpath(xpath[3].format(i+1)).text
			touzhue = driver.find_element_by_xpath(xpath[4].format(i+1)).text
			tuishui = driver.find_element_by_xpath(xpath[5].format(i+1)).text.split("%")[0]
			shuying = driver.find_element_by_xpath(xpath[6].format(i+1)).text
			result = float(touzhue)*(float(peilv)-1)+float(touzhue)*float(tuishui)/100
			result = ("%.3f"%result)
			if float(result) == float(shuying):
				print("玩法：{0}核对正确".format(wanfa))
			else:
				print("玩法：{0}  输".format(wanfa))


def runtest(driver,pid,k=[],kk=[]):
	for i in k:
		if i['event'] == "el_sendkey":
			el_clear(driver,i['xpath'])
			el_find(driver,i['xpath']).send_keys(i['params'])
		elif i['event'] == "el_click":
			el_click(driver,i['xpath'])
		elif i['event'] == "el_assertlogin":
			if el_assertlogin(driver,i['xpath']):
				pass
			else:
				break
		elif i['event'] == "drwen_click":
			drwen_touch(Template(i["xpath"], record_pos=i["params"], resolution=(100, 100)),driver,pid)
			time.sleep(3)
		elif i['event'] == "0":
			runtest(driver,pid,kk[0])
		elif i['event'] == "logic_betting":
			logic_betting(driver,i["xpath"])
		elif i['event'] == "logic_for_click":
			logic_for_click(driver,i["xapth"])
		elif i['event'] == "logic_checkwinlose":
			logic_checkwinlose(driver,i["xpath"])

		else:
			raise


#提取yaml文件
data = readyaml()
counts= len(data['web'])
#读取所有ord值
ords = get_target_value('ord',data,[])


# 测试步骤排序，按照ord值解析出测试用例并对测试步骤排序
testcases=[]
for j in range(counts):
	ordl=[]
	testl=[]
	for i in ords:
		if int(i['ord'][:3]) == j:
			ordl.append(i['ord'])
			ordl.sort()
	for j in ordl:
		for i in ords:
			if i['ord'] == j:
				testl.append(i)

	testcases.append(testl)


for k in testcases:
	driver = WebChrome()
	driver.implicitly_wait(8)
	#测试执行
	driver.get("https://member.163220.com/#/home")
	driver.maximize_window()

	pid = psutil.Process(driver.service.process.pid).children(recursive=True)[0].pid
	#元素绑定方法
	try:
		runtest(driver,pid,k,testcases)
		
				
	except:
		raise
	finally:
		driver.close()



# # 导入turtle包的所有内容:
# from turtle import *

# # 设置色彩模式是RGB:
# colormode(255)

# lt(90)

# lv = 14
# l = 120
# s = 45

# width(lv)

# # 初始化RGB颜色:
# r = 0
# g = 0
# b = 0
# pencolor(r, g, b)

# penup()
# bk(l)
# pendown()
# fd(l)

# def draw_tree(l, level):
#     global r, g, b
#     # save the current pen width
#     w = width()

#     # narrow the pen width
#     width(w * 3.0 / 4.0)
#     # set color:
#     r = r + 1
#     g = g + 2
#     b = b + 3
#     pencolor(r % 200, g % 200, b % 200)

#     l = 3.0 / 4.0 * l

#     lt(s)
#     fd(l)

#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     rt(2 * s)
#     fd(l)

#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     lt(s)

#     # restore the previous pen width
#     width(w)

# speed("fastest")

# draw_tree(l, 4)

# done()
# # from enum import Enum

# # Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# # for name, member in Month.__members__.items():
# #     print(name, '=>', member, ',', member.value)

# # from airtest.core.api import *


# # auto_setup(basedir="C:\\Users\\QQ\\Desktop",logdir=True,project_root="D:\\test\\Airproject\\invech\\android")
# # using("common.air")
# # from common import *
# # connect_device("android:///")
# # device()
# # assert_equal("test","test","sdfds")
# # import functools

# # def log(exec):
# # 	print(exec)
# # 	def tester(func):
# # 		@functools.wraps(func)
# # 		def wraper(*args,**kw):
# # 			print("洪杰死全家")
# # 			return func(*args,**kw)
# # 		return wraper
# # 	return tester


# # @log("你好")
# # def ming(a):
# # 	print("nihao:{0}".format(a))

# # print(ming.__name__)
