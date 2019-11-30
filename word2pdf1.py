import sys
import os
import comtypes.client

def Word2Pdf(doc_name,pdf_name):    #自定义word转pdf函数
	word=comtypes.client.CreateObject('Word.Application') #调用word应用程序
	doc=word.Documents.Open(doc_name)   #用word应用程序打开word文档
	doc.SaveAs(pdf_name,FileFormat=17)	#将word文档保存为pdf文档
	doc.Close()
	word.Quit()

#递归函数实现所有文件的查找
def Find_file(path):
	i=0
	file_list=os.listdir(path)
	for file_name in file_list:
		file_full_name=path+file_name
		if os.path.isfile(file_full_name):
			#doc_name=file_path+file_name
			doc_name=file_full_name
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
			# print("file")
		elif:------------------------------------------------------
			print("not file or directory!")
		if os.path.isdir(file_full_name):
			Find_file(file_full_name)
			print(file_full_name)




	print(os.listdir(path))

--------------------------------------------------------------------------------

if __name__ == '__main__':

	path='H:\\123\\'
	Find_file(path)