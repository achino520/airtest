# -*- encoding=utf8 -*-
__author__ = "QQ"

import yaml
import os
import csv
from yamlinclude import YamlIncludeConstructor
import json


YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.FullLoader, base_dir=os.path.dirname(__file__))

def readyaml():
	path = os.path.join(os.path.dirname(__file__), "test.yaml")
	fr = open(path,'r',encoding='utf-8',errors='ignore')
	content = fr.read()
	fr.close()
	data = yaml.load(content,Loader=yaml.FullLoader)
	return data


# with open('test.yaml',encoding='utf-8') as f:  #美化输出
#     data = yaml.load(f, Loader=yaml.FullLoader)

# jsonDumpsIndentStr = json.dumps(data, indent=1);
# print(jsonDumpsIndentStr)


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