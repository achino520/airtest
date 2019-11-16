# -*- encoding=utf8 -*-
__author__ = "QQ"


import yaml
import os
import csv

def readyaml():
	path = os.path.join(os.path.dirname(__file__), "test.yaml")
	fr = open(path,'r',encoding='utf-8',errors='ignore')
	content = fr.read()
	fr.close()
	data = yaml.load(content,Loader=yaml.FullLoader)
	return data

def readcsv(filename):
	# 读取csv至字典
	file = filename
	path = os.path.join(os.path.dirname(file), "test.csv")
	csvFile = open(path, "r")
	reader = csv.reader(csvFile)

	# 建立空字典
	result = {}
	for item in reader:
		# 忽略第一行
		if reader.line_num == 1:
			continue
		result[item[0]] = item[1]

	csvFile.close()
	return result

