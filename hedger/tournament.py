import hedger
from hedger import Result


class Tournament:
    def __init__(self, entries):
        self._entries = entries
        self._brackets = self._get_brackets()

    @property
    def entries(self):
        return self._entries

    @property
    def brackets(self):
        return self._brackets

    def _get_brackets(self):
        n_brackets = self._get_n_brackets()
        brackets = list()
        for code in range(n_brackets):
            results = self._get_results_from_code(code)
            bracket = self._make_bracket(results)
            brackets.append(bracket)
        return brackets

    def _get_n_brackets(self):
        n_matches = self._get_n_matches()
        return 2 ** n_matches

    def _get_n_matches(self):
        n_entries = len(self._entries)
        return n_entries - 1

    def _get_results_from_code(self, bracket_index):
        binary = self._convert_to_binary(bracket_index)
        results = [self._decode_bit_as_result(b) for b in binary]
        return results

    def _convert_to_binary(self, bracket_index):
        n_digits = self._get_n_matches()
        binary_fmt = "{" + "0:0{}b".format(n_digits) + "}"
        return binary_fmt.format(bracket_index)

    def _decode_bit_as_result(self, bit):
        if int(bit) == Result.TOP_WINS.value:
            return Result.TOP_WINS
        else:
            return Result.BOTTOM_WINS

    def _make_bracket(self, results):
        bracket_builder = hedger.BracketBuilder(self, results)
        bracket = bracket_builder.get_bracket()

        return bracket
