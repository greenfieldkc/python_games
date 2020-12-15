import random
import timeit

class SnakesLadders():
    snakes = {16:6, 46:25, 49:11, 62:19, 64:60, 74:53, 89:68, 92:88, 95:75, 99:80} #key = beginning square, val = ending square
    ladders = {2:38, 7:14, 8:31, 15:26, 21:42, 28:84, 36:44, 54:67, 71:91, 78:98, 87:94}


    def __init__(self):
        self.players = {1:0, 2:0}  #takes player number as key and board position as value
        self.turn_count = 0
        self.winner = None

    def play(self, die1, die2):
        if self.players[1] == 100 or self.players[2] == 100 : return "Game over!"
        if self.turn_count % 2 == 0:
            player = 1
        else:
            player = 2
        #print("Player {p} rolled {d1}, {d2}".format(p=player, d1=die1, d2=die2))
        self.players[player] += die1 + die2
        if self.players[player] == 100:
            self.winner = "Player " + str(player)
            return "Player " + str(player) + " Wins!"
        elif self.players[player] > 100:
            #print("Passed 100. Moving Backwards...")
            self.players[player] = 100 - (self.players[player] - 100)
        if self.players[player] in self.snakes:
            #print("Player {p} is sliding down a snake!".format(p=player))
            self.players[player] = self.snakes[self.players[player]]
        elif self.players[player] in self.ladders:
            #print("Player {p} is climbing a ladder!".format(p=player))
            self.players[player] = self.ladders[self.players[player]]
        if die1 == die2:
            #print("Rolled a double! Play again!")
            self.play(random.randint(1,6), random.randint(1,6))
        else:
            self.turn_count += 1
        return "Player {p} is on square {x}".format(p=player, x=self.players[player])

def run_game():
    game = SnakesLadders()
    while game.winner == None:
        game.play(random.randint(1,6), random.randint(1,6))
    win_count[game.winner] += 1


start_time = timeit.default_timer()
win_count = {"Player 1":0, "Player 2":0}
num_tests = 100000
for i in range(num_tests):
    run_game()

stop_time = timeit.default_timer()
print("Time: ", stop_time - start_time, "seconds.")
print(win_count)
print("Player 1 won ", win_count["Player 1"]/num_tests * 100, "% of time")

print("Player 2 won ", win_count["Player 2"]/num_tests * 100, "% of time")
