from collections import defaultdict

class Solution:
    def bestTeamScore(self, scores, ages):
        n = len(scores)
        players = [(ages[i], scores[i]) for i in range(n)]
        players.sort()

        memo = defaultdict(int)

        def dp(index):
            if index < 0:
                return 0

            if index in memo:
                return memo[index]

            best_score = players[index][1]  # Initialize with the score of the current player

            for j in range(index - 1, -1, -1):
                if players[j][1] <= players[index][1]:
                    best_score = max(best_score, dp(j) + players[index][1])

            memo[index] = best_score
            return best_score

        max_score = 0
        for i in range(n):
            max_score = max(max_score, dp(i))

        return max_score