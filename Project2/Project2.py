# bs4 is a package and beautifulsoup is python library
from bs4 import BeautifulSoup 
# Requests will allow you to send https requests.It allows you to access the response data of python in the same way.
import requests 
# pprint used for makes our code beautiful.
from pprint import pprint
# json used for perform some methods on dictionay/json string(loads,dumps).
import json

url="https://paytmmall.com/fmcg-sauces-pickles-glpid-101471?page=1&latitude=12.868065800000002&longitude=77.7128736"
response=requests.get(url)
# print response.text

soup=BeautifulSoup(response.text,"lxml")
# print soup
pickleDetails=soup.find("div",class_="_2Bze")
# print pickleDetails


for i in pickleDetails:
    PickleDict={} 
    allPickleOfPrices=i.find_all("div",class_="_2bo3")
    # print allPickleOfPrices  
    allPickleOfImages=i.find_all("div",class_="_3nWP")  
    # print allPickleOfImages
    allPickleOfUrl=i.find_all("div",class_="_3WhJ")
    # print allPickleOfUrl
    allPickleOfNames=i.find_all("div",class_="pCOS")
    # print allPickleOfNames
    for index in allPickleOfImages:
        images=index.img["src"]
        print (images)
    for index in allPickleOfPrices:
        prices=index.find("div",class_="_1kMS").span.get_text()
        # print prices
    for index in allPickleOfUrl:
        Url=index.a["href"]
        # print Url
    for index in allPickleOfNames:
        names=index.find("div",class_="_2apC").get_text()
        # print names
    

        PickleDict["picklePrices"]=prices
        PickleDict["pickleImages"]=images
        PickleDict["pickleUrls"]=Url
        PickleDict["pickleNames"]=names
        print (PickleDict)
