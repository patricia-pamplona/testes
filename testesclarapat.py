from test_sembanco import *

import unittest


class TestMedico(unittest.TestCase):

    # 1
    def test_exame_mes(self):
        situacao1 = [(1, 1, '5/2/22', 100), (1, 2, '5/2/22', 90),
                     (2, 1, '4/9/21', 250)]
        self.assertEqual(test_exame_mes(situacao1, 1, 120), 0.5)
        self.assertEqual(test_exame_mes(situacao1, 2, 120), 0)

    # 2

    def exameMedicoMes(self):
        situacao1 = [(1, 1, '5/2/22', 100), (1, 2, '5/2/22', 90),
                     (2, 1, '4/9/21', 250)]
        self.assertEqual(exameMedicoMes(
            situacao1, 1), 2) 
        self.assertEqual(exameMedicoMes(situacao1, 2), 1)