from bs4 import BeautifulSoup
import requests
from pprint import pprint

def extract_data_from_imdb(movie_url):
    res=requests.get(movie_url)
    soup=BeautifulSoup(res.text,"html.parser")
    return(soup)

dictionary={}
def extract_language_country_from_imdb(imdb_data):
    allCountryData=imdb_data.find("div",class_="article",id="titleDetails")
    country=allCountryData.find_all("div",class_="txt-block")
    language=[] 
    try: 
        for index in country[:3]: 
            h4_tag=index.find("h4",class_="inline").get_text()
            if h4_tag=="Country:":
                country=(index.a.get_text())
            if h4_tag=="Language:":
                a_tag=index.find_all("a") 
                for j in a_tag:
                    language.append(j.get_text())   
    except AttributeError: 
        print("------------")
    dictionary["language"]=language
    dictionary["country"]=country
    
def extract_director_bio_from_imdb(imdb):
    bio_and_director=imdb.find("div",class_="plot_summary")
    Bio=bio_and_director.find("div",class_="summary_text").get_text().strip()
    
    Directors_name=[] 
    director=bio_and_director.find("div","credit_summary_item")
    for i in director.find_all("a"): 
        Directors_name.append(i.get_text())
    dictionary["bio"]=Bio
    dictionary["Directors"]=Directors_name 
def extract_name_time(imdb):
    nameAndtime=imdb.find("div",class_="title_wrapper")
    movie_name=nameAndtime.h1.get_text()
    i=0
    name=" "
    while i<len(movie_name):
        if movie_name[i]=="(" :
            break
        name=name+movie_name[i]
        i=i+1
    Time=nameAndtime.find("div",class_="subtext").time["datetime"]
    i=0
    time_in_min=""
    while i<len(Time):
        if Time[i].isdigit():
            time_in_min=time_in_min+(Time[i])
        i=i+1
    dictionary["name"]=name.strip("\xa0")
    dictionary["runtime"]=time_in_min
def extract_poster_genre_info(imdb):
    Poster_image_url=imdb.find("div",class_="poster")
    image_url=(Poster_image_url.img["src"])
    # print(image_url)
    genre_info=imdb.find_all("div",class_="see-more inline canwrap")
    for i in genre_info:
        genre=(i.find("h4",class_="inline").get_text())
        if genre=="Genres:":
            a_tag=i.find_all("a")
            genre_list=[]
            for j in a_tag:
                genre_list.append(j.get_text())
    dictionary["poster_img_url"]=image_url 
    dictionary["genre"]=genre_list


def Scrap_Movie_Details(movie_url):
    soup=extract_data_from_imdb(movie_url)
    languageAndCountry=extract_language_country_from_imdb(soup)
    DirectorAndBio=extract_director_bio_from_imdb(soup)
    NameTime=extract_name_time(soup) 
    poster_genre=extract_poster_genre_info(soup)
    return(dictionary)  
url="https://www.imdb.com/title/tt1438298/"
particular_movie_details=(Scrap_Movie_Details(url))
pprint(particular_movie_details)

