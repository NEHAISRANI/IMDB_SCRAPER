from imdbTask1 import *
from pprint import pprint
import json

def analyse_actors (): 
	castallData=[]
	for i in moviesInfo[:3]:
		movieUrls=(i["url"])
		urlSplit=(movieUrls.split("/"))
		Urlofmovie=urlSplit[5]
		# print(Urlofmovie)
		with open("movieDetails/"+str(Urlofmovie)+"_alldata.json","r") as read_file:
			readData=json.load(read_file)
			data=readData["cast"]
			castallData.append(data)
	return(castallData)
nameAndId=analyse_actors()
print(nameAndId)

actorsId=[]
actorsName=[] 
for i in nameAndId:
	for j in i:
		if j["imdb_id"] not in actorsId:
			if j["name"] not in actorsName:
				actorsId.append(j["imdb_id"])
				actorsName.append(j["name"])
print(actorsId,actorsName)

for actors in actorsId:
	actorsNamedic={}
	moviesId={}
	for j in nameAndId:
		for k in j:
			if k["imdb_id"]==actors:
				if k["name"] != actorsNamedic.get("name"):
					actorsNamedic["name"]=k["name"]
					actorsNamedic["num_movies"]=1
				else:
					actorsNamedic["num_movies"] = actorsNamedic["num_movies"] + 1
		moviesId[actors]=actorsNamedic 
	print(moviesId)
