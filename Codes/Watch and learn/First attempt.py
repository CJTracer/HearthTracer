#head
import urllib.request
import requests
import os 


#const
file_name=["./Output"]


#make file

path=os.path.dirname(os.path.dirname(os.getcwd()))


count=0
for name in file_name:
    count+=1
    path_tem=path+name
    if(os.path.exists(path_tem)==False):
        os.chdir(path)
        print(path_tem)
        os.mkdir(path_tem)
    os.chdir(path_tem)
    source=open('deck'+str(count)+'.txt','w',encoding='utf8')



#crawl
response = urllib.request.urlopen('https://www.iyingdi.com/web/tools/hearthstone/decks/deckdetail/5419309?btypes=home_allset_setdetail&setid=1021902')

