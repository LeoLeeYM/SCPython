
import LibraryAppend

Text_Replace_Number = 1
Temporary_Text_Storage = []

def Translation_Code(Code_List):
   
    num1 = 0
    num2 = 0
    num3 = 0
    Text_Code = ""
    
    List_Code = Code_List
    Progress = len(List_Code) * 4
    Single = 1 / Progress
    lattice = Progress / 10

    Cumulative = 0

    print("正在解释:",end = "")

    for Row in List_Code:

        List_Code[num1] = Text_Removal(Row)

        Cumulative += 1
        if Cumulative > lattice:
            print("■■",end = "")
            Cumulative = 0
        num1 += 1

    for Row1 in List_Code:

        List_Code[num2] = Replace_Base(Row1)
        List_Code[num2] = Replace_Core(List_Code[num2])
        List_Code[num2] = Replace_Method(List_Code[num2])

        Cumulative += 1
        if Cumulative > lattice:
            print("■■",end = "")
            Cumulative = 0
        num2 += 1

    for Row2 in List_Code:

        List_Code[num3] = Text_Restores(Row2)

        Cumulative += 1
        if Cumulative > lattice:
            print("■■",end = "")
            Cumulative = 0
        num3 += 1


    for Row3 in List_Code:

        Text_Code = Text_Code + Row3 + "\n"

        Cumulative += 1
        if Cumulative > lattice:
            print("■■",end = "")
            Cumulative = 0
    print("■■")
    return Text_Code


def Text_Removal(Code_Row):
#逐字符查找取区间自定义文字

    global Text_Replace_Number
    global Temporary_Text_Storage

    Row_Code = Code_Row
    Recording = ""
    position = 0
    num = 0

    Row_Code = Symbol_Replacement(Row_Code)
    
    num1 = 0

    while True:
        
        if Row_Code == "":
            break
        
        if Recording == "":
           
            if Row_Code[num1] == '"""':
                Recording = '"'
                position = num

                continue

            if Row_Code[num1] == '"':
                Recording = '"'
                position = num

                continue
            if Row_Code[num1] == "'":
                Recording = "'"
                position = num

                continue
        else:
            
            if Row_Code[num1] == Recording:

                if position != num:

                
                    Interval_Text = Row_Code[position:num + 1]
                    Replace_Text = f"/Suiyue_thbs{Text_Replace_Number}thbs_Suiyue/"
                    position = 0
                    Text_Replace_Number += 1

                    Temporary_Text_Storage.append([Replace_Text,Interval_Text])

                    Row_Code = Row_Code.replace(Interval_Text,Replace_Text)

                    Recording = ""
        num += 1

        if len(Row_Code) - 1 == num1:
            break
        num1 += 1

        
    return Row_Code
        

    
def Text_Restores(Code_Row):
    global Temporary_Text_Storage

    Code = Code_Row
    for i in Temporary_Text_Storage:
        Code = Code.replace(i[0],i[1])
    return Code
    

#执行替换
def Replace_Base(Code):

    Replace_Code = Code

    for i in LibraryAppend.Code_Base:
        
        Replace_Code = Replace_Code.replace(i[1],i[0])

    return Replace_Code


def Replace_Core(Code):
    
    Replace_Code = Code

    for i in LibraryAppend.Code_Core:
        Replace_Code = Replace_Code.replace(i[1],i[0])

    return Replace_Code


def Replace_Method(Code):
    
    Replace_Code = Code

    for i in LibraryAppend.Code_Method:
        Replace_Code = Replace_Code.replace(i[1],i[0])

    return Replace_Code

def Symbol_Replacement(Code):
    Code_Text = Code

    Code_Text = Code_Text.replace("“",'"')
    Code_Text = Code_Text.replace("”",'"')

    Code_Text = Code_Text.replace("‘","'")
    Code_Text = Code_Text.replace("’","'")

    Code_Text = Code_Text.replace("！",'!')
    Code_Text = Code_Text.replace("？",'?')
    Code_Text = Code_Text.replace("。",'.')

    Code_Text = Code_Text.replace("（",'(')
    Code_Text = Code_Text.replace("）",')')

    Code_Text = Code_Text.replace("【",'[')
    Code_Text = Code_Text.replace("】",']')

    Code_Text = Code_Text.replace("《",'<')
    Code_Text = Code_Text.replace("》",'>')

    Code_Text = Code_Text.replace("：",':')

    return Code_Text#中文符号替换