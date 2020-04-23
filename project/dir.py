# 选择出我所需要的任意文件
#  很多时候我们需要批量选出文件夹中相同文件类型的文件比如：我在网盘中下载了资源，里面包含了mp4,html,pdf,mp3而我只想选出html文件该怎么办？

import tkinter,os,shutil,re
from tkinter import filedialog

#用户输入要查找的类型文件
fileType = input()
#选择文件夹
needFileName = filedialog.askdirectory()
#用户选择后的文件夹
needFiles = os.listdir(needFileName)
# 存放移动文件的文件夹
finallyDir = os.path.join(os.path.dirname(needFileName),fileType)

if not os.path.exists(finallyDir):
    os.mkdir(finallyDir)

# for file in needFiles:
#     # print(file)
#     if os.path.isfile(file):  
#         print(file+" is dir")
    # elif bool(re.search(fileType,file)):
    #     print(file)
    # else:
    #     print("success " + file)    
        # print(os.path.join(os.path.dirname(needFileName),fileType))
        # print(os.path.dirname(needFileName))
        # shutil.copyfile(,finallyDir)
        
def Test1(rootDir): 
    list_dirs = os.walk(rootDir) 
    for root, dirs, files in list_dirs: 
        for d in dirs: 
            print(os.path.join(root, d) + "hello")     
        for f in files: 
            # 文件类型与输入的文件类型相同则移动到外面新建的文件夹中        
            if bool(re.search(fileType,f)):
                shutil.copy(os.path.join(root, f),finallyDir)
                
Test1(needFileName)