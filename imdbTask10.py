from imdbTask7 import*
from imdbTask5 import*
def extract_language_and_directors(movies_list):
	directorsList=[]
	for i  in movies_list:
		if i not in directorsList:
			directorsList.append(i)
	return(directorsList)
	
directors=extract_language_and_directors(allDirectorsName)
# pprint(directors) 


def analyse_language_and_directors (movie_Directors):
    dic={}  
    for i in movie_Directors:
        languageList=[]
        dic1={}
        for j in movie_details:
            if i in j["Directors"]:
                languageList.extend(j["language"])
            # print(new1)
        for lang in languageList: 
            if lang not in dic1:
                dic1[lang]=1
            else:
                dic1[lang]+=1
        dic[i]=dic1
    return(dic)
print(analyse_language_and_directors(directors))





