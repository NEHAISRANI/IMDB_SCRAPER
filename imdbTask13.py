from imdbTask4 import*
from imdbTask1 import*
from bs4 import BeautifulSoup
import requests
import json
import os 

def scrape_movie_cast_and_details(api):
    for i in api[200:251]:
        link=i["url"].split("/") 
        url1=link[5]
        # print(url1) 
        fileName1=("movieDetails/"+str(url1)+"_alldata.json")
        if os.path.exists(fileName1): 
            print("-----------------")
            file=open(fileName1,"r")
            readFile=file.read()
        else: 
            detailsOfMovies=Scrap_Movie_Details("https://www.imdb.com/title/"+str(url1)+"/")
            with open("moviesCast/"+str(url1)+"_cast.json","r") as file:
                readFile=json.load(file)
                print(readFile)
                detailsOfMovies["cast"]=readFile
                convert=(detailsOfMovies) 
                convert1=json.dumps(convert)
            with open("movieDetails/"+str(url1)+"_alldata.json","w") as write_file:
                write1=write_file.write(convert1) 
    return(readFile) 
allMovieData=scrape_movie_cast_and_details(moviesInfo)  
# print(allMovieData)


