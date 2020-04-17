from imdbTask4 import*
from imdbTask1 import*
import os 
import json 
def moviesCaching():
	getDetails=[]
	for i in moviesInfo:
		link=i["url"]
		movieUrl=link.split("/")
		fileName=("caching/"+str(movieUrl[5])+".json")
		if os.path.exists(fileName):
			print("-------------------------------")
			file=open(fileName,"r")
			readFile=file.read()
			getDetails.append(readFile)
			file.close() 
		else:
			functionCall=Scrap_Movie_Details(link)
			# print(functionCall)
			with open("caching/"+str(movieUrl[5])+".json","w")as file:
				write=json.dump(functionCall,file)
	return(getDetails)
pprint(moviesCaching())





    