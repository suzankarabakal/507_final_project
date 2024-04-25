import requests
import json

class CoStarSearch:
    '''A class to search for the most common co-stars of a given actor or actress.

    Parameters
    ----------
    actor : str
        The name of the actor or actress to search for

    Attributes
    ----------
    adjList : dict
        A dictionary containing the adjacency list of the graph of actors and movies, list of tuples
    
    actor : str
        The name of the actor or actress we are using

    actorID : str
        The TMDB id of the actor or actress we are using

    Methods
    ----
    fetchActorID(self, actor)
        Fetches the actor's id from the database

    fetchAdjList(self)
        Creates the adjacency list of the graph of actors and movies

    top3CoStars(self)
        Returns the top 3 most common co-stars of the actor or actress and the movies they were in together

    avgMovieRating(self)
        Calculates the average rating of a all the movies the actor or actress has been in with our actor

    printResults(self)
        Prints the results of the top 3 most common co-stars of the actor or actress and the movies they were in together, formatted nicely.

    '''
    def __init__(self, actor):
        self.actor = actor.capitalize()
        self.actorID = self.fetchActorID()
        self.adjList = self.fetchAdjList()
        self.top3 = self.top3CoStars()

    def fetchActorID(self):
        '''Fetches the actor's id from the TMDB api, which will be used to do more api calls later on.


        Returns
        -------
        str
            The actor's id
        '''
        url = "https://api.themoviedb.org/3"
        myKey =  "e1d886e0eb8db0db7a80c38dc06fe278"

        response = requests.get(f"{url}/search/person?api_key={myKey}&query={self.actor}")
        responseJSON = json.loads(response.text)

        popularity = 0

        if responseJSON['total_results'] == 0:
            print("Actor not found. Please try again.")
            return None
        else:
            for person in responseJSON['results']:
                if person['popularity'] > popularity:
                    self.actorID = person['id']
                    popularity = person['popularity']
                    
            #self.actorID = responseJSON['results'][0]['id']
        return self.actorID
    
    def fetchAdjList(self):
        '''Creates the adjacency list of every actor that the inputted actor has worked with on a feature film, giving their name and the movie they were in together.

        Returns
        -------
        dict
            The adjacency list of the graph of actors and movies. It is a dictionary where the key is the name of the actor and the value is a list of movies they were in together.
        '''
        self.adjList = {}

        url = "https://api.themoviedb.org/3"
        myKey =  "e1d886e0eb8db0db7a80c38dc06fe278"

        response = requests.get(f"{url}/person/{self.actorID}/movie_credits?api_key={myKey}")
        responseJSON = json.loads(response.text)

        for movie in responseJSON['cast']: # going through every movie the actor has been in
            # print(movie['title'])
            # # print(movie)
            movieID = movie['id']
            # print(movieID)

            # call general movie info here to sort out movies under 40 mins, TV movies, unreleased movies, and documentaries that this actor has been in
            movieInfo = requests.get(f"{url}/movie/{movieID}?api_key={myKey}")
            movieInfoJSON = json.loads(movieInfo.text)
            included = False
            if movieInfoJSON['status'] == "Released" and movieInfoJSON['runtime'] > 40:
                included = True
                movieRating = movieInfoJSON['vote_average']
                movieRevenue = movieInfoJSON['revenue']
            for genre in movieInfoJSON['genres']:
                if genre['name'] == "Documentary" or genre['name'] == "TV Movie":
                    included = False
                    break

                
            if included:
                # print(movie['title'] + "\n")
                # print(movieID)

                cast = requests.get(f"{url}/movie/{movieID}/credits?api_key={myKey}")
                castJSON = json.loads(cast.text)

                for actor in castJSON['cast']:
                    if actor['id'] != self.actorID and actor['name'] not in self.adjList:
                        self.adjList[actor['name']] = []
                        self.adjList[actor['name']].append([movie['title'], movieID, movieRating, movieRevenue]) 
                        # saves all the relevant info that will be used later for each costar: movie title, movie ID, movie rating, movie revenue

                    elif actor['id'] != self.actorID and actor['name'] in self.adjList:
                        self.adjList[actor['name']].append([movie['title'], movieID, movieRating, movieRevenue])

        return self.adjList
    
    def top3CoStars(self):
        '''Returns the top 3 most common co-stars of the actor or actress and the movies they were in together.

        Returns
        -------
        list
            A list of tuples containing the name of the actor and the movies they were in together. The list is sorted by the number of movies they were in together.
        '''
        # .items returns a list of tuples with the key and value of each item in the dictionary, so the sorted method can sort by the length of the value which is a list of movies
        top3 = sorted(self.adjList.items(), key=lambda x: len(x[1]), reverse=True) 
        return top3[:3]
    
    def avgMovieRating(self, top3):
        '''Calculates the average rating of all the movies the actor or actress has been in with our actor and selects the highest one.

        Returns
        -------
        tuple
            The actor's name and the average revenue of the movie with the highest average revenue
        '''
        ratingList = []
        for coStar in top3:
            totalRating = 0
            for movie in coStar[1]:
                totalRating += movie[2]
            avgRating = totalRating / len(coStar[1])
            avgRating = round(avgRating, 1)
            ratingList.append((coStar[0], avgRating))
        
        ratingList = sorted(ratingList, key=lambda x: x[1], reverse=True)
        return ratingList[0]
            
    def avgMovieRevenue(self, top3):
        '''Calculates the average revenue of all the movies the actor or actress has been in with our actor and selects the highest one.

        Returns
        -------
        tuple
            The actor's name and the average revenue of the movie with the highest average revenue
        '''
        revList = []
        for coStar in top3:
            totalRev = 0
            numMovies = 0
            for movie in coStar[1]:
                if movie[3] != 0:
                    totalRev += movie[3]
                    numMovies += 1
            if numMovies == 0:
                avgRev = 0
            else:
                avgRev = totalRev / numMovies
                avgRev = round(avgRev)
            revList.append((coStar[0], avgRev))
        
        revList = sorted(revList, key=lambda x: x[1], reverse=True)
        return revList[0]

    def printResults(self):
        '''Prints the results of the top 3 most common co-stars of the actor or actress and the movies they were in together, formatted nicely.'''
        top3 = self.top3CoStars()
        print(f"The top 3 most common co-stars of {self.actor} are:")
        print("\n")
        for i in range(3):
            print(f"{top3[i][0]} was in {len(top3[i][1])} movies with {self.actor}:")
            for movie in top3[i][1]:
                print(f"\t{movie[0]}")
            print("\n")

        print(f"{self.actor}'s collaborations with {self.avgMovieRating(top3)[0]} are the most critically acclaimed, with an average of {self.avgMovieRating(top3)[1]}/10 according to TMDB.")
        print("\n")
        print(f"{self.actor}'s collaborations with {self.avgMovieRevenue(top3)[0]} were the most profitable, making an average of ${self.avgMovieRevenue(top3)[1]} per movie.")
        print("\n")

if __name__ == "__main__":
    pass