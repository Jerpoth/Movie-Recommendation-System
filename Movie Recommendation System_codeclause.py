#!/usr/bin/env python
# coding: utf-8

# Importing the Dependendencies
# 

# In[12]:


import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity


# In[13]:


movies_data=pd.read_csv('D:\\DBMS\\notes\\ML\\movies.csv')


# In[14]:


movies_data.head()


# In[15]:


movies_data.shape


# In[17]:


movies_data.isnull().sum()


# In[19]:


for i in movies_data:
    movies_data[i]=movies_data[i].fillna('')


# In[20]:


movies_data.isnull().sum()


# In[22]:


# Selecting the recommendation feature

selected_feature=['genres','keywords','tagline','cast','director']
print(selected_feature)


# In[23]:


# combining the selected feature

combined_feature=movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']
print(combined_feature)


# In[25]:


# converting the text data to feature vector

vectorizer=TfidfVectorizer()
feature_vectors=vectorizer.fit_transform(combined_feature)
print(feature_vectors)


# In[26]:


# Getting the Similarity Scores

similarity=cosine_similarity(feature_vectors)
print(similarity)


# In[27]:


print(similarity.shape)


# In[28]:


# Getting the movie name from the user

movie_name=input('Enter your favourite movie name :')


# In[29]:


# creating the list

list_of_all_titles=movies_data['title'].tolist()
print(list_of_all_titles)


# In[31]:


# finding the close match

find_close_match=difflib.get_close_matches(movie_name,list_of_all_titles)
print(find_close_match)


# In[32]:


close_match=find_close_match[0]
print(close_match)


# In[34]:


# finding the index of the movie with title

index_of_the_movie=movies_data[movies_data.title==close_match]['index'].values[0]
print(index_of_the_movie)


# In[35]:


# Getting the list of similar movies

similarity_score=list(enumerate(similarity[index_of_the_movie]))
print(similarity_score)


# In[36]:


# sorting the movie based on their similarity score

sorted_similar_movies=sorted(similarity_score,key=lambda x:x[1],reverse=True)
print(sorted_similar_movies)


# In[42]:


# print the name of similar movie based on index

print('Movies suggested for you : \n')
i = 1
for movie in sorted_similar_movies:
    index=movie[0]
    title_from_index=movies_data[movies_data.index==index]['title'].values[0]
    if(i<30):
            print(i,'.', title_from_index)
            i+=1


# # Movie RecommendationSystem
# 

# In[43]:


movie_name=input('Enter your favourite movie name :')

list_of_all_titles=movies_data['title'].tolist()

find_close_match=difflib.get_close_matches(movie_name,list_of_all_titles)

close_match=find_close_match[0]

index_of_the_movie=movies_data[movies_data.title==close_match]['index'].values[0]

similarity_score=list(enumerate(similarity[index_of_the_movie]))

sorted_similar_movies=sorted(similarity_score,key=lambda x:x[1],reverse=True)

print('Movies suggested for you : \n')
i = 1
for movie in sorted_similar_movies:
    index=movie[0]
    title_from_index=movies_data[movies_data.index==index]['title'].values[0]
    if(i<30):
            print(i,'.', title_from_index)
            i+=1


# In[ ]:




