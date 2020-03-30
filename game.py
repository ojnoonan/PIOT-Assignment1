from sense_hat import SenseHat
from electronicDie import check_for_movement
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

        writer.writerow(current_time + " " + str(score))


def check_player_score(score):
    print(score)
    if score >= 10:
        sense.show_message("Player " + str(player_turn) + " Wins  ")
        save_winner(score)
    else:
        pass

while p1_score < 10 and p2_score < 10:
    roll = 0 # Reset roll each time
    if player_turn == 1:
        sense.show_message("Player " + str(player_turn))
        roll = check_for_movement(True)
        p1_score += roll
        check_player_score(p1_score)
        player_turn += 1

    else:
        sense.show_message("Player " + str(player_turn))
        roll = check_for_movement(True)
        p2_score += roll
        check_player_score(p2_score)
        player_turn -= 1
