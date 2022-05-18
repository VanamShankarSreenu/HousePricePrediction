from HousePricePrediction import score
import unittest

class Test_score(unittest.TestCase):
    def test_parse_args(self):
        method = score.scores()
        self.assertEqual(method.args.dataset_folder,"data/processed/test.csv")
    def test_score(self):
        method = score.scores()
        method.results()
        assert method.r2 is not None
        assert method.rmse is not None
        self.assertEqual(method.df.empty,False)


if __name__ == '__main__':
    unittest.main()