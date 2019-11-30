import sys
import os
import comtypes.client

#自定义word转pdf函数
def Single_Word2Pdf(doc_name,pdf_name):    
	word=comtypes.client.CreateObject('Word.Application') #调用word应用程序
	doc=word.Documents.Open(doc_name)   #用word应用程序打开word文档
	doc.SaveAs(pdf_name,FileFormat=17)	#将word文档保存为pdf文档
	doc.Close()
	word.Quit()

#
def Batch_Word2Pdf(path):
	i=0
	for root,dirs,files in os.walk(path):#返回目录路径、当前目录下的文件夹、当前目录下的文件
		#i=0
		for file_name in files:
			#doc_name=root+file_name
			# doc_name=os.path.abspath(file_name)
			#doc_name=os.path.join(root,file_name)
			pdf_name=""

			if file_name.split(".")[-1]=="docx" :     #判断是否为word文档，是则执行，否则跳过
				i=i+1
				doc_name=os.path.join(root,file_name)
				print("正在读取第"+str(i)+"个docx文件："+doc_name)
				for file_name_part in file_name.split("."):    #对是word文档的文件名按“.”进行分割，将docx之前的文件名进行连接
					if file_name_part=="docx":				   #并将"docx"改为“pdf”，形成pdf的文件名
						pdf_name=pdf_name+"pdf"
					else:
						pdf_name=pdf_name+file_name_part+"."

				#pdf_name=file_path+pdf_name    #pdf全路径文件名
				pdf_name=os.path.join(root,pdf_name)
				Single_Word2Pdf(doc_name,pdf_name)
				# print(str(i)+"、"+doc_name)
				print("成功转换第"+str(i)+"个docx2pdf文件："+pdf_name)
			else:
				continue			


if __name__ == '__main__':

	path='H:\\123\\'
	Batch_Word2Pdf(path)


##现在只能将word转换成pdf格式，后续可以可以继续改进，如增加要转换的格式的接口，实现各种文件格式的互转
