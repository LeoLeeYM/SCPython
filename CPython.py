#-*-conding:utf-8-*-

import LibraryAppend
import LibraryCreate
import Pretreatment
import Translation
import os
import sys
import subprocess


print(
"""
欢迎使用由岁悦科技工作室开发的

--------------
Suiyue CPython
--------------

SCPython 完全免费

岁悦会在岁悦官方网站 sywlit.com 上发布最新的 SCPython 解释器及官方IDE
任何个人及组织均可免费使用 SCPython 及其相关产品

您现在打开的是 SCPython 解释器
版本号为：b0.01.00
发布时间为：2019.8.18

请将使用 SCPython 语法格式编写的程序由文本形式导入，SCPython 解释器会自动执行

想为 SCPython 编写IDE？
联系我们：sywlit@126.com

""")
print("SCPython 译库版本："+LibraryCreate.Library_Version)
 

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


