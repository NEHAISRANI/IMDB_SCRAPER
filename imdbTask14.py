from imdbTask1 import*
import json

def analyseLeadAndCo_actorName():
    allMoviesData=[]
    for i in moviesInfo[:10]:
        movieUrls=(i["url"])   
        urlSplit=(movieUrls.split("/"))
        Urlofmovie=urlSplit[5]
        with open("movieDetails/"+str(Urlofmovie)+"_alldata.json","r") as read_file:
            readData=json.load(read_file)
            allMoviesData.append(readData)
    return(allMoviesData) 
actorsCast=analyseLeadAndCo_actorName()

castList=[]
def duplicate_lead_actors():
    for i in actorsCast:
        a=(i["cast"][:5])
        castList.append(a)
    return castList
leadActorid=duplicate_lead_actors()



def lead_actors(movie_list):
    leadActorName=[]
    for i in movie_list:
        movieOfCastLeadActors=i["cast"][0]["name"]
        leadActorName.append(movieOfCastLeadActors)
    return(leadActorName)
leadActorName=lead_actors(actorsCast)

def duplicate_lead_actors(movie_list):
    duplicateLead=[]
    for i in range(len(movie_list)):
        if leadActorName[i] not in duplicateLead:
            duplicateLead.append(leadActorName[i])
    return(duplicateLead)
duplicate_Lead=duplicate_lead_actors(leadActorName)

def analyse_co_actors(movie_list):
    new_list=[]
    for index in range(len(duplicate_Lead)):
        new=[]
        for index1 in movie_list:
            if duplicate_Lead[index] in index1[0]["name"]:
                new.append(index1)
        new_list.append(new)
    for i in range(len(duplicate_Lead)):
        dictionary={}
        for nestedList in new_list:
            dic={}
            lead_actor_id=nestedList[0][0]["imdb_id"]
            lead_actor_name=nestedList[0][0]["name"]
            coActorName=[] 
            co_Actor_list=[]
            for list1 in nestedList:
                for dict1 in list1[:1]: 
                    coActorName.append(dict1["name"])
                    if dict1 not in co_Actor_list:
                        co_Actor_list.append(dict1)
            duplicateCoActor=[]
            for index in coActorName:
                if index not in duplicateCoActor:
                    duplicateCoActor.append(index)
            # print(duplicateCoActor)
                    
            frequent_co_actor=[]
            for i in range(len(duplicateCoActor)):
                count=0
                for j in coActorName:
                    if duplicateCoActor[i]==j:
                        count=count+1
                if count>1:
                    for counter in co_Actor_list:
                        if counter["name"]==duplicateCoActor[i]:
                            counter["no_movie"]=count
                            frequent_co_actor.append(counter)
            print(frequent_co_actor)
            if frequent_co_actor!=[]:
                dic["name"]=lead_actor_name
                dic["frequent_co_actor"]=frequent_co_actor
                dictionary[lead_actor_id]=dic
        return(dictionary)
print(analyse_co_actors(leadActorid))
