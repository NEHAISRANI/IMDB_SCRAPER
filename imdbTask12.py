from bs4 import BeautifulSoup
import requests
from pprint import pprint
import json
from imdbTask1 import *
import os 

def scrape_movie_cast():
    for i in moviesInfo[:11]:
        movieUrl=i["url"].split("/")
        Url=(movieUrl[5])
        fileName1=("moviesCast/"+str(movieUrl[5])+"_cast.json")
        if os.path.exists(fileName1): 
            print("-----------------")
            file=open(fileName1,"r")
            readFile=file.read()
            print(readFile) 
        else:
            url="https://www.imdb.com/title/"+str(Url)+"/fullcredits?ref_=tt_cl_sm"
            res=requests.get(url) 
            soup=BeautifulSoup(res.text,"html.parser")
            tbody=soup.find("table",class_="cast_list")
            td=tbody.find_all("td",class_="") 
            castList=[]  
            castDic={}  
            for i in td:  
                aTag=i.a
                Tag=aTag["href"].split("/")
                hrefTag=Tag[2]
                castDic["imdb_id"]= hrefTag
                print(castDic)
                castDic["name"]= aTag.get_text().strip()
                dictioinary_copy=castDic.copy()
                castList.append(dictioinary_copy)
            with open("moviesCast/"+str(movieUrl[5])+"_cast.json","w") as file:
                write=json.dump(castList,file) 
moviesCast=scrape_movie_cast()
# print(moviesCast)

