from imdbTask5 import *
from pprint import pprint

def exportLanguages(Languages):
    languageList=[] 
    for i in Languages:
        lang=(i["language"])
        languageList.extend(lang)
    return(languageList)
allLanguages=(exportLanguages(movie_details))
# pprint(allLanguages)

def sortedLanguage(sortlanguage):
    sortedLanguagelist=[]
    for i in sortlanguage:
        if i not in sortedLanguagelist:
            sortedLanguagelist.append(i)
    return(sortedLanguagelist)
sort=(sortedLanguage(allLanguages))

def analyse_movies_language(sorted):
    i=0
    countLanguages={}
    while i<len(sorted):
        j=0
        count=0 
        while j<len(allLanguages):
            if sorted[i]==allLanguages[j]:
                count=count+1
            j=j+1
        countLanguages[sorted[i]]=(count)
        i=i+1
    return(countLanguages)
# pprint(analyse_movies_language(sort))

    
    