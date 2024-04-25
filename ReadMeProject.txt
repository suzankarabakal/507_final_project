The code has just one interaction with the end user. The prompt given to the user will be to input the name of an actor. The user can stop running the program by typing "exit" instead of an actor's name.

In response to the inputted actor's name, the program will output text listing the inputted actor's top 3 most common costars, the name of the movies they were in together, and which of the three actors had the most successful collaborations with the inputted actor based on revenue and ratings.

The program uses the TMDB api, which requires a key. However, the user does not need to input the key, I have included my API key in the code to make the API calls.

The code requires the Python packages requests and json for it to work.

The graph of the data is organized as a dictionary. Nodes in the network represent actors or actresses. Edges represent whether there is a connection between the inputted actor and the node.