import cProfile
import pstats
from pstats import SortKey

import hedger

teams = [
    ('Gonzaga', 98.38),
    ('Creighton', 88.85),
    ('Southern California', 90.96),
    ('Oregon', 87.39),
    ('Michigan', 90.96),
    ('Florida State', 88.93),
    ('UCLA', 88.97),
    ('Alabama', 90.57),
    ('Baylor', 97.13),
    ('Villanova', 87.75),
    ('Arkansas', 88.38),
    ('Oral Roberts', 76.43),
    ('Loyola (IL)', 88.6),
    ('Oregon State', 86.15),
    ('Syracuse', 86.02),
    ('Houston', 93.12),
]

entries = [hedger.Entry(*team) for team in teams]
tournament = hedger.Tournament(entries)

brackets = tournament.brackets

with cProfile.Profile() as pr:
    for bracket in brackets[:2]:
        bracket.summarize()

with open('time_profile_stats_4.txt', 'w') as stream:
    stats = pstats.Stats(pr, stream=stream)
    stats.sort_stats(SortKey.CUMULATIVE)
    stats.print_stats()
