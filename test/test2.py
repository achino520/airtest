import yaml
import os
def readyaml():
	path = os.path.join(os.path.dirname(__file__), "ti.yaml")
	fr = open(path,'r',encoding='utf-8',errors='ignore')
	content = fr.read()
	fr.close()
	data = yaml.load(content,Loader=yaml.FullLoader)
	return data

data = readyaml()
print(data)