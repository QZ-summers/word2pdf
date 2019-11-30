import os

# os.chdir("/var/www/html")#切换到指定目录
# os.getcwd()#返回该文件所在的目录
# fd=os.open("/tmp",os.O_RDONLY)#打开当前目录下的tmp文件
# os.fchdir(fd)#修改目录
# os.close()#关闭文件

path='H:\\123\\'
# if os.path.isdir(path):
# 	print("directory")
# elif os.path.isfile(path):
# 	print("file")
# else:
# 	print("not file or directory!")


# print(os.listdir(path))


for root,dirs,files in os.walk(path):
	for name in files:
		print(os.path.join(root,name))
	for name in dirs:
		print(os.path.join(root,name))

#Python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 
#范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
str.find(str, beg=0, end=len(string))