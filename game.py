from sense_hat import SenseHat
from electronicDie import emoJ
import csv, time

sense = SenseHat()
sense.clear()

# Player Scores
p1_score = 0
p2_score = 0

f = open('winner.csv', 'w') # Open file

# Current player turn
player_turn = 1

class diceGame:

    def save_winner(self, score):
        with f:
            writer = csv.writer(f)

            t = time.localtime() # Get current time
            current_time = time.strftime("%H:%M:%S", t) # Format time

            writer.writerow(current_time + " " + str(score))


    def check_player_score(self, score):
        print(score)
        if score >= 30:
            sense.show_message("Player " + str(player_turn) + " Wins  ")
            dg.save_winner(score)
        else:
            pass

    while p1_score < 30 and p2_score < 30:
        die = emoJ(True)
        roll = 0 # Reset roll each time
        if player_turn == 1:
            sense.show_message("Player " + str(player_turn), scroll_speed=0.05)
            roll = die.check_for_movement()
            p1_score += roll
            dg.check_player_score(p1_score)
            player_turn += 1

        else:
            sense.show_message("Player " + str(player_turn), scroll_speed=0.05)
            roll = die.check_for_movement()
            p2_score += roll
            dg.check_player_score(p2_score)
            player_turn -= 1
dg = diceGame()


