import os

path="H:\\123\\"

#搜索文件
filename="123.docx"

def file(filenme):
	for root,dirs,files in os.walk(path):
		return files,dirs,root



test=os.walk(path)
print(test)
print("--------------------------------------------")
for a,b,c in os.walk(path):
#for a,b,c in test:
	print(a)
	print(b)
	print(c)
	print("--------------------------------------------")

test=file(filename)#一次只返回一次递归的值
print(test)
print(test[0])
print("--------------------------------------------")

for a,b,c in os.walk(path):
	# for d in a:
	# 	print(d)
	for e in b:
		print(e)
	for f in c:
		g=os.path.abspath(f)#当前运行程序的路径+文件名---是错误的---想要的是查找的文件的路径
		h=os.path.join(a,f)
		print(h)
		print(g)
	print("--------------------------------------------")

# print(os.walk(path))




	# print(files)
# print(dirs)
	# for name in files:
	# 	if filename==name:
	# 		print(os.path.join(root,name))
	# 	else:
	# 		print("没有这个文件！")