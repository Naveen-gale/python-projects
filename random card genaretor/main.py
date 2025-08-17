import random

card = ["spead" , "club" , "Diamond" , "heart"]
 

rank = [1,2,3,4,5,6,7,8,9,10,"jack" ,"queen", "king", "ace"] 


def rande_cards():
    rand_card =  random.choice(card)
    random_ranks = random.choice(rank)


    print(f"the [{rand_card}] of [{random_ranks }]")



rande_cards()