The code has just one interaction with the end user. The prompt given to the user will be to input the name of an actor. The user can stop running the program by typing "exit" instead of an actor's name. The prompt: "Enter the name of an actor or actress (or type 'exit' to quit): "

In response to the inputted actor's name, the program will output text listing the inputted actor's top 3 most common costars, the name of the movies they were in together, and which of the three actors had the most successful collaborations with the inputted actor based on revenue and ratings. If the input given by the user is not an actors name (such as nonsense letters/numbers or a name with a typo), it will tell the user "Actor not found. Please try again." The original prompt asking the user to input the name of an actor will be the next line.

The program uses the TMDB api, which requires a key. However, the user does not need to input the key, I have included my API key in the code to make the API calls.

The code requires the Python packages requests and json for it to work.

The graph of the data is organized as a dictionary. Nodes in the network represent actors or actresses. Edges represent whether there is a connection between the inputted actor and the node.

The dictionary contains each node that represents an actor. Each node is structured with the actor's name as the dictionary item's key. The value of each dictionary item is a list of movies, with each movie being represented as a list containing the movie's title, TMDB ID, rating, and revenue. For example:
inputtedActor.adjList = {costar1: [[movie1 title, movie1 ID, movie1 rating, movie1 revenue], [movie2 title, movie2 ID, movie2 rating, movie2 revenue]], costar2: [[movie1 title, movie1 ID, movie1 rating, movie1 revenue]]}
