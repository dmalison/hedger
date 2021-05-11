from hedger.result import Result
from hedger.bracket import Bracket, BracketBuilder
from hedger.entry import Entry, EmptyEntry
from hedger.match import Match
from hedger.tournament import Tournament


def generate_score_csv(teams, filepath='data/bracket_scores.csv'):
    entries = [Entry(team) for team in teams]
