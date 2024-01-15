class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers_count = Counter(loser for _, loser in matches)
        all_players = set(player for match in matches for player in match)

        never_lost = [player for player in all_players if player not in losers_count]
        lost_once = [player for player, count in losers_count.items() if count == 1]

        return [sorted(never_lost), sorted(lost_once)]