from imdbTask1 import *
from imdbTask4 import *
def get_movie_list_details(api):
    allMoviedata=[]
    for i in api[:20]:
        link=i["url"]
        extractMovieDetails=Scrap_Movie_Details(link)
        copyMoviedata=extractMovieDetails.copy()
        # moviesData.clear()
        allMoviedata.append(copyMoviedata)
    return(allMoviedata) 
movie_details=(get_movie_list_details(moviesInfo))
# pprint(movie_details) 





