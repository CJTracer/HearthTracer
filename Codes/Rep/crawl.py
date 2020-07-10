#head
import urllib.request
import requests
import os 

print("输入赛事在旅法师营地上的完整地址")

url=input()

ele = requests.get(url)

print(ele.text)
