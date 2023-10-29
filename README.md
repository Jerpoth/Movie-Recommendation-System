# Movie-Recommendation-System
this is a movie recommendation system that helps users discover movies similar to their favorites by analyzing textual features and calculating their similarity. The code and dataset can be shared on GitHub for others to use and explore.
Data Preparation: The project starts by loading a dataset of movies, which includes information like genres, keywords, cast, and more. It also handles missing data by filling in empty values.

Feature Extraction: It selects specific features such as genres, keywords, taglines, cast, and director to create a combined feature for each movie by concatenating these attributes. Then, it converts this text data into feature vectors using the TF-IDF vectorization technique.

Similarity Calculation: Cosine similarity is calculated between the feature vectors of all movies. This similarity score is used to find movies that are similar to a user's input.

User Input: The user is prompted to enter the name of their favorite movie (e.g., "Iron Man" or "Gravity").

Close Match: The project uses the difflib library to find a close match for the user's input within the list of movie titles.

Recommendation: Once the close match is found, the project retrieves the index of the selected movie and sorts the movies in the dataset based on their similarity to the selected movie.

Output: The system then provides a list of recommended movies that are similar to the user's input movie.
