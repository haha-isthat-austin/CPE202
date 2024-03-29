import unittest
import subprocess
from concordance import *


class TestList(unittest.TestCase):


    def test_01(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file1.txt")
        conc.write_concordance("file1_con.txt")
        err = subprocess.call("FC file1_con.txt file1_sol.txt", shell = True)
        self.assertEqual(err, 0)

        
    def test_02(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("file2_con.txt")
        err = subprocess.call("FC file2_con.txt file2_sol.txt", shell = True)
        self.assertEqual(err, 0)

        
    def test_03(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("declaration.txt")
        conc.write_concordance("declaration_con.txt")
        err = subprocess.call("FC declaration_con.txt declaration_sol.txt", shell = True)
        self.assertEqual(err, 0)

        
if __name__ == '__main__':
    unittest.main()
