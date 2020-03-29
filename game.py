from sense_hat import SenseHat
import electronicDie as ed

sense = SenseHat()
sense.clear()

# Player Scores
p1_score = 0
p2_score = 0

# Current player turn
player_turn = 1

while p1_score < 30 and p2_score < 30:
    roll = 0 # Reset roll each time
    sense.show_message("Player " + player_turn + " Roll  ")
    if player_turn == 1:
        roll = ed.roll_dice
        p1_score + roll
        check_player_score(p1_score)
        player_turn + 1

    else:
        roll = ed.roll_dice
        p2_score + roll
        check_player_score(p2_score)
        player_turn - 1

def check_player_score(score):
    if score == 30:
        sense.show_message("Player " + player_turn + " Wins  ")
    else:
        pass
        