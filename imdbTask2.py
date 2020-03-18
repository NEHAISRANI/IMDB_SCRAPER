from imdbTask1 import *
from pprint import pprint
def sortedMoviesYear(movies):
    moviesYear=[]
    index=0
    while index<len(movies):
        if movies[index]["year"] not in moviesYear:
            moviesYear.append(movies[index]["year"])
        index=index+1 
    return(moviesYear)
sortedYears=(sortedMoviesYear(moviesInfo))
# print(sortedYears)

def group_by_year(Years):
    index=0
    dic={}
    while index<len(Years):
        j=0
        commonyearList=[]
        while j<len(moviesInfo): 
            if Years[index]==moviesInfo[j]["year"]:
                commonyearList.append(moviesInfo[j])
            j=j+1
        dic[Years[index]]=commonyearList
        index=index+1
    return(dic)
group_Of_Movies=(group_by_year(sortedYears))
pprint(group_Of_Movies)