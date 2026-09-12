import unittest
from tool import choose,metrics
class ThresholdTests(unittest.TestCase):
 def test_selection(self):
  scores=[.1,.4,.8,.9]; actual=[0,0,1,1]; self.assertEqual(metrics(scores,actual,.8)['precision'],1); self.assertEqual(choose(scores,actual,.9,.5)['threshold'],.8); self.assertIsNone(choose(scores,actual,1.1,0))
if __name__=='__main__':unittest.main()
