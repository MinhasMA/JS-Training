
#pick player and validate input

#player 1 and player 2 - toggle between the two - one at a time

players = ['player1', 'player2']


def correct_your_choice():
    draw = input("please pick who will start the show:") 
    while draw not in players:
        draw = input("please pick who will start the show:") 

def first_draw():
        drawer = input("please pick who will start the show:")
        if drawer not in players:
            print("Invalid choice.Draw again")
            correct_your_choice()
        else:
            print(drawer + " to start")
# choose who will start - then build a sequence


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
