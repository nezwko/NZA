import random

popularity = 0
items = []
game_file = 'tyrone.txt'

def save_game(popularity, items):
    with open(game_file, "a") as file:
        file.write(f"{popularity}\n")
        file.write(f"{items}\n")
        
def load_game(popularity, items):
    while True:
        try: 
            with open(game_file,"r") as file:
                content = file.read()
                print(content)
            return popularity, items
        except FileNotFoundError:
            print("No saved file found.")
            return 0,[]
    
def delete_savefile(popularity, items):
    with open(game_file, "w") as file:
        file.write(" ")

def fashion_runway():
    return random.choice(["Oh no, You fell down!","Applause!! Nice Runway."])

def play_game():
    global popularity, items
    popularity, items = load_game(popularity, items)
    print('Welcome to Fashion Runway!')

    while True:
        try:
            print(f"Popularity: {popularity}, Items: {items}")
            print('Choose an action!')
            print('[1] Start Runway')  
            print('[2] Gain Popularity')
            print('[3] Save Game')
            print('[4] Quit Game')
            print('[5] Delete Saved File')
            user = input("Enter Your Choice: ")
    
            if user == "1":
                result = fashion_runway()
                if result == "Applause!! Nice Runway.":
                    item = random.choice(["Trophy", "Medal", "Crown"])
                    items.append(item)
                    print(f"You Acquired a {item}!")
                else:
                    damage = random.randint(10,20)
                    popularity -= damage
                    print(f"You fell! You lost {damage} popularity")

            elif user == "2":
                gain = 20
                popularity += gain
                print(f"You have gained {gain} popularity!")
        
            elif user == "3":
                save_game(popularity, items)
                print("File Saved")
        
            elif user == "4":
                save_game(popularity, items)
                print("Quitting")
                break

            elif user == "5":
                delete_savefile(popularity,items)
                print("Save File Deleted.")
        
            else:
                print("Please enter a Valid Number.")
        
        except Exception as e:
            print(f"An error occured: {e}. Please enter a valid choice.")
play_game()



