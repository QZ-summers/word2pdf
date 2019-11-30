
import sys
import os
import comtypes.client

def Word2Pdf(doc_name,pdf_name):    #自定义word转pdf函数
	word=comtypes.client.CreateObject('Word.Application') #调用word应用程序
	doc=word.Documents.Open(doc_name)   #用word应用程序打开word文档
	doc.SaveAs(pdf_name,FileFormat=17)	#将word文档保存为pdf文档
	doc.Close()
	word.Quit()


#查找路径下的所有word文件

try:
	file_path='H:\\123\\'#路径名中不能有中文字符
	i=0

	file_list=os.listdir(file_path)
	for file_name in file_list:

		doc_name=file_path+file_name
		pdf_name=""

		if file_name.split(".")[-1]=="docx" :     #判断是否为word文档，是则执行，否则跳过
			i=i+1
			for file_name_part in file_name.split("."):    #对是word文档的文件名按“.”进行分割，将docx之前的文件名进行连接
				if file_name_part=="docx":				   #并将"docx"改为“pdf”，形成pdf的文件名
					pdf_name=pdf_name+"pdf"
				else:
					pdf_name=pdf_name+file_name_part+"."

			pdf_name=file_path+pdf_name    #pdf全路径文件名
			Word2Pdf(doc_name,pdf_name)
			print(str(i)+"、"+doc_name)
			print(str(i)+"、"+pdf_name)
		else:
			continue
except Exception as e:
	print("出现错误，错误是：",e)
			

