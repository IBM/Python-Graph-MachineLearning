from collections import defaultdict
from heapq import nlargest

class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        return sum(nlargest(K, self.scores.values()))

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0