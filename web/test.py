#coding=utf-8
# __author__ = 'Administrator'



# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
 
# __doc__ = '''
# pythonwin中win32gui的用法
# 本文件演如何使用win32gui来遍历系统中所有的顶层窗口，
# 并遍历所有顶层窗口中的子窗口
# '''
 
import win32gui
from pprint import pprint
import win32con
import win32api
import time
from selenium import webdriver
# def gbk2utf8(s):
#     return s.decode('gbk').encode('utf-8')
 

# def show_window_attr(hWnd):
#     '''
#     显示窗口的属性
#     :return:
#     '''
#     if not hWnd:
#         return
 
#     #中文系统默认title是gb2312的编码
#     title = win32gui.GetWindowText(hWnd)
#     title = gbk2utf8(title)
#     clsname = win32gui.GetClassName(hWnd)
 
#     # print '窗口句柄:%s ' % (hWnd)
#     # print '窗口标题:%s' % (title)
#     # print '窗口类名:%s' % (clsname)
#     # print ''
 
# def show_windows(hWndList):
#     for h in hWndList:
#         show_window_attr(h)
 
# def demo_top_windows():
#     '''
#     演示如何列出所有的顶级窗口
#     :return:
#     '''
#     hWndList = []
#     win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
#     show_windows(hWndList)
 
#     return hWndList
 
# def demo_child_windows(parent):
#     '''
#     演示如何列出所有的子窗口
#     :return:
#     '''
#     if not parent:
#         return
 
#     hWndChildList = []
#     win32gui.EnumChildWindows(parent, lambda hWnd, param: param.append(hWnd),  hWndChildList)
#     show_windows(hWndChildList)
#     return hWndChildList
 

# c = webdriver.Chrome()
# c.service.process # is a Popen instance for the chromedriver process
# import psutil
# p = psutil.Process(c.service.process.pid)
# #print(p.pid)
# print(p.children(recursive=True)[0].pid)

import win32process
  
a = win32process.GetWindowThreadProcessId(1380352)
print(a[1])

# def get_hwnds_for_pid(pid):
# 	# 通过PID查询句柄ID
# 	def callback(hwnd, hwnds):
# 		if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
# 			_, found_pid = win32process.GetWindowThreadProcessId(hwnd)
# 			if found_pid == pid:
# 				hwnds.append(hwnd)
# 			return True
 
# 	hwnds = []
# 	win32gui.EnumWindows(callback, hwnds)
# 	hwndy = 0
# 	if hwnds:
# 		hwndy = hwnds[0]
 
# 	return hwndy
 
 

# print(get_hwnds_for_pid(163704))


# hWndList = []
# win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
# hWndList.sort()
# for i in hWndList:
# 	if "Google Chrome" in win32gui.GetWindowText(i):
# 		print(i,win32gui.GetWindowText(i))

	#print("{0} is {1}".format(i,win32gui.GetWindowText(i)).encode(''))
#print(hWndList)
# # assert len(hWndList)
 
# # parent = hWndList[20]
# # #这里系统的窗口好像不能直接遍历，不知道是否是权限的问题
# # hWndChildList = demo_child_windows(parent)
 
# # print('-----top windows-----')
# # pprint(hWndList)
 
# # print('-----sub windows:from %s------' % (parent))
# # pprint(hWndChildList)
# # 4065908[66064, 66018, 65858, 65922, 65918, 65912, 65908, 65892, 65946, 65944, 65930, 65926, 65848, 65928, 65894, 131712, 66208, 66230, 66228, 3278248, 4459524, 395722, 65966, 1182590, 67882, 65990, 65992, 66830, 197696, 65730, 65808, 263410, 67588, 199576, 2296144, 1051430, 133042, 395464, 2099718, 4260966, 263148, 525048, 132256, 4982820, 7733868, 330636, 526718, 263566, 2950854, 1181804, 4458910, 855024, 5048692, 2492508, 5114342, 264666, 1115990, 3213934, 263038, 3148572, 1379440, 4065908, 3934756, 1772610, 1576168, 262774, 2690078, 5704970, 2493488, 1640850, 4196456, 984448, 1443854, 591212, 3082352, 1707228, 2164080, 1837540, 527106, 852584, 2624502, 1903008, 6228018, 1837814, 1443262, 1049226, 2164684, 2032980, 197466, 2820456, 330314, 264602, 657920, 1509274, 198376, 132882, 198444, 1968230, 1245820, 2428130, 65998, 394594, 920770, 1837732, 1313706, 1379564, 1575946, 2099238, 1378600, 1902880, 789710, 1443936, 1444876, 2230742, 2754902, 1706988, 984240, 396266, 527548, 1444284, 525316, 199614, 3017132, 264330, 6292560, 5114356, 592430, 264526, 395576, 329794, 67910, 133366, 4786362, 2361518, 65798, 67278, 67136, 3147204, 1050030, 984490, 591316, 2426026, 132216, 197460, 197728, 197456, 459882, 132236, 132136, 132276, 132162, 66784, 66776, 66746, 66718, 66710, 66686, 66670, 66664, 66614, 66610, 66698, 66592, 66510, 66472, 66466, 66464, 66460, 131968, 66318, 66316, 66312, 66302, 66252, 66242, 66236, 66216, 131694, 131700, 66048, 66078, 131262, 66112, 66054, 66022, 66020, 65994, 65982, 65980, 131410, 65948, 131142, 65832, 65828, 65754, 65810, 65804, 131116, 131190, 131144, 66588, 66690, 66682, 132084, 132088, 132720, 67238, 263838, 132746, 67092, 
# #win32gui.SetForegroundWindow(527516)
#win32gui.SendMessage(329446, win32con.MOUSEEVENTF_LEFTDOWN, 100, 200)
# pos = (813,281)
# a = 790348
# tmp=win32api.MAKELONG(pos[0],pos[1])
# print(tmp)
# win32gui.PostMessage(a, win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,tmp)
# time.sleep(0.05)
# win32gui.SendMessage(a, win32con.WM_LBUTTONUP,win32con.MK_LBUTTON,tmp)