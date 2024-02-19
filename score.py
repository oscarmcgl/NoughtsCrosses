import json

def check_wins(Name): 
    try:
        with open('wins.json', 'r') as f: 
                                        
            data = json.load(f)
            wins = data[str(Name)]
            print(wins) 
    except:
        print(f"{Name} does not exist.")



        


# check_wins("oscar")    

# def new(Name):
#     try:
         
#         with open('wins.json', 'r') as f:
#                 data = json.load(f)
#                 ac = data[str(Name)]

#         print("Already exists in database!")
#     except:
#         with open('wins.json', 'w') as f:
#              json.dump(data+dict(Name),f)


#new("lara")