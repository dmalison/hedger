import hedger
from hedger import utils


class Bracket:
    POINTS_PER_ROUND = 320

    def __init__(self, matches):
        self._matches = matches

    @property
    def matches(self):
        return self._matches

    @property
    def results_code(self):
        return [match.result.value for m in self._matches]
    
    def compute_score(self, scoring_bracket):
        match_count = self._get_match_count()
        winners_count = self._get_winners_count(scoring_bracket)

        total_score = 0
        for round_, matches in match_count.items():
            winners = winners_count.get(round_, 0)
            score = self._compute_round_score(matches, winners)
            total_score += score

        return total_score

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


class BracketBuilder:
    def __init__(self, entries, results):
        self._entries = entries
        self._results = results

        self._last_round_matches = None
        self._result_iter = None
        self._matches = None
        self._round = None

    def get_bracket(self):
        self._initialize_recursion()
        while self._bracket_incomplete():
            self._add_another_round_of_matches()

        return hedger.Bracket(self._all_matches)

    def _initialize_recursion(self):
        self._last_round_matches = self._entries
        self._result_iter = iter(self._results)
        self._all_matches = list()
        self._round = 0

    def _bracket_incomplete(self):
        return len(self._last_round_matches) > 1

    def _add_another_round_of_matches(self):
        this_round_matches = self._make_this_round_matches()
        self._update_recursion(this_round_matches)

    def _update_recursion(self, this_round_matches):
        self._all_matches.extend(this_round_matches)
        self._round += 1
        self._last_round_matches = this_round_matches

    def _make_this_round_matches(self):
        index = 0
        this_round_matches = list()
        for top, bottom in utils.pairwise_grouper(
            self._last_round_matches,
            fillvalue=hedger.EmptyEntry()
        ):
            new_match = hedger.Match(
                round_=self._round,
                index=index,
                top=top,
                bottom=bottom,
                result=next(self._result_iter)
            )
            this_round_matches.append(new_match)
            index += 1

        return this_round_matches
