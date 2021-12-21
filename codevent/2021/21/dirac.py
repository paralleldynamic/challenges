from collections import Counter
from copy import deepcopy
from functools import cache
from itertools import cycle

class Player():
    def __init__(self, name, starting_position, score=0):
        self.name = name
        self.score = score
        self.board = cycle(range(1, 11))
        self.starting_position = starting_position
        for _ in range(starting_position):
            self.position = next(self.board)

    def roll_and_move(self, die, rolls):
        for _ in range(rolls):
            roll = die.roll()
            for r in range(roll):
                self.position = next(self.board)
        self.score += self.position
        return self.score

    def reset(self):
        self.score = 0
        self.board = cycle(range(1, 11))
        for _ in range(self.starting_position):
            self.position = next(self.board)
        return self

    def __repr__(self):
        return f"Player<({self.name}, score: {self.score}, position: {self.position})>"

class Die():
    def __init__(self, sides, deterministic):
        if deterministic:
            self._die = cycle(range(1, sides + 1))
        self.rolls = 0
        self.showing = 1
        self.sides = sides
        self.deterministic = deterministic

    def roll(self):
        self.rolls += 1
        roll = next(self._die)
        self.showing = roll
        return roll

    def reset(self):
        if self.deterministic:
            self._die = cycle(range(1, self.sides + 1))
            self.showing = 1
        self.rolls = 0
        return self

    def __repr__(self):
        return f"Die<(Sides: {self.sides}, showing: {self.showing}"

class Dirac():
    def __init__(self, players, score_threshold=1000, sides=100, deterministic=True):
        self.players = players
        self.score_threshold = score_threshold
        self.high_score = 0
        self.in_the_lead = None
        self.turns = 0
        self.die = Die(sides, deterministic)

    def turn(self, player, rolls=3):
        self.turns += 1
        score = player.roll_and_move(self.die, rolls)
        if score > self.high_score:
            self.high_score = score
            self.in_the_lead = player
        return self.high_score

    @property
    def player_scores(self):
        offset = "\n" + " " * 15
        return offset.join([str(p) for p in self.players])

    def evaluate(self):
        print("Evaluating Dirac game...")
        while self.high_score < self.score_threshold:
            for player in self.players:
                self.turn(player)
                if self.high_score >= self.score_threshold:
                    break
        return f"Game of Dirac evaluated. The winner is {self.in_the_lead} with a score of {self.in_the_lead.score}." \
            f"\n  There were a total of {self.turns} turns, {self.die.rolls} rolls." \
            f"\n  All players: {self.player_scores}"

    def reset(self):
        self.high_score = 0
        self.turns = 0
        self.in_the_lead = None
        for player in self.players:
            player.reset()
        self.die.reset()

    def __repr__(self):
        if self.turns > 0:
            state = f"Dirac<({self.in_the_lead} is winning with {self.in_the_lead.score})>"
        else:
            state = f"Game of Dirac has not yet begun. There are {len(self.players)} players."
        return state

die_sums = Counter([i + j + k + 3
                    for i in range(3)
                    for j in range(3)
                    for k in range(3)])

# solved part 2 with help from subreddit. will need to try to implement a solution again
# several strategies that I tried from the subreddit did not result in the correct answer?

if __name__ == "__main__":
    p1 = Player("Player 1", 8)
    p2 = Player("Player 2", 2)
    players = [p1, p2]
    game = Dirac(players)

    msg = game.evaluate()
    loser, = list(filter(lambda x: x != game.in_the_lead, game.players))
    part_1 = f"Part 1: {loser.score * game.die.rolls}"
    print(msg)
    print(part_1)

    # 105619718613031
    part_2 = max(play_quantum(0, 8, 0, 2))
    print(f"Part 2: {part_2}")
