from imdbTask5 import *
from pprint import pprint

def directorsName(movieDirectors):
    directorsList=[]
    for i in movieDirectors:
        director=i["Directors"]
        directorsList.extend(director) 
    return(directorsList)
allDirectorsName=directorsName(movie_details)
# print(allDirectorsName)



def analyse_movies_directors(Directors):
    directorsDic={}
    for i in Directors:
        if i not in directorsDic:
            directorsDic[i]=1
        else:
            directorsDic[i]+=1
    return(directorsDic)
data=analyse_movies_directors(allDirectorsName)
# print(data)
