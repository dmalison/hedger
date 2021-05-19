import hedger
from hedger import utils


class Bracket:
    POINTS_PER_ROUND = 320

    def __init__(self, matches, tournament):
        self._matches = matches
        self._tournament = tournament

        self._code = self._get_code()
        self._prob = self._get_prob()
        self._match_count = self._get_match_count()
        self._winner_names = self._get_winner_names()
        self._points_per_match = self._get_points_per_match()

    @property
    def matches(self):
        return self._matches

    @property
    def code(self):
        return self._code

    @property
    def prob(self):
        return self._prob

    @property
    def winner_names(self):
        return self._winner_names

    def summarize(self):
        return self.get_dist().summarize()

    def _get_code(self):
        binary = self._get_results_as_binary()
        return int(binary, 2)

    def _get_prob(self):
        prob = 1
        for match in self.matches:
            prob *= match.get_prob()
        return prob

    def _get_winner_names(self):
        return [match.winner.name for match in self._matches]

    def _get_points_per_match(self):
        return [
            self.POINTS_PER_ROUND / self._match_count.get(match.round)
            for match in self._matches
        ]

    def get_dist(self):
        points = list()
        for code, (prob, winner_names) in \
                self._tournament.brackets_info.items():
            score = self._get_score(winner_names)
            sample_point = utils.Point(
                omega=code,
                prob=prob,
                value=score
            )
            points.append(sample_point)
        return utils.DiscreteDist(points)

    def _get_score(self, scoring_bracket_winner_names):
        total_score = 0
        for winner, scoring_winner, points in zip(
                self._winner_names,
                scoring_bracket_winner_names,
                self._points_per_match
        ):
            if winner == scoring_winner:
                total_score += points

        return int(total_score)

    def _get_results_as_binary(self):
        values = [str(match.result.value) for match in self._matches]
        return ''.join(values)

    def _get_match_count(self):
        match_count = utils.MapToCounts()
        for match in self.matches:
            match_count.increment(match.round)
        return match_count


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
