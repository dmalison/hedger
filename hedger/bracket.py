from hedger import utils


class Bracket:
    POINTS_PER_ROUND = 320

    def __init__(self, matches):
        self._matches = matches

    @property
    def matches(self):
        return self._matches

    def score_against(self, scoring_bracket):
        match_count = self._get_match_count()
        winners_count = self._get_winners_count(scoring_bracket)

        total_score = 0
        for round_, matches in match_count.items():
            winners = winners_count.get(round_, 0)
            score = self._compute_round_score(matches, winners)
            total_score += score

        return score

    def _get_match_count(self):
        match_count = utils.MapToCounts()
        for match in self.matches:
            match_count.increment(match.round)
        return match_count

    def _get_winners_count(self, scoring_bracket):
        winners_count = utils.MapToCounts()
        for match, scoring_match in zip(self.matches, scoring_bracket.matches):
            winner_is_correct = self._check_if_winner_is_correct(
                match,
                scoring_match
            )
            if winner_is_correct:
                winners_count.increment(match.round)
        return winners_count

    def _check_if_winner_is_correct(self, match, scoring_match):
        return match.get_winner() == scoring_match.get_winner()

    def _compute_round_score(self, matches, winners):
        return winners / matches * self.POINTS_PER_ROUND
