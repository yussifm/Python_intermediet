
# Linear Search 
# Q: find a number(query) from the turn down cards

# cards
list_cares = [12,8,11,13,5,6,7,8,9,1,3,2,4]


# finde cards founc
def find_card(card: list, query: int):
    position = 0
    while True:
        if(card[position] == query):
            print("card found at index", card.index(position))
            return False
        elif(position == len(card)-1):
            print("Query {} can't be found in any index of cards".format(query))
            return False
       
        position +=1


if __name__ == "__main__":
    find_card(list_cares, 20)

