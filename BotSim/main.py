import random
import os, binascii

ID_SIZE_IN_BYTES = 4

class Player:
    def __init__(self, ID, Rank, Skill, Bot):
        self.id = ID
        self.rank = Rank
        self.skill = Skill
        self.is_bot = Bot
        self.win_rate = 0
        self.playing = 0
        self.total_wins = 0
        self.win_streak = 0
        self.games_played = 0

    def win (self):
        self.games_played += 1
        self.total_wins += 1
        if self.win_streak == 3:
            self.rank += 1
            self.win_streak = 0
        else:
            self.win_streak += 1

    def loss (self):
        self.games_played += 1
        if self.win_streak == -5:
            self.rank -= 1
            self.win_streak = 0
        else:
            self.win_streak -= 1


class GameControl:
    def __init__(self, N_games):
        self.n_games = N_games
        self.player_list = []


    def add_players(self, N_players):

        self.player_list.append(create_player())

def make_game(p1, p2):
    p1_score = random.randint(0, p1.skill)
    p2_score = random.randint(0, p2.skill)
    if p1_score > p2_score:
        p1.win()
        p2.loss()
    elif p1_score < p2_score:
        p1.loss()
        p2.win()
    else:
        if random.randint(0, 1) == 0:
            p1.win()
            p2.loss()
        else:
            p1.loss()
            p2.win()


def create_player(rank, skill):
    ID = binascii.b2a_hex(os.urandom(ID_SIZE_IN_BYTES))
    p1 = Player(ID, rank, skill, 0)
    print(p1.id, p1.rank, p1.skill)
    return ID

def create_bot(rank, skill):
    ID = binascii.b2a_hex(os.urandom(ID_SIZE_IN_BYTES))
    p1 = Player(ID, rank, skill, 0)
    print(p1.id, p1.rank, p1.skill)
    return ID


if __name__ == '__main__':
    p1 = Player(1, 0, 100, 0)
    p2 = Player(2, 0, 10, 0)
    for i in range (1000000):
        make_game(p1, p2)

    print("P1/P2 wins", p1.total_wins, p2.total_wins)