
#pick player and validate input

#player 1 and player 2 - toggle between the two - one at a time

players = ['player 1', 'player 2']

choices = ['X', 'O']

def correct_your_choice():
    draw = input("please pick who will start the show:") 
    while draw not in players:
        draw = input("Wrong choice. please pick who will start the show:")
    print(draw + " to start")

def first_draw():
        drawer = input("please pick who will start the show:")
        if drawer not in players:
            print("Invalid choice.Draw again")
            correct_your_choice()
            
        else:
            print(drawer + " to start")
            
        choice = input("make your choice please:")
        while choice not in choices:
            print("This is an invalid choice. Please pick either X or O")
        print(drawer + " has picked " + choice)
            
def draw_board():
    row1 = ["-","-","-"]
    row2 = ["-","-","-"]
    row3 = ["-","-","-"]
    
    print(row1)
    print(row2)
    print(row3)


def draw_board2():
    row1 = ["-","-","-"]
    row2 = ["-","-","-"]
    row3 = ["-","-","-"]
    
    print(row1) + "r"
    print(row2) + "s"
    print(row3) + "t"

def pick_choice():
    choice = input
#draw board 

def draw_board():
    row1 = ["-","-","-"]
    row2 = ["-","-","-"]
    row3 = ["-","-","-"]
    
    print(row1)
    print(row2)
    print(row3)




# until either board is full or the sequence is made - ask for input and draw board
#  validate input
#  place on board
#  check board 
