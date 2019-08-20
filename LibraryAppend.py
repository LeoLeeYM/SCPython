
Code_Base = [] #初始化基本库
Code_Core = [] #初始化核心库
Code_Method = [] #初始化方法库

def Join_Code(Code,Replace_Code,Library):
    
    if Library == "Base":
        Code_Base.append([Code,Replace_Code])

    if Library == "Core":
        Code_Core.append([Code,Replace_Code])

    if Library == "Method":
        Code_Method.append([Code,Replace_Code])