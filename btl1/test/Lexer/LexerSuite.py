"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""
import sys
import os
import unittest
import inspect

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_001(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("if","if,<EOF>", inspect.stack()[0].function))

    def test_002(self):
        """Operators"""
        self.assertTrue(TestLexer.test("+","+,<EOF>", inspect.stack()[0].function))

    def test_003(self):
        """Separators"""
        self.assertTrue(TestLexer.test("[]","[,],<EOF>", inspect.stack()[0].function))

    def test_004(self):
        """Identifiers"""
        self.assertTrue(TestLexer.test("_VOTien","_VOTien,<EOF>", inspect.stack()[0].function))

    def test_005(self):
        """Literals INT"""
        self.assertTrue(TestLexer.test("12","12,<EOF>", inspect.stack()[0].function))

    def test_006(self):
        """Literals INT 16*1 + 1 = 17"""
        self.assertTrue(TestLexer.test("0x11","0x11,<EOF>", inspect.stack()[0].function))

    def test_007(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.test("12.e-8","12.e-8,<EOF>", inspect.stack()[0].function))

    def test_008(self):
        """Literals String"""
        self.assertTrue(TestLexer.test(""" "VOTIEN \\r" ""","VOTIEN \\r,<EOF>", inspect.stack()[0].function))

    def test_009(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.test("// VOTIEN","<EOF>", inspect.stack()[0].function))

    def test_010(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.test("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>", inspect.stack()[0].function))

    def test_011(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.test("^","ErrorToken ^", inspect.stack()[0].function))

    def test_012(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.test(""" "VOTIEN\n" ""","Unclosed string: VOTIEN", inspect.stack()[0].function))

    def test_013(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.test(""" "VOTIEN\\f" ""","Illegal escape in string: VOTIEN\\f", inspect.stack()[0].function))


    def test_014(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.test(""" 
            const a = 2;
""","\n,const,a,=,2,;,\n,<EOF>", inspect.stack()[0].function))
    def test_015(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.test("0452.", "0452.,<EOF>", inspect.stack()[0].function))
    def test_016(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.test("-0120", "-,0,120,<EOF>", inspect.stack()[0].function))
    def test_017(self):
        """Keywords"""
        self.assertTrue(TestLexer.test("/* a * */", "<EOF>", inspect.stack()[0].function))
    def test_018(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.test("""
            2.
""", "2.,;,<EOF>", inspect.stack()[0].function))
    def test_019(self):
        """NEW_LINE"""
        self.assertTrue(TestLexer.test("""
            type Calculator interface {
                                        
                Add(x, y int) int;
                Subtract(a, b float, c int) [3]ID;
                Reset()
                                        
                SayHello(name string);
                                        
            }
""", "", inspect.stack()[0].function))
    def test_020(self):
        """for_statement"""
        self.assertTrue(TestLexer.test("""    
            func VoTien() {
                if (x > 10) {return; } 
                if (x > 10) {
                  return; 
                } else if (x == 10) {
                    var z str;
                } else {
                    var z ID;
                }
            }
        ""","", inspect.stack()[0].function))