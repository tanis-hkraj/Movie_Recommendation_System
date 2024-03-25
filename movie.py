import pandas as pd
import numpy as np
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
movies_data=pd.read_csv('movies.csv')
selected_features=['genres','keywords','tagline','cast','director','title']
for i in selected_features:
    movies_data[i].fillna('',inplace=True)
combined_features=movies_data['genres']
for i in selected_features:
    if i=='genre':
        continue
    combined_features+=' '+movies_data[i]
vectorizer=TfidfVectorizer()
feature_vectors=vectorizer.fit_transform(combined_features)
similarity=cosine_similarity(feature_vectors)
movie_name=input("Enter your favourite movie name : ")
list_titles=movies_data['title'].tolist()
find_close_match=difflib.get_close_matches(movie_name,list_titles)
close_match=find_close_match[0]
index_of_movie=movies_data[movies_data.title==close_match]['index'].values[0]
simarlirity_score=list(enumerate(similarity[index_of_movie]))
sorted_similar_movies=sorted(simarlirity_score,key=lambda x:x[1],reverse=True)
print("Movies Suggested: \n")
i=1
for movie in sorted_similar_movies:
    index=movie[0]
    title_from_index=movies_data[movies_data.index==index]['title'].values[0]
    if(i<15):
        print(i,'.',title_from_index)
        i+=1