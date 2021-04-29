import hedger
from hedger import utils, Result


class Tournament:
    def __init__(self, entries):
        self._entries = entries

        self._matches = None
        self._round = None
        self._last_round_matches = None
        self._results_iter = None

    def make_all_brackets(self):
        n_brackets = self._get_n_brackets()
        all_brackets = list()
        for bracket_index in range(n_brackets):
            results = self._get_results_from_index(bracket_index)
            bracket = self._make_bracket(results)
            all_brackets.append(bracket)
        return all_brackets

    def _get_n_brackets(self):
        n_matches = self._get_n_matches()
        return 2 ** n_matches

    def _get_n_matches(self):
        n_entries = len(self._entries)
        return n_entries - 1

    def _get_results_from_index(self, bracket_index):
        binary_string = self._convert_to_binary_string(bracket_index)
        results = [self._encode_bit_as_result(b) for b in binary_string]
        return results

    def _convert_to_binary_string(self, bracket_index):
        n_digits = self._get_n_matches()
        binary_fmt = "{" + "0:0{}b".format(n_digits) + "}"
        return binary_fmt.format(bracket_index)

    def _encode_bit_as_result(self, bit):
        return Result.TOP_WINS if bit == "1" else Result.BOTTOM_WINS

    def _make_bracket(self, results):
        self._initialize_bracket_variables(results)
        while self._bracket_incomplete():
            self._update_bracket_variables()

        return hedger.Bracket(self._matches)

    def _initialize_bracket_variables(self, results):
        self._matches = list()
        self._round = 0
        self._last_round_matches = self._entries
        self._result_iter = iter(results)

    def _bracket_incomplete(self):
        return len(self._last_round_matches) > 1

    def _update_bracket_variables(self):
        this_round_matches = self._make_this_round_matches()

        self._matches.extend(this_round_matches)
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
