from sense_hat import SenseHat
from electronicDie import roll_dice
import csv, time

sense = SenseHat()
sense.clear()

# Player Scores
p1_score = 0
p2_score = 0

f = open('winner.csv', 'w') # Open file

# Current player turn
player_turn = 1

def save_winner(score):
    with f:
        writer = csv.writer(f)

        t = time.localtime() # Get current time
        current_time = time.strftime("%H:%M:%S", t) # Format time

        writer.writerow(score + current_time)


def check_player_score(score):
    if score == 30:
        sense.show_message("Player " + player_turn + " Wins  ")
    else:
        pass

while p1_score < 30 and p2_score < 30:
    roll = 0 # Reset roll each time
    sense.show_message("Player " + str(player_turn) + " Roll  ")
    if player_turn == 1:
        roll = roll_dice()
        p1_score + roll
        check_player_score(p1_score)
        player_turn + 1

    else:
        roll = roll_dice()
        p2_score + roll
        check_player_score(p2_score)
        player_turn - 1
        