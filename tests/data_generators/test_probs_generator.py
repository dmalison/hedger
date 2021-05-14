from hedger import utils, csv_generators
from tests import utils as tests_utils


class ProbsGeneratorTest(tests_utils.CsvTestCase):
    def test_generate_probs_csv_with_four_equal_teams(self):
        teams = [
            {'name': 'Gryffindor', 'rating': 100},
            {'name': 'Ravenclaw', 'rating': 100},
            {'name': 'Hufflepuff', 'rating': 100},
            {'name': 'Slytherin', 'rating': 100},
        ]

        probs_generator = csv_generators.ProbsGenerator(teams)
        probs_generator.write(self.temp_filepath)

        with utils.CsvReader(self.temp_filepath) as reader:
            for row in reader:
                self.assertEqual(row['prob'], .125)

    def test_generate_probs_csv_with_four_unequal_teams(self):
        teams = [
            {'name': 'Gryffindor', 'rating': 106.264},
            {'name': 'Ravenclaw', 'rating': 100},
            {'name': 'Hufflepuff', 'rating': 100},
            {'name': 'Slytherin', 'rating': 93.736},
        ]

        probs_generator = csv_generators.ProbsGenerator(teams)
        probs_generator.write(self.temp_filepath)

        fixture_filepath = "tests/data/test_generate_probs_csv_fixture.csv"
        self.assertCsvAlmostEqual(self.temp_filepath, fixture_filepath, 4)
