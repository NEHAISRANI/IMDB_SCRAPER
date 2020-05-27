import time
import random
from pprint import pprint
from imdbTask1 import*
from imdbTask4 import* 
import os 
import json 
def moviesCaching():
    getDetails=[]
    for i in moviesInfo:
        link=i["url"]
        movieUrl=link.split("/")
        fileName1=("cach/"+str(movieUrl[5])+".json")
        if os.path.exists(fileName1):
            # print("-------------------------------")
            file=open(fileName1,"r")
            readFile=file.read()
            getDetails.append(readFile)
            file.close()  
        else:
            functionCall=Scrap_Movie_Details(link) 
            with open("cach/"+str(movieUrl[5])+".json","w") as file:
                write=json.dump(functionCall,file)
                timeLimit=random.randint(1,3)
                time.sleep(timeLimit)
    return(getDetails)
movieDetailsWithCaching=moviesCaching() 
pprint(movieDetailsWithCaching)
# print(len(movieDetailsWithCaching))

