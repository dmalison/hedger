import hedger
from hedger import utils


class Bracket:
    POINTS_PER_ROUND = 320

    def __init__(self, matches, tournament):
        self._matches = matches
        self._tournament = tournament

    @property
    def matches(self):
        return self._matches

    def summarize(self):
        return self.get_dist().summarize()

    def get_code(self):
        binary = self._get_results_as_binary()
        return int(binary, 2)

    def get_prob(self):
        prob = 1
        for match in self.matches:
            prob *= match.get_prob()
        return prob

    def get_dist(self):
        points = list()
        for scoring_bracket in self._tournament.brackets:
            score = self._get_score(scoring_bracket)
            sample_point = utils.Point(
                omega=scoring_bracket.get_code(),
                prob=scoring_bracket.get_prob(),
                value=score
            )
            points.append(sample_point)
        return utils.DiscreteDist(points)

    def _get_score(self, scoring_bracket):
        match_count = self._get_match_count()
        winners_count = self._get_winners_count(scoring_bracket)

        total_score = 0
        for round_, matches in match_count.items():
            winners = winners_count.get(round_, 0)
            score = self._get_round_score(matches, winners)
            total_score += score

        return int(total_score)

    def _get_results_as_binary(self):
        values = [str(match.result.value) for match in self._matches]
        return ''.join(values)

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

    def _get_round_score(self, matches, winners):
        return winners / matches * self.POINTS_PER_ROUND


class BracketBuilder:
    def __init__(self, tournament, results):
        self._tournament = tournament
        self._results = results

        self._last_round_matches = None
        self._result_iter = None
        self._matches = None
        self._round = None

    def get_bracket(self):
        self._initialize_recursion()
        while self._is_bracket_incomplete():
            self._add_another_round_of_matches()

        return hedger.Bracket(self._all_matches, self._tournament)

    def _initialize_recursion(self):
        self._last_round_matches = self._tournament.entries
        self._result_iter = iter(self._results)
        self._all_matches = list()
        self._round = 0

    def _is_bracket_incomplete(self):
        return len(self._last_round_matches) > 1

    def _add_another_round_of_matches(self):
        this_round_matches = self._make_this_round_matches()
        self._update_state(this_round_matches)

    def _update_state(self, this_round_matches):
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
