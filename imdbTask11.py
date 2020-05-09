from imdbTask5 import* 

def extract_movies_genre(movies_Genrelist):
	genreList=[]
	for i in movies_Genrelist:
		genreList.extend(i["genre"])
	return(genreList)
genre=(extract_movies_genre(movie_details))
# print(genre)

def analyse_movies_genre(moviesGenre):
	genreDic={}
	for i in moviesGenre: 
		if i not in genreDic:
			genreDic[i]=1
		else:
			genreDic[i]+=1
	return(genreDic)
print(analyse_movies_genre(genre))