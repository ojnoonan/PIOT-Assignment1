from sense_hat import SenseHat
import electronicDie

sense = SenseHat()
sense.clear()

# Player Scores
p1_score = 0
p2_score = 0

# Current player turn
player_turn = 1

while p1_score < 30 and p2_score < 30:
    sense.show_message("Player " + player_turn + " Roll  ")
    if player_turn == 1:
        player_turn + 1
        
    else:
        player_turn - 1
        