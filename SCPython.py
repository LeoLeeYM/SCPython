#-*-conding:utf-8-*-

import LibraryAppend
import LibraryCreate
import Pretreatment
import Translation
import os
import sys
import subprocess

print("-----------------------------------------")
file_name = input("输入'/帮助',则进入SCPython的使用帮助\n输入'/自定义',则进入自定义模式\n输入SCPython代码文件地址则执行解释\n\n请输入：")

while file_name == "":
    
    file_name = input("您刚才未输入指令，请重新输入：")

if file_name == "/帮助":
    pass
elif file_name == "/自定义":
    pass
else:
    file = open(file_name,encoding = 'utf-8')
    file_text = file.read()

    List_Code = Pretreatment.Decomposition_Code(file_text)

    Text = Translation.Translation_Code(List_Code)
 
    file_new = open(os.environ["TMP"] + "\SCPYFile.py","w",encoding = 'utf-8')
    file_new.write(Text)
    file_new.close()
    os.system('cls')  

    os.system(os.environ["TMP"] + r'"\SCPYFile.py"')


