# Requests will allow you to send https requests.It allows you to access the response data of python in the same way.
import requests
#BeautifulSoup is a python library for pulling data from htl and  xml files 
from bs4 import BeautifulSoup
# pprint used for makes our code beautiful. 
from pprint import pprint

url=" https://www.imdb.com/india/top-rated-indian-movies/" #get the data from imdb api

res=requests.get(url)

soup=BeautifulSoup(res.text,"html.parser")#parser is convert the data html and xml
# pprint(soup)

Title=soup.find("tbody",class_="lister-list")

tr_data=Title.find_all("tr")

movies_list=[]

def scrape_top_list(trs):
	position=1
	for movie in trs:
		movie_details={}
		name=movie.find("td",class_="titleColumn").a.get_text()
		year=movie.find("td",class_="titleColumn").span.get_text()
		ratings=movie.find("td",class_="ratingColumn imdbRating").strong.get_text()
		movie_details["url"]=urlyear=movie.find("td",class_="titleColumn").span.get_text()
		ratings=movie.find("td",class_="ratingColumn imdbRating").strong.get_text()
		Urls=movie.find("a")["href"]
		movie_urls="https://www.imdb.com/"+Urls
		# print(url)
		movie_details["position"]=position
		movie_details["name"]=name
		movie_details["year"]=int(year[1:5])
		movie_details["url"]=movie_urls
		movie_details["ratings"]=ratings
		position=position+1
		movies_list.append(movie_details)
	return (movies_list)
moviesInfo=(scrape_top_list(tr_data))
# pprint(moviesInfo)



