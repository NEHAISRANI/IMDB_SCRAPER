from imdbTask1 import*
from imdbTask2 import*
def group_by_decade(decade):
    movie_years=[]
    deacdeMovieDeatils={}
    for i in decade:
        modules=i%10 
        difference=i-modules
        rangeyear=(difference+10)-1
        if rangeyear not in movie_years:
            movie_years.append(rangeyear)
            decadeYear=[] 
            for j in moviesInfo:
                if difference<=j["year"] and rangeyear>=j["year"]:
                    decadeYear.append(j)
            deacdeMovieDeatils[difference]=decadeYear
    return(deacdeMovieDeatils)
pprint(group_by_decade(group_Of_Movies))




