from DataStructure import CoStarSearch 
        

if __name__ == "__main__":

    while True:
        actor_name = input("Enter the name of an actor or actress (or type 'exit' to quit): ")
        
        if actor_name.lower() == 'exit':
            print("Exiting...")
            break
        
        print("Searching...")
        co_star_search = CoStarSearch(actor_name)
        co_star_search.printResults()


    # THIS WAS USED FOR TESTING PURPOSES:

    # zendaya = CoStarSearch("Zendaya")
    # print(zendaya.adjList)
    # print(zendaya.top3)
    # zendaya.printResults()

    # katharine = CoStarSearch("Katharine Hepburn")
    # print(katharine.adjList)
    # print("\n")
    # print(katharine.top3)
    # print("\n")
    # katharine.printResults()

    # emma = CoStarSearch("Emma Stone")
    # print(emma.adjList)
    # print("\n")
    # print(emma.top3)
    # print("\n")
    # emma.printResults()

    # hanks = CoStarSearch("tom hanks")
    # print(hanks.adjList)
    # print("\n")
    # print(hanks.top3)
    # print("\n")
    # hanks.printResults()

    # adamscott = CoStarSearch("adam scott")
    # print(adamscott.adjList)
    # print("\n")
    # print(adamscott.top3)
    # print("\n")
    # adamscott.printResults()