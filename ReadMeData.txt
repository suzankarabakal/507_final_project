# Data Source: The Movie Database (TMDB)

URL for Data: https://api.themoviedb.org/3
URL for Documentation: https://developer.themoviedb.org/reference/intro/getting-started

I will note that the TMDB documentation is not very good. I mostly figured out how to use it by Googling things and reading the forums.

## Format(s): 
Data is retrieved in JSON format.

## Description of accessing the data:

The data from TMDB is accessed using HTTP requests made to their API endpoints. The endpoints that I used were: 
/search/person
/person/{actorID}/movie_credits
/movie/{movieID}
/movie/{movieID}/credits

Each of these endpoints also need the api key parameter added to it with api_key={api_key} stuck on the end. 

/search/person also needs the additional parameter of the person's name you are searching as a string with query={name} stuck on the end after the api key.

The Python requests library is used to send requests and retrieve data. I didn't cache the data.

## Summary of Data:

From /search/person: Shows a dictionary of the people with that name on TMDB. The number of results depends on the search. Each result's dictionary has 9 variables.

From /person/{actorID}/movie_credits: Shows a dictionary of their credits as either cast or crew. The number of results depends on the person. Each result's dictionary has 17 variables.

From /movie/{movieID}: Shows a dictionary of information about the movie. Each movie's dictionary has 26 variables.

From /movie/{movieID}/credits: Shows a dictionary of the cast and crew on the movie. The number of results depends on the movie. Each cast member's dictionary has 12 variables.
