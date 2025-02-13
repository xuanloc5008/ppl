# Generated from main/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u02b2\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\7\2\u0086")
        buf.write("\n\2\f\2\16\2\u0089\13\2\3\2\3\2\3\2\7\2\u008e\n\2\f\2")
        buf.write("\16\2\u0091\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\5\3\u009f\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4\u00ac\n\4\3\5\3\5\3\5\3\5\3\5\3\5\5")
        buf.write("\5\u00b4\n\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\5\7\u00c3\n\7\3\7\3\7\3\b\3\b\5\b\u00c9\n\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\5\t\u00d0\n\t\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\5\13\u00d9\n\13\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\5\r\u00e2\n\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\5")
        buf.write("\16\u00eb\n\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\5\20\u00f5\n\20\3\20\3\20\3\21\3\21\3\21\3\21\5\21\u00fd")
        buf.write("\n\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\5\23")
        buf.write("\u0108\n\23\3\23\3\23\3\23\5\23\u010d\n\23\3\23\5\23\u0110")
        buf.write("\n\23\3\24\3\24\3\24\5\24\u0115\n\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\5\25\u011c\n\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\7\26\u0124\n\26\f\26\16\26\u0127\13\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\7\27\u012f\n\27\f\27\16\27\u0132\13\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u013a\n\30\f\30\16")
        buf.write("\30\u013d\13\30\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u0145")
        buf.write("\n\31\f\31\16\31\u0148\13\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\7\32\u0150\n\32\f\32\16\32\u0153\13\32\3\33\3\33")
        buf.write("\3\33\5\33\u0158\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\5\34\u0164\n\34\7\34\u0166\n\34\f\34")
        buf.write("\16\34\u0169\13\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\5\35\u0176\n\35\3\36\3\36\5\36\u017a")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3\37\5\37\u0181\n\37\3 \3 \3")
        buf.write(" \3 \3 \3!\3!\3!\3!\5!\u018c\n!\3!\3!\5!\u0190\n!\3\"")
        buf.write("\3\"\3\"\3\"\5\"\u0196\n\"\3\"\3\"\5\"\u019a\n\"\3\"\3")
        buf.write("\"\3\"\3\"\7\"\u01a0\n\"\f\"\16\"\u01a3\13\"\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3#\3#\5#\u01ad\n#\3$\3$\3$\3%\3%\3%\3%\5%")
        buf.write("\u01b6\n%\3&\3&\3&\3&\3&\3&\3&\3&\5&\u01c0\n&\3&\3&\5")
        buf.write("&\u01c4\n&\3&\3&\3&\3&\7&\u01ca\n&\f&\16&\u01cd\13&\3")
        buf.write("&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\7(\u01db\n")
        buf.write("(\f(\16(\u01de\13(\3)\3)\3)\3)\5)\u01e4\n)\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3+\3+\3+\3+\5+\u01f2\n+\3,\3,\3,\3,\3-\3")
        buf.write("-\3.\3.\3.\3.\3.\5.\u01ff\n.\3/\3/\3/\5/\u0204\n/\3\60")
        buf.write("\3\60\3\60\3\60\5\60\u020a\n\60\3\61\3\61\3\61\3\61\3")
        buf.write("\62\3\62\3\62\3\62\3\62\7\62\u0215\n\62\f\62\16\62\u0218")
        buf.write("\13\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3")
        buf.write("\63\3\63\3\63\7\63\u0226\n\63\f\63\16\63\u0229\13\63\3")
        buf.write("\63\3\63\3\63\5\63\u022e\n\63\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\7\64\u0238\n\64\f\64\16\64\u023b\13\64")
        buf.write("\3\64\3\64\7\64\u023f\n\64\f\64\16\64\u0242\13\64\3\64")
        buf.write("\3\64\7\64\u0246\n\64\f\64\16\64\u0249\13\64\3\64\5\64")
        buf.write("\u024c\n\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3")
        buf.write("\66\5\66\u0257\n\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67")
        buf.write("\38\38\38\38\58\u0264\n8\38\38\38\38\78\u026a\n8\f8\16")
        buf.write("8\u026d\138\38\38\39\39\3:\3:\3;\3;\3;\3;\5;\u0279\n;")
        buf.write("\3;\3;\3;\3;\5;\u027f\n;\3;\3;\3<\3<\3<\3<\5<\u0287\n")
        buf.write("<\3=\3=\7=\u028b\n=\f=\16=\u028e\13=\3=\6=\u0291\n=\r")
        buf.write("=\16=\u0292\5=\u0295\n=\3>\3>\3>\3?\3?\5?\u029c\n?\3@")
        buf.write("\3@\3@\3@\3@\5@\u02a3\n@\3A\3A\3A\3A\3A\5A\u02aa\nA\3")
        buf.write("B\7B\u02ad\nB\fB\16B\u02b0\13B\3B\2\b*,.\60\62\66C\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\2")
        buf.write("\b\4\2\13\16\66\66\3\2\34!\3\2\27\30\3\2\31\33\4\2\30")
        buf.write("\30$$\4\2&*//\2\u02d7\2\u0087\3\2\2\2\4\u009e\3\2\2\2")
        buf.write("\6\u00ab\3\2\2\2\b\u00b3\3\2\2\2\n\u00b5\3\2\2\2\f\u00c2")
        buf.write("\3\2\2\2\16\u00c8\3\2\2\2\20\u00cf\3\2\2\2\22\u00d1\3")
        buf.write("\2\2\2\24\u00d8\3\2\2\2\26\u00da\3\2\2\2\30\u00de\3\2")
        buf.write("\2\2\32\u00ea\3\2\2\2\34\u00ec\3\2\2\2\36\u00f0\3\2\2")
        buf.write("\2 \u00fc\3\2\2\2\"\u00fe\3\2\2\2$\u010f\3\2\2\2&\u0111")
        buf.write("\3\2\2\2(\u011b\3\2\2\2*\u011d\3\2\2\2,\u0128\3\2\2\2")
        buf.write(".\u0133\3\2\2\2\60\u013e\3\2\2\2\62\u0149\3\2\2\2\64\u0157")
        buf.write("\3\2\2\2\66\u0159\3\2\2\28\u0175\3\2\2\2:\u0179\3\2\2")
        buf.write("\2<\u0180\3\2\2\2>\u0182\3\2\2\2@\u0187\3\2\2\2B\u0191")
        buf.write("\3\2\2\2D\u01ac\3\2\2\2F\u01ae\3\2\2\2H\u01b5\3\2\2\2")
        buf.write("J\u01b7\3\2\2\2L\u01d1\3\2\2\2N\u01dc\3\2\2\2P\u01e3\3")
        buf.write("\2\2\2R\u01e5\3\2\2\2T\u01f1\3\2\2\2V\u01f3\3\2\2\2X\u01f7")
        buf.write("\3\2\2\2Z\u01fe\3\2\2\2\\\u0200\3\2\2\2^\u0209\3\2\2\2")
        buf.write("`\u020b\3\2\2\2b\u020f\3\2\2\2d\u022d\3\2\2\2f\u022f\3")
        buf.write("\2\2\2h\u024d\3\2\2\2j\u0256\3\2\2\2l\u025d\3\2\2\2n\u025f")
        buf.write("\3\2\2\2p\u0270\3\2\2\2r\u0272\3\2\2\2t\u0278\3\2\2\2")
        buf.write("v\u0282\3\2\2\2x\u0294\3\2\2\2z\u0296\3\2\2\2|\u0299\3")
        buf.write("\2\2\2~\u02a2\3\2\2\2\u0080\u02a4\3\2\2\2\u0082\u02ae")
        buf.write("\3\2\2\2\u0084\u0086\7?\2\2\u0085\u0084\3\2\2\2\u0086")
        buf.write("\u0089\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2")
        buf.write("\u0088\u008a\3\2\2\2\u0089\u0087\3\2\2\2\u008a\u008f\5")
        buf.write("\4\3\2\u008b\u008e\5\4\3\2\u008c\u008e\7?\2\2\u008d\u008b")
        buf.write("\3\2\2\2\u008d\u008c\3\2\2\2\u008e\u0091\3\2\2\2\u008f")
        buf.write("\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0092\3\2\2\2")
        buf.write("\u0091\u008f\3\2\2\2\u0092\u0093\7\2\2\3\u0093\3\3\2\2")
        buf.write("\2\u0094\u0095\5@!\2\u0095\u0096\7.\2\2\u0096\u009f\3")
        buf.write("\2\2\2\u0097\u0098\5> \2\u0098\u0099\7.\2\2\u0099\u009f")
        buf.write("\3\2\2\2\u009a\u009f\5B\"\2\u009b\u009f\5J&\2\u009c\u009f")
        buf.write("\5L\'\2\u009d\u009f\5R*\2\u009e\u0094\3\2\2\2\u009e\u0097")
        buf.write("\3\2\2\2\u009e\u009a\3\2\2\2\u009e\u009b\3\2\2\2\u009e")
        buf.write("\u009c\3\2\2\2\u009e\u009d\3\2\2\2\u009f\5\3\2\2\2\u00a0")
        buf.write("\u00ac\7\67\2\2\u00a1\u00ac\78\2\2\u00a2\u00ac\79\2\2")
        buf.write("\u00a3\u00ac\7:\2\2\u00a4\u00ac\7;\2\2\u00a5\u00ac\7<")
        buf.write("\2\2\u00a6\u00ac\7\25\2\2\u00a7\u00ac\7\26\2\2\u00a8\u00ac")
        buf.write("\7\24\2\2\u00a9\u00ac\5\36\20\2\u00aa\u00ac\5\30\r\2\u00ab")
        buf.write("\u00a0\3\2\2\2\u00ab\u00a1\3\2\2\2\u00ab\u00a2\3\2\2\2")
        buf.write("\u00ab\u00a3\3\2\2\2\u00ab\u00a4\3\2\2\2\u00ab\u00a5\3")
        buf.write("\2\2\2\u00ab\u00a6\3\2\2\2\u00ab\u00a7\3\2\2\2\u00ab\u00a8")
        buf.write("\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa\3\2\2\2\u00ac")
        buf.write("\7\3\2\2\2\u00ad\u00b4\7\f\2\2\u00ae\u00b4\7\r\2\2\u00af")
        buf.write("\u00b4\7\16\2\2\u00b0\u00b4\7\13\2\2\u00b1\u00b4\5\22")
        buf.write("\n\2\u00b2\u00b4\7\66\2\2\u00b3\u00ad\3\2\2\2\u00b3\u00ae")
        buf.write("\3\2\2\2\u00b3\u00af\3\2\2\2\u00b3\u00b0\3\2\2\2\u00b3")
        buf.write("\u00b1\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\t\3\2\2\2\u00b5")
        buf.write("\u00b6\t\2\2\2\u00b6\13\3\2\2\2\u00b7\u00c3\5@!\2\u00b8")
        buf.write("\u00c3\5> \2\u00b9\u00c3\5V,\2\u00ba\u00c3\5f\64\2\u00bb")
        buf.write("\u00c3\5n8\2\u00bc\u00c3\5p9\2\u00bd\u00c3\5r:\2\u00be")
        buf.write("\u00c3\5t;\2\u00bf\u00c3\5v<\2\u00c0\u00c3\5z>\2\u00c1")
        buf.write("\u00c3\5\u0080A\2\u00c2\u00b7\3\2\2\2\u00c2\u00b8\3\2")
        buf.write("\2\2\u00c2\u00b9\3\2\2\2\u00c2\u00ba\3\2\2\2\u00c2\u00bb")
        buf.write("\3\2\2\2\u00c2\u00bc\3\2\2\2\u00c2\u00bd\3\2\2\2\u00c2")
        buf.write("\u00be\3\2\2\2\u00c2\u00bf\3\2\2\2\u00c2\u00c0\3\2\2\2")
        buf.write("\u00c2\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5\5")
        buf.write("x=\2\u00c5\r\3\2\2\2\u00c6\u00c9\5\20\t\2\u00c7\u00c9")
        buf.write("\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9")
        buf.write("\17\3\2\2\2\u00ca\u00cb\5\6\4\2\u00cb\u00cc\7-\2\2\u00cc")
        buf.write("\u00cd\5\16\b\2\u00cd\u00d0\3\2\2\2\u00ce\u00d0\5\6\4")
        buf.write("\2\u00cf\u00ca\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0\21\3")
        buf.write("\2\2\2\u00d1\u00d2\5\24\13\2\u00d2\u00d3\5\n\6\2\u00d3")
        buf.write("\23\3\2\2\2\u00d4\u00d5\5\26\f\2\u00d5\u00d6\5\24\13\2")
        buf.write("\u00d6\u00d9\3\2\2\2\u00d7\u00d9\5\26\f\2\u00d8\u00d4")
        buf.write("\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9\25\3\2\2\2\u00da\u00db")
        buf.write("\7\64\2\2\u00db\u00dc\7\67\2\2\u00dc\u00dd\7\65\2\2\u00dd")
        buf.write("\27\3\2\2\2\u00de\u00df\7\66\2\2\u00df\u00e1\7\62\2\2")
        buf.write("\u00e0\u00e2\5\32\16\2\u00e1\u00e0\3\2\2\2\u00e1\u00e2")
        buf.write("\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\7\63\2\2\u00e4")
        buf.write("\31\3\2\2\2\u00e5\u00e6\5\34\17\2\u00e6\u00e7\7-\2\2\u00e7")
        buf.write("\u00e8\5\32\16\2\u00e8\u00eb\3\2\2\2\u00e9\u00eb\5\34")
        buf.write("\17\2\u00ea\u00e5\3\2\2\2\u00ea\u00e9\3\2\2\2\u00eb\33")
        buf.write("\3\2\2\2\u00ec\u00ed\7\66\2\2\u00ed\u00ee\7,\2\2\u00ee")
        buf.write("\u00ef\5*\26\2\u00ef\35\3\2\2\2\u00f0\u00f1\5 \21\2\u00f1")
        buf.write("\u00f2\5\b\5\2\u00f2\u00f4\7\62\2\2\u00f3\u00f5\5&\24")
        buf.write("\2\u00f4\u00f3\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f6")
        buf.write("\3\2\2\2\u00f6\u00f7\7\63\2\2\u00f7\37\3\2\2\2\u00f8\u00f9")
        buf.write("\5\"\22\2\u00f9\u00fa\5 \21\2\u00fa\u00fd\3\2\2\2\u00fb")
        buf.write("\u00fd\5\"\22\2\u00fc\u00f8\3\2\2\2\u00fc\u00fb\3\2\2")
        buf.write("\2\u00fd!\3\2\2\2\u00fe\u00ff\7\64\2\2\u00ff\u0100\7\67")
        buf.write("\2\2\u0100\u0101\7\65\2\2\u0101#\3\2\2\2\u0102\u0110\5")
        buf.write("\6\4\2\u0103\u0110\5\30\r\2\u0104\u0105\7\66\2\2\u0105")
        buf.write("\u0107\7\62\2\2\u0106\u0108\5&\24\2\u0107\u0106\3\2\2")
        buf.write("\2\u0107\u0108\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u0110")
        buf.write("\7\63\2\2\u010a\u010c\7\62\2\2\u010b\u010d\5&\24\2\u010c")
        buf.write("\u010b\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010e\3\2\2\2")
        buf.write("\u010e\u0110\7\63\2\2\u010f\u0102\3\2\2\2\u010f\u0103")
        buf.write("\3\2\2\2\u010f\u0104\3\2\2\2\u010f\u010a\3\2\2\2\u0110")
        buf.write("%\3\2\2\2\u0111\u0114\5$\23\2\u0112\u0113\7-\2\2\u0113")
        buf.write("\u0115\5&\24\2\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2\2")
        buf.write("\u0115\'\3\2\2\2\u0116\u0117\5*\26\2\u0117\u0118\7-\2")
        buf.write("\2\u0118\u0119\5(\25\2\u0119\u011c\3\2\2\2\u011a\u011c")
        buf.write("\5*\26\2\u011b\u0116\3\2\2\2\u011b\u011a\3\2\2\2\u011c")
        buf.write(")\3\2\2\2\u011d\u011e\b\26\1\2\u011e\u011f\5,\27\2\u011f")
        buf.write("\u0125\3\2\2\2\u0120\u0121\f\4\2\2\u0121\u0122\7#\2\2")
        buf.write("\u0122\u0124\5,\27\2\u0123\u0120\3\2\2\2\u0124\u0127\3")
        buf.write("\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126+")
        buf.write("\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u0129\b\27\1\2\u0129")
        buf.write("\u012a\5.\30\2\u012a\u0130\3\2\2\2\u012b\u012c\f\4\2\2")
        buf.write("\u012c\u012d\7\"\2\2\u012d\u012f\5.\30\2\u012e\u012b\3")
        buf.write("\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u0131")
        buf.write("\3\2\2\2\u0131-\3\2\2\2\u0132\u0130\3\2\2\2\u0133\u0134")
        buf.write("\b\30\1\2\u0134\u0135\5\60\31\2\u0135\u013b\3\2\2\2\u0136")
        buf.write("\u0137\f\4\2\2\u0137\u0138\t\3\2\2\u0138\u013a\5\60\31")
        buf.write("\2\u0139\u0136\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u0139")
        buf.write("\3\2\2\2\u013b\u013c\3\2\2\2\u013c/\3\2\2\2\u013d\u013b")
        buf.write("\3\2\2\2\u013e\u013f\b\31\1\2\u013f\u0140\5\62\32\2\u0140")
        buf.write("\u0146\3\2\2\2\u0141\u0142\f\4\2\2\u0142\u0143\t\4\2\2")
        buf.write("\u0143\u0145\5\62\32\2\u0144\u0141\3\2\2\2\u0145\u0148")
        buf.write("\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147")
        buf.write("\61\3\2\2\2\u0148\u0146\3\2\2\2\u0149\u014a\b\32\1\2\u014a")
        buf.write("\u014b\5\64\33\2\u014b\u0151\3\2\2\2\u014c\u014d\f\4\2")
        buf.write("\2\u014d\u014e\t\5\2\2\u014e\u0150\5\64\33\2\u014f\u014c")
        buf.write("\3\2\2\2\u0150\u0153\3\2\2\2\u0151\u014f\3\2\2\2\u0151")
        buf.write("\u0152\3\2\2\2\u0152\63\3\2\2\2\u0153\u0151\3\2\2\2\u0154")
        buf.write("\u0155\t\6\2\2\u0155\u0158\5*\26\2\u0156\u0158\5\66\34")
        buf.write("\2\u0157\u0154\3\2\2\2\u0157\u0156\3\2\2\2\u0158\65\3")
        buf.write("\2\2\2\u0159\u015a\b\34\1\2\u015a\u015b\58\35\2\u015b")
        buf.write("\u0167\3\2\2\2\u015c\u0163\f\4\2\2\u015d\u015e\7\64\2")
        buf.write("\2\u015e\u015f\5*\26\2\u015f\u0160\7\65\2\2\u0160\u0164")
        buf.write("\3\2\2\2\u0161\u0162\7+\2\2\u0162\u0164\5*\26\2\u0163")
        buf.write("\u015d\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u0166\3\2\2\2")
        buf.write("\u0165\u015c\3\2\2\2\u0166\u0169\3\2\2\2\u0167\u0165\3")
        buf.write("\2\2\2\u0167\u0168\3\2\2\2\u0168\67\3\2\2\2\u0169\u0167")
        buf.write("\3\2\2\2\u016a\u0176\5\6\4\2\u016b\u016c\7\60\2\2\u016c")
        buf.write("\u016d\5*\26\2\u016d\u016e\7\61\2\2\u016e\u0176\3\2\2")
        buf.write("\2\u016f\u0176\7\66\2\2\u0170\u0171\7\66\2\2\u0171\u0172")
        buf.write("\7\60\2\2\u0172\u0173\5:\36\2\u0173\u0174\7\61\2\2\u0174")
        buf.write("\u0176\3\2\2\2\u0175\u016a\3\2\2\2\u0175\u016b\3\2\2\2")
        buf.write("\u0175\u016f\3\2\2\2\u0175\u0170\3\2\2\2\u01769\3\2\2")
        buf.write("\2\u0177\u017a\5<\37\2\u0178\u017a\3\2\2\2\u0179\u0177")
        buf.write("\3\2\2\2\u0179\u0178\3\2\2\2\u017a;\3\2\2\2\u017b\u0181")
        buf.write("\5*\26\2\u017c\u017d\5*\26\2\u017d\u017e\7-\2\2\u017e")
        buf.write("\u017f\5<\37\2\u017f\u0181\3\2\2\2\u0180\u017b\3\2\2\2")
        buf.write("\u0180\u017c\3\2\2\2\u0181=\3\2\2\2\u0182\u0183\7\17\2")
        buf.write("\2\u0183\u0184\7\66\2\2\u0184\u0185\7%\2\2\u0185\u0186")
        buf.write("\5*\26\2\u0186?\3\2\2\2\u0187\u0188\7\20\2\2\u0188\u018f")
        buf.write("\7\66\2\2\u0189\u0190\5\b\5\2\u018a\u018c\5\b\5\2\u018b")
        buf.write("\u018a\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018d\3\2\2\2")
        buf.write("\u018d\u018e\7%\2\2\u018e\u0190\5*\26\2\u018f\u0189\3")
        buf.write("\2\2\2\u018f\u018b\3\2\2\2\u0190A\3\2\2\2\u0191\u0192")
        buf.write("\7\7\2\2\u0192\u0193\7\66\2\2\u0193\u0195\7\60\2\2\u0194")
        buf.write("\u0196\5D#\2\u0195\u0194\3\2\2\2\u0195\u0196\3\2\2\2\u0196")
        buf.write("\u0197\3\2\2\2\u0197\u0199\7\61\2\2\u0198\u019a\5\b\5")
        buf.write("\2\u0199\u0198\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019b")
        buf.write("\3\2\2\2\u019b\u019c\5\u0082B\2\u019c\u01a1\7\62\2\2\u019d")
        buf.write("\u01a0\7?\2\2\u019e\u01a0\5T+\2\u019f\u019d\3\2\2\2\u019f")
        buf.write("\u019e\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2")
        buf.write("\u01a1\u01a2\3\2\2\2\u01a2\u01a4\3\2\2\2\u01a3\u01a1\3")
        buf.write("\2\2\2\u01a4\u01a5\7\63\2\2\u01a5\u01a6\7.\2\2\u01a6C")
        buf.write("\3\2\2\2\u01a7\u01a8\5F$\2\u01a8\u01a9\7-\2\2\u01a9\u01aa")
        buf.write("\5D#\2\u01aa\u01ad\3\2\2\2\u01ab\u01ad\5F$\2\u01ac\u01a7")
        buf.write("\3\2\2\2\u01ac\u01ab\3\2\2\2\u01adE\3\2\2\2\u01ae\u01af")
        buf.write("\5H%\2\u01af\u01b0\5\b\5\2\u01b0G\3\2\2\2\u01b1\u01b2")
        buf.write("\7\66\2\2\u01b2\u01b3\7-\2\2\u01b3\u01b6\5H%\2\u01b4\u01b6")
        buf.write("\7\66\2\2\u01b5\u01b1\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6")
        buf.write("I\3\2\2\2\u01b7\u01b8\7\7\2\2\u01b8\u01b9\7\60\2\2\u01b9")
        buf.write("\u01ba\7\66\2\2\u01ba\u01bb\7\66\2\2\u01bb\u01bc\7\61")
        buf.write("\2\2\u01bc\u01bd\7\66\2\2\u01bd\u01bf\7\60\2\2\u01be\u01c0")
        buf.write("\5D#\2\u01bf\u01be\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c1")
        buf.write("\3\2\2\2\u01c1\u01c3\7\61\2\2\u01c2\u01c4\5\b\5\2\u01c3")
        buf.write("\u01c2\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c5\3\2\2\2")
        buf.write("\u01c5\u01c6\5\u0082B\2\u01c6\u01cb\7\62\2\2\u01c7\u01ca")
        buf.write("\7?\2\2\u01c8\u01ca\5T+\2\u01c9\u01c7\3\2\2\2\u01c9\u01c8")
        buf.write("\3\2\2\2\u01ca\u01cd\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb")
        buf.write("\u01cc\3\2\2\2\u01cc\u01ce\3\2\2\2\u01cd\u01cb\3\2\2\2")
        buf.write("\u01ce\u01cf\7\63\2\2\u01cf\u01d0\7.\2\2\u01d0K\3\2\2")
        buf.write("\2\u01d1\u01d2\7\b\2\2\u01d2\u01d3\7\66\2\2\u01d3\u01d4")
        buf.write("\7\t\2\2\u01d4\u01d5\7\62\2\2\u01d5\u01d6\5T+\2\u01d6")
        buf.write("\u01d7\7\63\2\2\u01d7\u01d8\7.\2\2\u01d8M\3\2\2\2\u01d9")
        buf.write("\u01db\5P)\2\u01da\u01d9\3\2\2\2\u01db\u01de\3\2\2\2\u01dc")
        buf.write("\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01ddO\3\2\2\2\u01de")
        buf.write("\u01dc\3\2\2\2\u01df\u01e0\5z>\2\u01e0\u01e1\7.\2\2\u01e1")
        buf.write("\u01e4\3\2\2\2\u01e2\u01e4\5J&\2\u01e3\u01df\3\2\2\2\u01e3")
        buf.write("\u01e2\3\2\2\2\u01e4Q\3\2\2\2\u01e5\u01e6\7\b\2\2\u01e6")
        buf.write("\u01e7\7\66\2\2\u01e7\u01e8\7\n\2\2\u01e8\u01e9\7\62\2")
        buf.write("\2\u01e9\u01ea\5T+\2\u01ea\u01eb\7\63\2\2\u01eb\u01ec")
        buf.write("\7.\2\2\u01ecS\3\2\2\2\u01ed\u01ee\5\f\7\2\u01ee\u01ef")
        buf.write("\5T+\2\u01ef\u01f2\3\2\2\2\u01f0\u01f2\5\f\7\2\u01f1\u01ed")
        buf.write("\3\2\2\2\u01f1\u01f0\3\2\2\2\u01f2U\3\2\2\2\u01f3\u01f4")
        buf.write("\5Z.\2\u01f4\u01f5\5X-\2\u01f5\u01f6\5*\26\2\u01f6W\3")
        buf.write("\2\2\2\u01f7\u01f8\t\7\2\2\u01f8Y\3\2\2\2\u01f9\u01fa")
        buf.write("\5\\/\2\u01fa\u01fb\7+\2\2\u01fb\u01fc\5Z.\2\u01fc\u01ff")
        buf.write("\3\2\2\2\u01fd\u01ff\5\\/\2\u01fe\u01f9\3\2\2\2\u01fe")
        buf.write("\u01fd\3\2\2\2\u01ff[\3\2\2\2\u0200\u0203\7\66\2\2\u0201")
        buf.write("\u0204\5^\60\2\u0202\u0204\3\2\2\2\u0203\u0201\3\2\2\2")
        buf.write("\u0203\u0202\3\2\2\2\u0204]\3\2\2\2\u0205\u0206\5`\61")
        buf.write("\2\u0206\u0207\5^\60\2\u0207\u020a\3\2\2\2\u0208\u020a")
        buf.write("\5`\61\2\u0209\u0205\3\2\2\2\u0209\u0208\3\2\2\2\u020a")
        buf.write("_\3\2\2\2\u020b\u020c\7\64\2\2\u020c\u020d\5*\26\2\u020d")
        buf.write("\u020e\7\65\2\2\u020ea\3\2\2\2\u020f\u0210\7\4\2\2\u0210")
        buf.write("\u0211\5\u0082B\2\u0211\u0216\7\62\2\2\u0212\u0215\7?")
        buf.write("\2\2\u0213\u0215\5T+\2\u0214\u0212\3\2\2\2\u0214\u0213")
        buf.write("\3\2\2\2\u0215\u0218\3\2\2\2\u0216\u0214\3\2\2\2\u0216")
        buf.write("\u0217\3\2\2\2\u0217\u0219\3\2\2\2\u0218\u0216\3\2\2\2")
        buf.write("\u0219\u021a\7\63\2\2\u021ac\3\2\2\2\u021b\u022e\3\2\2")
        buf.write("\2\u021c\u021d\7\4\2\2\u021d\u021e\7\3\2\2\u021e\u021f")
        buf.write("\7\60\2\2\u021f\u0220\5*\26\2\u0220\u0221\7\61\2\2\u0221")
        buf.write("\u0222\5\u0082B\2\u0222\u0227\7\62\2\2\u0223\u0226\7?")
        buf.write("\2\2\u0224\u0226\5T+\2\u0225\u0223\3\2\2\2\u0225\u0224")
        buf.write("\3\2\2\2\u0226\u0229\3\2\2\2\u0227\u0225\3\2\2\2\u0227")
        buf.write("\u0228\3\2\2\2\u0228\u022a\3\2\2\2\u0229\u0227\3\2\2\2")
        buf.write("\u022a\u022b\7\63\2\2\u022b\u022c\5d\63\2\u022c\u022e")
        buf.write("\3\2\2\2\u022d\u021b\3\2\2\2\u022d\u021c\3\2\2\2\u022e")
        buf.write("e\3\2\2\2\u022f\u0230\7\3\2\2\u0230\u0231\7\60\2\2\u0231")
        buf.write("\u0232\5*\26\2\u0232\u0233\7\61\2\2\u0233\u0234\5\u0082")
        buf.write("B\2\u0234\u0239\7\62\2\2\u0235\u0238\7?\2\2\u0236\u0238")
        buf.write("\5T+\2\u0237\u0235\3\2\2\2\u0237\u0236\3\2\2\2\u0238\u023b")
        buf.write("\3\2\2\2\u0239\u0237\3\2\2\2\u0239\u023a\3\2\2\2\u023a")
        buf.write("\u023c\3\2\2\2\u023b\u0239\3\2\2\2\u023c\u0240\7\63\2")
        buf.write("\2\u023d\u023f\7?\2\2\u023e\u023d\3\2\2\2\u023f\u0242")
        buf.write("\3\2\2\2\u0240\u023e\3\2\2\2\u0240\u0241\3\2\2\2\u0241")
        buf.write("\u0243\3\2\2\2\u0242\u0240\3\2\2\2\u0243\u0247\5d\63\2")
        buf.write("\u0244\u0246\7?\2\2\u0245\u0244\3\2\2\2\u0246\u0249\3")
        buf.write("\2\2\2\u0247\u0245\3\2\2\2\u0247\u0248\3\2\2\2\u0248\u024b")
        buf.write("\3\2\2\2\u0249\u0247\3\2\2\2\u024a\u024c\5b\62\2\u024b")
        buf.write("\u024a\3\2\2\2\u024b\u024c\3\2\2\2\u024cg\3\2\2\2\u024d")
        buf.write("\u024e\7\66\2\2\u024e\u024f\7-\2\2\u024f\u0250\7\66\2")
        buf.write("\2\u0250\u0251\7/\2\2\u0251\u0252\7\23\2\2\u0252\u0253")
        buf.write("\5*\26\2\u0253i\3\2\2\2\u0254\u0257\5V,\2\u0255\u0257")
        buf.write("\5@!\2\u0256\u0254\3\2\2\2\u0256\u0255\3\2\2\2\u0257\u0258")
        buf.write("\3\2\2\2\u0258\u0259\7.\2\2\u0259\u025a\5*\26\2\u025a")
        buf.write("\u025b\7.\2\2\u025b\u025c\5V,\2\u025ck\3\2\2\2\u025d\u025e")
        buf.write("\5*\26\2\u025em\3\2\2\2\u025f\u0263\7\5\2\2\u0260\u0264")
        buf.write("\5l\67\2\u0261\u0264\5j\66\2\u0262\u0264\5h\65\2\u0263")
        buf.write("\u0260\3\2\2\2\u0263\u0261\3\2\2\2\u0263\u0262\3\2\2\2")
        buf.write("\u0264\u0265\3\2\2\2\u0265\u0266\5\u0082B\2\u0266\u026b")
        buf.write("\7\62\2\2\u0267\u026a\7?\2\2\u0268\u026a\5T+\2\u0269\u0267")
        buf.write("\3\2\2\2\u0269\u0268\3\2\2\2\u026a\u026d\3\2\2\2\u026b")
        buf.write("\u0269\3\2\2\2\u026b\u026c\3\2\2\2\u026c\u026e\3\2\2\2")
        buf.write("\u026d\u026b\3\2\2\2\u026e\u026f\7\63\2\2\u026fo\3\2\2")
        buf.write("\2\u0270\u0271\7\22\2\2\u0271q\3\2\2\2\u0272\u0273\7\21")
        buf.write("\2\2\u0273s\3\2\2\2\u0274\u0275\5Z.\2\u0275\u0276\7+\2")
        buf.write("\2\u0276\u0279\3\2\2\2\u0277\u0279\3\2\2\2\u0278\u0274")
        buf.write("\3\2\2\2\u0278\u0277\3\2\2\2\u0279\u027a\3\2\2\2\u027a")
        buf.write("\u027b\7\66\2\2\u027b\u027e\7\60\2\2\u027c\u027f\5(\25")
        buf.write("\2\u027d\u027f\3\2\2\2\u027e\u027c\3\2\2\2\u027e\u027d")
        buf.write("\3\2\2\2\u027f\u0280\3\2\2\2\u0280\u0281\7\61\2\2\u0281")
        buf.write("u\3\2\2\2\u0282\u0283\7\6\2\2\u0283\u0286\5\u0082B\2\u0284")
        buf.write("\u0287\5*\26\2\u0285\u0287\3\2\2\2\u0286\u0284\3\2\2\2")
        buf.write("\u0286\u0285\3\2\2\2\u0287w\3\2\2\2\u0288\u028c\7.\2\2")
        buf.write("\u0289\u028b\7?\2\2\u028a\u0289\3\2\2\2\u028b\u028e\3")
        buf.write("\2\2\2\u028c\u028a\3\2\2\2\u028c\u028d\3\2\2\2\u028d\u0295")
        buf.write("\3\2\2\2\u028e\u028c\3\2\2\2\u028f\u0291\7?\2\2\u0290")
        buf.write("\u028f\3\2\2\2\u0291\u0292\3\2\2\2\u0292\u0290\3\2\2\2")
        buf.write("\u0292\u0293\3\2\2\2\u0293\u0295\3\2\2\2\u0294\u0288\3")
        buf.write("\2\2\2\u0294\u0290\3\2\2\2\u0295y\3\2\2\2\u0296\u0297")
        buf.write("\7\66\2\2\u0297\u0298\5\b\5\2\u0298{\3\2\2\2\u0299\u029b")
        buf.write("\7\66\2\2\u029a\u029c\5\b\5\2\u029b\u029a\3\2\2\2\u029b")
        buf.write("\u029c\3\2\2\2\u029c}\3\2\2\2\u029d\u029e\5|?\2\u029e")
        buf.write("\u029f\7-\2\2\u029f\u02a0\5~@\2\u02a0\u02a3\3\2\2\2\u02a1")
        buf.write("\u02a3\5|?\2\u02a2\u029d\3\2\2\2\u02a2\u02a1\3\2\2\2\u02a3")
        buf.write("\177\3\2\2\2\u02a4\u02a5\7\66\2\2\u02a5\u02a6\7\60\2\2")
        buf.write("\u02a6\u02a7\5~@\2\u02a7\u02a9\7\61\2\2\u02a8\u02aa\5")
        buf.write("\b\5\2\u02a9\u02a8\3\2\2\2\u02a9\u02aa\3\2\2\2\u02aa\u0081")
        buf.write("\3\2\2\2\u02ab\u02ad\7?\2\2\u02ac\u02ab\3\2\2\2\u02ad")
        buf.write("\u02b0\3\2\2\2\u02ae\u02ac\3\2\2\2\u02ae\u02af\3\2\2\2")
        buf.write("\u02af\u0083\3\2\2\2\u02b0\u02ae\3\2\2\2J\u0087\u008d")
        buf.write("\u008f\u009e\u00ab\u00b3\u00c2\u00c8\u00cf\u00d8\u00e1")
        buf.write("\u00ea\u00f4\u00fc\u0107\u010c\u010f\u0114\u011b\u0125")
        buf.write("\u0130\u013b\u0146\u0151\u0157\u0163\u0167\u0175\u0179")
        buf.write("\u0180\u018b\u018f\u0195\u0199\u019f\u01a1\u01ac\u01b5")
        buf.write("\u01bf\u01c3\u01c9\u01cb\u01dc\u01e3\u01f1\u01fe\u0203")
        buf.write("\u0209\u0214\u0216\u0225\u0227\u022d\u0237\u0239\u0240")
        buf.write("\u0247\u024b\u0256\u0263\u0269\u026b\u0278\u027e\u0286")
        buf.write("\u028c\u0292\u0294\u029b\u02a2\u02a9\u02ae")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'.'", "':'", "','", "';'", "':='", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQUAL", "UNEQUAL", "LT", "LTE", "GT", "GTE", 
                      "AND", "OR", "NOT", "ASSIGN", "ADD_ASS", "SUB_ASS", 
                      "MUL_ASS", "DIV_ASS", "MOD_ASS", "DOT", "COLON", "COMMA", 
                      "SEMICOLON", "COLONEQUAL", "LP", "RP", "LCP", "RCP", 
                      "LSP", "RSP", "ID", "INT_LIT", "BIN_LIT", "OCT_LIT", 
                      "HEX_LIT", "FLOAT_LIT", "STRING_LIT", "BOOL_LIT", 
                      "NIL_LIT", "NEWLINE", "WS", "COMMENT_LINE", "COMMENT", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_declared = 1
    RULE_liter = 2
    RULE_all_type = 3
    RULE_basic_type = 4
    RULE_statement = 5
    RULE_list_liter = 6
    RULE_list_literal_noempty = 7
    RULE_list_array_type_lit = 8
    RULE_array_type_lit = 9
    RULE_array_type = 10
    RULE_struct_literal = 11
    RULE_list_ele_lit = 12
    RULE_list_ele = 13
    RULE_arr_liter = 14
    RULE_dim_lit = 15
    RULE_dim = 16
    RULE_arr_ele = 17
    RULE_list_arr_ele = 18
    RULE_list_expr = 19
    RULE_expr = 20
    RULE_expr1 = 21
    RULE_expr2 = 22
    RULE_expr3 = 23
    RULE_expr4 = 24
    RULE_expr5 = 25
    RULE_expr6 = 26
    RULE_expr7 = 27
    RULE_functcall = 28
    RULE_functcall_noempty = 29
    RULE_const_decl = 30
    RULE_var_decl = 31
    RULE_func_decl = 32
    RULE_param_lit = 33
    RULE_param = 34
    RULE_list_ID = 35
    RULE_method_decl = 36
    RULE_struct_decl = 37
    RULE_struct_body = 38
    RULE_struct_member = 39
    RULE_interface_decl = 40
    RULE_list_statement = 41
    RULE_ass_statement = 42
    RULE_operator = 43
    RULE_list_assignment_lhs = 44
    RULE_assignment_lhs = 45
    RULE_list_array_index = 46
    RULE_array_index = 47
    RULE_else_statement = 48
    RULE_elif_statement = 49
    RULE_if_statement = 50
    RULE_range_loop = 51
    RULE_init_loop = 52
    RULE_basic_loop = 53
    RULE_for_statement = 54
    RULE_break_statement = 55
    RULE_continue_statement = 56
    RULE_call_statement = 57
    RULE_return_statement = 58
    RULE_end_statement = 59
    RULE_struct_statements = 60
    RULE_method_param = 61
    RULE_method_param_lit = 62
    RULE_method_statement = 63
    RULE_ignore = 64

    ruleNames =  [ "program", "declared", "liter", "all_type", "basic_type", 
                   "statement", "list_liter", "list_literal_noempty", "list_array_type_lit", 
                   "array_type_lit", "array_type", "struct_literal", "list_ele_lit", 
                   "list_ele", "arr_liter", "dim_lit", "dim", "arr_ele", 
                   "list_arr_ele", "list_expr", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "functcall", 
                   "functcall_noempty", "const_decl", "var_decl", "func_decl", 
                   "param_lit", "param", "list_ID", "method_decl", "struct_decl", 
                   "struct_body", "struct_member", "interface_decl", "list_statement", 
                   "ass_statement", "operator", "list_assignment_lhs", "assignment_lhs", 
                   "list_array_index", "array_index", "else_statement", 
                   "elif_statement", "if_statement", "range_loop", "init_loop", 
                   "basic_loop", "for_statement", "break_statement", "continue_statement", 
                   "call_statement", "return_statement", "end_statement", 
                   "struct_statements", "method_param", "method_param_lit", 
                   "method_statement", "ignore" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    ADD=21
    SUB=22
    MUL=23
    DIV=24
    MOD=25
    EQUAL=26
    UNEQUAL=27
    LT=28
    LTE=29
    GT=30
    GTE=31
    AND=32
    OR=33
    NOT=34
    ASSIGN=35
    ADD_ASS=36
    SUB_ASS=37
    MUL_ASS=38
    DIV_ASS=39
    MOD_ASS=40
    DOT=41
    COLON=42
    COMMA=43
    SEMICOLON=44
    COLONEQUAL=45
    LP=46
    RP=47
    LCP=48
    RCP=49
    LSP=50
    RSP=51
    ID=52
    INT_LIT=53
    BIN_LIT=54
    OCT_LIT=55
    HEX_LIT=56
    FLOAT_LIT=57
    STRING_LIT=58
    BOOL_LIT=59
    NIL_LIT=60
    NEWLINE=61
    WS=62
    COMMENT_LINE=63
    COMMENT=64
    ERROR_CHAR=65
    UNCLOSE_STRING=66
    ILLEGAL_ESCAPE=67

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclaredContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclaredContext,i)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 130
                self.match(MiniGoParser.NEWLINE)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
            self.declared()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.NEWLINE))) != 0):
                self.state = 139
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                    self.state = 137
                    self.declared()
                    pass
                elif token in [MiniGoParser.NEWLINE]:
                    self.state = 138
                    self.match(MiniGoParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 144
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared" ):
                return visitor.visitDeclared(self)
            else:
                return visitor.visitChildren(self)




    def declared(self):

        localctx = MiniGoParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declared)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.var_decl()
                self.state = 147
                self.match(MiniGoParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.const_decl()
                self.state = 150
                self.match(MiniGoParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 152
                self.func_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 153
                self.method_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 154
                self.struct_decl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 155
                self.interface_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def BIN_LIT(self):
            return self.getToken(MiniGoParser.BIN_LIT, 0)

        def OCT_LIT(self):
            return self.getToken(MiniGoParser.OCT_LIT, 0)

        def HEX_LIT(self):
            return self.getToken(MiniGoParser.HEX_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def arr_liter(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_literContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_liter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiter" ):
                return visitor.visitLiter(self)
            else:
                return visitor.visitChildren(self)




    def liter(self):

        localctx = MiniGoParser.LiterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_liter)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.BIN_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.match(MiniGoParser.BIN_LIT)
                pass
            elif token in [MiniGoParser.OCT_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.match(MiniGoParser.OCT_LIT)
                pass
            elif token in [MiniGoParser.HEX_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 161
                self.match(MiniGoParser.HEX_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 162
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 163
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 164
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 8)
                self.state = 165
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 9)
                self.state = 166
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.LSP]:
                self.enterOuterAlt(localctx, 10)
                self.state = 167
                self.arr_liter()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 11)
                self.state = 168
                self.struct_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def list_array_type_lit(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_type_litContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_all_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_type" ):
                return visitor.visitAll_type(self)
            else:
                return visitor.visitChildren(self)




    def all_type(self):

        localctx = MiniGoParser.All_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_all_type)
        try:
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 174
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.LSP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 175
                self.list_array_type_lit()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 176
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_type" ):
                return visitor.visitBasic_type(self)
            else:
                return visitor.visitChildren(self)




    def basic_type(self):

        localctx = MiniGoParser.Basic_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_basic_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def end_statement(self):
            return self.getTypedRuleContext(MiniGoParser.End_statementContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def ass_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Ass_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statementContext,0)


        def struct_statements(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_statementsContext,0)


        def method_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Method_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 181
                self.var_decl()
                pass

            elif la_ == 2:
                self.state = 182
                self.const_decl()
                pass

            elif la_ == 3:
                self.state = 183
                self.ass_statement()
                pass

            elif la_ == 4:
                self.state = 184
                self.if_statement()
                pass

            elif la_ == 5:
                self.state = 185
                self.for_statement()
                pass

            elif la_ == 6:
                self.state = 186
                self.break_statement()
                pass

            elif la_ == 7:
                self.state = 187
                self.continue_statement()
                pass

            elif la_ == 8:
                self.state = 188
                self.call_statement()
                pass

            elif la_ == 9:
                self.state = 189
                self.return_statement()
                pass

            elif la_ == 10:
                self.state = 190
                self.struct_statements()
                pass

            elif la_ == 11:
                self.state = 191
                self.method_statement()
                pass


            self.state = 194
            self.end_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_literContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_literal_noempty(self):
            return self.getTypedRuleContext(MiniGoParser.List_literal_noemptyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_liter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_liter" ):
                return visitor.visitList_liter(self)
            else:
                return visitor.visitChildren(self)




    def list_liter(self):

        localctx = MiniGoParser.List_literContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_list_liter)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.list_literal_noempty()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_literal_noemptyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def liter(self):
            return self.getTypedRuleContext(MiniGoParser.LiterContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_liter(self):
            return self.getTypedRuleContext(MiniGoParser.List_literContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_literal_noempty

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_literal_noempty" ):
                return visitor.visitList_literal_noempty(self)
            else:
                return visitor.visitChildren(self)




    def list_literal_noempty(self):

        localctx = MiniGoParser.List_literal_noemptyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_list_literal_noempty)
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.liter()
                self.state = 201
                self.match(MiniGoParser.COMMA)
                self.state = 202
                self.list_liter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.liter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_array_type_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Array_type_litContext,0)


        def basic_type(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_array_type_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_array_type_lit" ):
                return visitor.visitList_array_type_lit(self)
            else:
                return visitor.visitChildren(self)




    def list_array_type_lit(self):

        localctx = MiniGoParser.List_array_type_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list_array_type_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.array_type_lit()
            self.state = 208
            self.basic_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_type_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def array_type_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Array_type_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type_lit" ):
                return visitor.visitArray_type_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_type_lit(self):

        localctx = MiniGoParser.Array_type_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_type_lit)
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.array_type()
                self.state = 211
                self.array_type_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.array_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSP(self):
            return self.getToken(MiniGoParser.LSP, 0)

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def RSP(self):
            return self.getToken(MiniGoParser.RSP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(MiniGoParser.LSP)
            self.state = 217
            self.match(MiniGoParser.INT_LIT)
            self.state = 218
            self.match(MiniGoParser.RSP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCP(self):
            return self.getToken(MiniGoParser.LCP, 0)

        def RCP(self):
            return self.getToken(MiniGoParser.RCP, 0)

        def list_ele_lit(self):
            return self.getTypedRuleContext(MiniGoParser.List_ele_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(MiniGoParser.ID)
            self.state = 221
            self.match(MiniGoParser.LCP)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 222
                self.list_ele_lit()


            self.state = 225
            self.match(MiniGoParser.RCP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_ele_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_ele(self):
            return self.getTypedRuleContext(MiniGoParser.List_eleContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_ele_lit(self):
            return self.getTypedRuleContext(MiniGoParser.List_ele_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_ele_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_ele_lit" ):
                return visitor.visitList_ele_lit(self)
            else:
                return visitor.visitChildren(self)




    def list_ele_lit(self):

        localctx = MiniGoParser.List_ele_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_list_ele_lit)
        try:
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.list_ele()
                self.state = 228
                self.match(MiniGoParser.COMMA)
                self.state = 229
                self.list_ele_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.list_ele()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_eleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_ele

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_ele" ):
                return visitor.visitList_ele(self)
            else:
                return visitor.visitChildren(self)




    def list_ele(self):

        localctx = MiniGoParser.List_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_list_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(MiniGoParser.ID)
            self.state = 235
            self.match(MiniGoParser.COLON)
            self.state = 236
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_literContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dim_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Dim_litContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def LCP(self):
            return self.getToken(MiniGoParser.LCP, 0)

        def RCP(self):
            return self.getToken(MiniGoParser.RCP, 0)

        def list_arr_ele(self):
            return self.getTypedRuleContext(MiniGoParser.List_arr_eleContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_liter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_liter" ):
                return visitor.visitArr_liter(self)
            else:
                return visitor.visitChildren(self)




    def arr_liter(self):

        localctx = MiniGoParser.Arr_literContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_arr_liter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.dim_lit()
            self.state = 239
            self.all_type()
            self.state = 240
            self.match(MiniGoParser.LCP)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.LCP) | (1 << MiniGoParser.LSP) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 241
                self.list_arr_ele()


            self.state = 244
            self.match(MiniGoParser.RCP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dim_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dim(self):
            return self.getTypedRuleContext(MiniGoParser.DimContext,0)


        def dim_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Dim_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_dim_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDim_lit" ):
                return visitor.visitDim_lit(self)
            else:
                return visitor.visitChildren(self)




    def dim_lit(self):

        localctx = MiniGoParser.Dim_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_dim_lit)
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.dim()
                self.state = 247
                self.dim_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.dim()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSP(self):
            return self.getToken(MiniGoParser.LSP, 0)

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def RSP(self):
            return self.getToken(MiniGoParser.RSP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dim

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDim" ):
                return visitor.visitDim(self)
            else:
                return visitor.visitChildren(self)




    def dim(self):

        localctx = MiniGoParser.DimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_dim)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(MiniGoParser.LSP)
            self.state = 253
            self.match(MiniGoParser.INT_LIT)
            self.state = 254
            self.match(MiniGoParser.RSP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_eleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def liter(self):
            return self.getTypedRuleContext(MiniGoParser.LiterContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCP(self):
            return self.getToken(MiniGoParser.LCP, 0)

        def RCP(self):
            return self.getToken(MiniGoParser.RCP, 0)

        def list_arr_ele(self):
            return self.getTypedRuleContext(MiniGoParser.List_arr_eleContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_ele

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_ele" ):
                return visitor.visitArr_ele(self)
            else:
                return visitor.visitChildren(self)




    def arr_ele(self):

        localctx = MiniGoParser.Arr_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_arr_ele)
        self._la = 0 # Token type
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.liter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.struct_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.match(MiniGoParser.ID)
                self.state = 259
                self.match(MiniGoParser.LCP)
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.LCP) | (1 << MiniGoParser.LSP) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 260
                    self.list_arr_ele()


                self.state = 263
                self.match(MiniGoParser.RCP)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 264
                self.match(MiniGoParser.LCP)
                self.state = 266
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.LCP) | (1 << MiniGoParser.LSP) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 265
                    self.list_arr_ele()


                self.state = 268
                self.match(MiniGoParser.RCP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_arr_eleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr_ele(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_eleContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_arr_ele(self):
            return self.getTypedRuleContext(MiniGoParser.List_arr_eleContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_arr_ele

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_arr_ele" ):
                return visitor.visitList_arr_ele(self)
            else:
                return visitor.visitChildren(self)




    def list_arr_ele(self):

        localctx = MiniGoParser.List_arr_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_list_arr_ele)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.arr_ele()
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 272
                self.match(MiniGoParser.COMMA)
                self.state = 273
                self.list_arr_ele()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr" ):
                return visitor.visitList_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_expr(self):

        localctx = MiniGoParser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_list_expr)
        try:
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.expr(0)
                self.state = 277
                self.match(MiniGoParser.COMMA)
                self.state = 278
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 286
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 287
                    self.match(MiniGoParser.OR)
                    self.state = 288
                    self.expr1(0) 
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 302
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 297
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 298
                    self.match(MiniGoParser.AND)
                    self.state = 299
                    self.expr2(0) 
                self.state = 304
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def UNEQUAL(self):
            return self.getToken(MiniGoParser.UNEQUAL, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LTE(self):
            return self.getToken(MiniGoParser.LTE, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GTE(self):
            return self.getToken(MiniGoParser.GTE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 308
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 309
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.UNEQUAL) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LTE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GTE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 310
                    self.expr3(0) 
                self.state = 315
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 319
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 320
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 321
                    self.expr4(0) 
                self.state = 326
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 335
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 330
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 331
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 332
                    self.expr5() 
                self.state = 337
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 339
                self.expr(0)
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LP, MiniGoParser.LSP, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.expr6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def LSP(self):
            return self.getToken(MiniGoParser.LSP, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RSP(self):
            return self.getToken(MiniGoParser.RSP, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 357
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 346
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 353
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LSP]:
                        self.state = 347
                        self.match(MiniGoParser.LSP)
                        self.state = 348
                        self.expr(0)
                        self.state = 349
                        self.match(MiniGoParser.RSP)
                        pass
                    elif token in [MiniGoParser.DOT]:
                        self.state = 351
                        self.match(MiniGoParser.DOT)
                        self.state = 352
                        self.expr(0)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 359
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def liter(self):
            return self.getTypedRuleContext(MiniGoParser.LiterContext,0)


        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def functcall(self):
            return self.getTypedRuleContext(MiniGoParser.FunctcallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = MiniGoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr7)
        try:
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.liter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
                self.match(MiniGoParser.LP)
                self.state = 362
                self.expr(0)
                self.state = 363
                self.match(MiniGoParser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 365
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 366
                self.match(MiniGoParser.ID)
                self.state = 367
                self.match(MiniGoParser.LP)
                self.state = 368
                self.functcall()
                self.state = 369
                self.match(MiniGoParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctcallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functcall_noempty(self):
            return self.getTypedRuleContext(MiniGoParser.Functcall_noemptyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_functcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctcall" ):
                return visitor.visitFunctcall(self)
            else:
                return visitor.visitChildren(self)




    def functcall(self):

        localctx = MiniGoParser.FunctcallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_functcall)
        try:
            self.state = 375
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LP, MiniGoParser.LSP, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.functcall_noempty()
                pass
            elif token in [MiniGoParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Functcall_noemptyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def functcall_noempty(self):
            return self.getTypedRuleContext(MiniGoParser.Functcall_noemptyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_functcall_noempty

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctcall_noempty" ):
                return visitor.visitFunctcall_noempty(self)
            else:
                return visitor.visitChildren(self)




    def functcall_noempty(self):

        localctx = MiniGoParser.Functcall_noemptyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_functcall_noempty)
        try:
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
                self.expr(0)
                self.state = 379
                self.match(MiniGoParser.COMMA)
                self.state = 380
                self.functcall_noempty()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(MiniGoParser.CONST)
            self.state = 385
            self.match(MiniGoParser.ID)
            self.state = 386
            self.match(MiniGoParser.ASSIGN)
            self.state = 387
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(MiniGoParser.VAR)
            self.state = 390
            self.match(MiniGoParser.ID)
            self.state = 397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 391
                self.all_type()
                pass

            elif la_ == 2:
                self.state = 393
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSP) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 392
                    self.all_type()


                self.state = 395
                self.match(MiniGoParser.ASSIGN)
                self.state = 396
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def LCP(self):
            return self.getToken(MiniGoParser.LCP, 0)

        def RCP(self):
            return self.getToken(MiniGoParser.RCP, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def param_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Param_litContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def list_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.List_statementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.List_statementContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(MiniGoParser.FUNC)
            self.state = 400
            self.match(MiniGoParser.ID)
            self.state = 401
            self.match(MiniGoParser.LP)
            self.state = 403
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 402
                self.param_lit()


            self.state = 405
            self.match(MiniGoParser.RP)
            self.state = 407
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSP) | (1 << MiniGoParser.ID))) != 0):
                self.state = 406
                self.all_type()


            self.state = 409
            self.ignore()
            self.state = 410
            self.match(MiniGoParser.LCP)
            self.state = 415
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.NEWLINE))) != 0):
                self.state = 413
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.NEWLINE]:
                    self.state = 411
                    self.match(MiniGoParser.NEWLINE)
                    pass
                elif token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                    self.state = 412
                    self.list_statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 417
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 418
            self.match(MiniGoParser.RCP)
            self.state = 419
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MiniGoParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def param_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Param_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_lit" ):
                return visitor.visitParam_lit(self)
            else:
                return visitor.visitChildren(self)




    def param_lit(self):

        localctx = MiniGoParser.Param_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_param_lit)
        try:
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.param()
                self.state = 422
                self.match(MiniGoParser.COMMA)
                self.state = 423
                self.param_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_ID(self):
            return self.getTypedRuleContext(MiniGoParser.List_IDContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.list_ID()
            self.state = 429
            self.all_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_IDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_ID(self):
            return self.getTypedRuleContext(MiniGoParser.List_IDContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_ID

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_ID" ):
                return visitor.visitList_ID(self)
            else:
                return visitor.visitChildren(self)




    def list_ID(self):

        localctx = MiniGoParser.List_IDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_list_ID)
        try:
            self.state = 435
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 431
                self.match(MiniGoParser.ID)
                self.state = 432
                self.match(MiniGoParser.COMMA)
                self.state = 433
                self.list_ID()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LP)
            else:
                return self.getToken(MiniGoParser.LP, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RP)
            else:
                return self.getToken(MiniGoParser.RP, i)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def LCP(self):
            return self.getToken(MiniGoParser.LCP, 0)

        def RCP(self):
            return self.getToken(MiniGoParser.RCP, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def param_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Param_litContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def list_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.List_statementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.List_statementContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = MiniGoParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(MiniGoParser.FUNC)
            self.state = 438
            self.match(MiniGoParser.LP)
            self.state = 439
            self.match(MiniGoParser.ID)
            self.state = 440
            self.match(MiniGoParser.ID)
            self.state = 441
            self.match(MiniGoParser.RP)
            self.state = 442
            self.match(MiniGoParser.ID)
            self.state = 443
            self.match(MiniGoParser.LP)
            self.state = 445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 444
                self.param_lit()


            self.state = 447
            self.match(MiniGoParser.RP)
            self.state = 449
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSP) | (1 << MiniGoParser.ID))) != 0):
                self.state = 448
                self.all_type()


            self.state = 451
            self.ignore()
            self.state = 452
            self.match(MiniGoParser.LCP)
            self.state = 457
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.NEWLINE))) != 0):
                self.state = 455
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.NEWLINE]:
                    self.state = 453
                    self.match(MiniGoParser.NEWLINE)
                    pass
                elif token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                    self.state = 454
                    self.list_statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 459
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 460
            self.match(MiniGoParser.RCP)
            self.state = 461
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LCP(self):
            return self.getToken(MiniGoParser.LCP, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RCP(self):
            return self.getToken(MiniGoParser.RCP, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_decl" ):
                return visitor.visitStruct_decl(self)
            else:
                return visitor.visitChildren(self)




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.match(MiniGoParser.TYPE)
            self.state = 464
            self.match(MiniGoParser.ID)
            self.state = 465
            self.match(MiniGoParser.STRUCT)
            self.state = 466
            self.match(MiniGoParser.LCP)
            self.state = 467
            self.list_statement()
            self.state = 468
            self.match(MiniGoParser.RCP)
            self.state = 469
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Struct_memberContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Struct_memberContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_body" ):
                return visitor.visitStruct_body(self)
            else:
                return visitor.visitChildren(self)




    def struct_body(self):

        localctx = MiniGoParser.Struct_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_struct_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.FUNC or _la==MiniGoParser.ID:
                self.state = 471
                self.struct_member()
                self.state = 476
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_memberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_statements(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_statementsContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_member" ):
                return visitor.visitStruct_member(self)
            else:
                return visitor.visitChildren(self)




    def struct_member(self):

        localctx = MiniGoParser.Struct_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_struct_member)
        try:
            self.state = 481
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.struct_statements()
                self.state = 478
                self.match(MiniGoParser.SEMICOLON)
                pass
            elif token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 480
                self.method_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LCP(self):
            return self.getToken(MiniGoParser.LCP, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RCP(self):
            return self.getToken(MiniGoParser.RCP, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_decl" ):
                return visitor.visitInterface_decl(self)
            else:
                return visitor.visitChildren(self)




    def interface_decl(self):

        localctx = MiniGoParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(MiniGoParser.TYPE)
            self.state = 484
            self.match(MiniGoParser.ID)
            self.state = 485
            self.match(MiniGoParser.INTERFACE)
            self.state = 486
            self.match(MiniGoParser.LCP)
            self.state = 487
            self.list_statement()
            self.state = 488
            self.match(MiniGoParser.RCP)
            self.state = 489
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement" ):
                return visitor.visitList_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_statement(self):

        localctx = MiniGoParser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_list_statement)
        try:
            self.state = 495
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 491
                self.statement()
                self.state = 492
                self.list_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 494
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ass_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_assignment_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.List_assignment_lhsContext,0)


        def operator(self):
            return self.getTypedRuleContext(MiniGoParser.OperatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ass_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAss_statement" ):
                return visitor.visitAss_statement(self)
            else:
                return visitor.visitChildren(self)




    def ass_statement(self):

        localctx = MiniGoParser.Ass_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_ass_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.list_assignment_lhs()
            self.state = 498
            self.operator()
            self.state = 499
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLONEQUAL(self):
            return self.getToken(MiniGoParser.COLONEQUAL, 0)

        def ADD_ASS(self):
            return self.getToken(MiniGoParser.ADD_ASS, 0)

        def SUB_ASS(self):
            return self.getToken(MiniGoParser.SUB_ASS, 0)

        def MUL_ASS(self):
            return self.getToken(MiniGoParser.MUL_ASS, 0)

        def DIV_ASS(self):
            return self.getToken(MiniGoParser.DIV_ASS, 0)

        def MOD_ASS(self):
            return self.getToken(MiniGoParser.MOD_ASS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = MiniGoParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ADD_ASS) | (1 << MiniGoParser.SUB_ASS) | (1 << MiniGoParser.MUL_ASS) | (1 << MiniGoParser.DIV_ASS) | (1 << MiniGoParser.MOD_ASS) | (1 << MiniGoParser.COLONEQUAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_assignment_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_lhsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def list_assignment_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.List_assignment_lhsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_assignment_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_assignment_lhs" ):
                return visitor.visitList_assignment_lhs(self)
            else:
                return visitor.visitChildren(self)




    def list_assignment_lhs(self):

        localctx = MiniGoParser.List_assignment_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_list_assignment_lhs)
        try:
            self.state = 508
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 503
                self.assignment_lhs()
                self.state = 504
                self.match(MiniGoParser.DOT)
                self.state = 505
                self.list_assignment_lhs()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 507
                self.assignment_lhs()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def list_array_index(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_indexContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_lhs" ):
                return visitor.visitAssignment_lhs(self)
            else:
                return visitor.visitChildren(self)




    def assignment_lhs(self):

        localctx = MiniGoParser.Assignment_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_assignment_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.match(MiniGoParser.ID)
            self.state = 513
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LSP]:
                self.state = 511
                self.list_array_index()
                pass
            elif token in [MiniGoParser.ADD_ASS, MiniGoParser.SUB_ASS, MiniGoParser.MUL_ASS, MiniGoParser.DIV_ASS, MiniGoParser.MOD_ASS, MiniGoParser.DOT, MiniGoParser.COLONEQUAL]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_array_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_index(self):
            return self.getTypedRuleContext(MiniGoParser.Array_indexContext,0)


        def list_array_index(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_indexContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_array_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_array_index" ):
                return visitor.visitList_array_index(self)
            else:
                return visitor.visitChildren(self)




    def list_array_index(self):

        localctx = MiniGoParser.List_array_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_list_array_index)
        try:
            self.state = 519
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 515
                self.array_index()
                self.state = 516
                self.list_array_index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 518
                self.array_index()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSP(self):
            return self.getToken(MiniGoParser.LSP, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RSP(self):
            return self.getToken(MiniGoParser.RSP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_index" ):
                return visitor.visitArray_index(self)
            else:
                return visitor.visitChildren(self)




    def array_index(self):

        localctx = MiniGoParser.Array_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_array_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.match(MiniGoParser.LSP)
            self.state = 522
            self.expr(0)
            self.state = 523
            self.match(MiniGoParser.RSP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def LCP(self):
            return self.getToken(MiniGoParser.LCP, 0)

        def RCP(self):
            return self.getToken(MiniGoParser.RCP, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def list_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.List_statementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.List_statementContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = MiniGoParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_else_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            self.match(MiniGoParser.ELSE)
            self.state = 526
            self.ignore()
            self.state = 527
            self.match(MiniGoParser.LCP)
            self.state = 532
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.NEWLINE))) != 0):
                self.state = 530
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.NEWLINE]:
                    self.state = 528
                    self.match(MiniGoParser.NEWLINE)
                    pass
                elif token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                    self.state = 529
                    self.list_statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 534
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 535
            self.match(MiniGoParser.RCP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def LCP(self):
            return self.getToken(MiniGoParser.LCP, 0)

        def RCP(self):
            return self.getToken(MiniGoParser.RCP, 0)

        def elif_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Elif_statementContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def list_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.List_statementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.List_statementContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elif_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_statement" ):
                return visitor.visitElif_statement(self)
            else:
                return visitor.visitChildren(self)




    def elif_statement(self):

        localctx = MiniGoParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_elif_statement)
        self._la = 0 # Token type
        try:
            self.state = 555
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 538
                self.match(MiniGoParser.ELSE)
                self.state = 539
                self.match(MiniGoParser.IF)
                self.state = 540
                self.match(MiniGoParser.LP)
                self.state = 541
                self.expr(0)
                self.state = 542
                self.match(MiniGoParser.RP)
                self.state = 543
                self.ignore()
                self.state = 544
                self.match(MiniGoParser.LCP)
                self.state = 549
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.NEWLINE))) != 0):
                    self.state = 547
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.NEWLINE]:
                        self.state = 545
                        self.match(MiniGoParser.NEWLINE)
                        pass
                    elif token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                        self.state = 546
                        self.list_statement()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 551
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 552
                self.match(MiniGoParser.RCP)
                self.state = 553
                self.elif_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def LCP(self):
            return self.getToken(MiniGoParser.LCP, 0)

        def RCP(self):
            return self.getToken(MiniGoParser.RCP, 0)

        def elif_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Elif_statementContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def list_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.List_statementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.List_statementContext,i)


        def else_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Else_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 557
            self.match(MiniGoParser.IF)
            self.state = 558
            self.match(MiniGoParser.LP)
            self.state = 559
            self.expr(0)
            self.state = 560
            self.match(MiniGoParser.RP)
            self.state = 561
            self.ignore()
            self.state = 562
            self.match(MiniGoParser.LCP)
            self.state = 567
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.NEWLINE))) != 0):
                self.state = 565
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.NEWLINE]:
                    self.state = 563
                    self.match(MiniGoParser.NEWLINE)
                    pass
                elif token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                    self.state = 564
                    self.list_statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 569
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 570
            self.match(MiniGoParser.RCP)
            self.state = 574
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 571
                    self.match(MiniGoParser.NEWLINE) 
                self.state = 576
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

            self.state = 577
            self.elif_statement()
            self.state = 581
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 578
                    self.match(MiniGoParser.NEWLINE) 
                self.state = 583
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

            self.state = 585
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 584
                self.else_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def COLONEQUAL(self):
            return self.getToken(MiniGoParser.COLONEQUAL, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_range_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_loop" ):
                return visitor.visitRange_loop(self)
            else:
                return visitor.visitChildren(self)




    def range_loop(self):

        localctx = MiniGoParser.Range_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_range_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            self.match(MiniGoParser.ID)
            self.state = 588
            self.match(MiniGoParser.COMMA)
            self.state = 589
            self.match(MiniGoParser.ID)
            self.state = 590
            self.match(MiniGoParser.COLONEQUAL)
            self.state = 591
            self.match(MiniGoParser.RANGE)
            self.state = 592
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def ass_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Ass_statementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Ass_statementContext,i)


        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_init_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_loop" ):
                return visitor.visitInit_loop(self)
            else:
                return visitor.visitChildren(self)




    def init_loop(self):

        localctx = MiniGoParser.Init_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_init_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 596
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 594
                self.ass_statement()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 595
                self.var_decl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 598
            self.match(MiniGoParser.SEMICOLON)
            self.state = 599
            self.expr(0)
            self.state = 600
            self.match(MiniGoParser.SEMICOLON)
            self.state = 601
            self.ass_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_loop" ):
                return visitor.visitBasic_loop(self)
            else:
                return visitor.visitChildren(self)




    def basic_loop(self):

        localctx = MiniGoParser.Basic_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_basic_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 603
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def LCP(self):
            return self.getToken(MiniGoParser.LCP, 0)

        def RCP(self):
            return self.getToken(MiniGoParser.RCP, 0)

        def basic_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_loopContext,0)


        def init_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Init_loopContext,0)


        def range_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Range_loopContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def list_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.List_statementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.List_statementContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            self.match(MiniGoParser.FOR)
            self.state = 609
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.state = 606
                self.basic_loop()
                pass

            elif la_ == 2:
                self.state = 607
                self.init_loop()
                pass

            elif la_ == 3:
                self.state = 608
                self.range_loop()
                pass


            self.state = 611
            self.ignore()
            self.state = 612
            self.match(MiniGoParser.LCP)
            self.state = 617
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.NEWLINE))) != 0):
                self.state = 615
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.NEWLINE]:
                    self.state = 613
                    self.match(MiniGoParser.NEWLINE)
                    pass
                elif token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                    self.state = 614
                    self.list_statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 619
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 620
            self.match(MiniGoParser.RCP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MiniGoParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622
            self.match(MiniGoParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MiniGoParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 624
            self.match(MiniGoParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def list_assignment_lhs(self):
            return self.getTypedRuleContext(MiniGoParser.List_assignment_lhsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 630
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.state = 626
                self.list_assignment_lhs()
                self.state = 627
                self.match(MiniGoParser.DOT)
                pass

            elif la_ == 2:
                pass


            self.state = 632
            self.match(MiniGoParser.ID)
            self.state = 633
            self.match(MiniGoParser.LP)
            self.state = 636
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LP, MiniGoParser.LSP, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 634
                self.list_expr()
                pass
            elif token in [MiniGoParser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 638
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MiniGoParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 640
            self.match(MiniGoParser.RETURN)
            self.state = 641
            self.ignore()
            self.state = 644
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LP, MiniGoParser.LSP, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 642
                self.expr(0)
                pass
            elif token in [MiniGoParser.SEMICOLON, MiniGoParser.NEWLINE]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class End_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_end_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnd_statement" ):
                return visitor.visitEnd_statement(self)
            else:
                return visitor.visitChildren(self)




    def end_statement(self):

        localctx = MiniGoParser.End_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_end_statement)
        try:
            self.state = 658
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SEMICOLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 646
                self.match(MiniGoParser.SEMICOLON)
                self.state = 650
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,65,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 647
                        self.match(MiniGoParser.NEWLINE) 
                    self.state = 652
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,65,self._ctx)

                pass
            elif token in [MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 654 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 653
                        self.match(MiniGoParser.NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 656 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,66,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_statements" ):
                return visitor.visitStruct_statements(self)
            else:
                return visitor.visitChildren(self)




    def struct_statements(self):

        localctx = MiniGoParser.Struct_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_struct_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 660
            self.match(MiniGoParser.ID)
            self.state = 661
            self.all_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_param" ):
                return visitor.visitMethod_param(self)
            else:
                return visitor.visitChildren(self)




    def method_param(self):

        localctx = MiniGoParser.Method_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_method_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 663
            self.match(MiniGoParser.ID)
            self.state = 665
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSP) | (1 << MiniGoParser.ID))) != 0):
                self.state = 664
                self.all_type()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_param_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_param(self):
            return self.getTypedRuleContext(MiniGoParser.Method_paramContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def method_param_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Method_param_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_param_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_param_lit" ):
                return visitor.visitMethod_param_lit(self)
            else:
                return visitor.visitChildren(self)




    def method_param_lit(self):

        localctx = MiniGoParser.Method_param_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_method_param_lit)
        try:
            self.state = 672
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 667
                self.method_param()
                self.state = 668
                self.match(MiniGoParser.COMMA)
                self.state = 669
                self.method_param_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 671
                self.method_param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def method_param_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Method_param_litContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def all_type(self):
            return self.getTypedRuleContext(MiniGoParser.All_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_statement" ):
                return visitor.visitMethod_statement(self)
            else:
                return visitor.visitChildren(self)




    def method_statement(self):

        localctx = MiniGoParser.Method_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_method_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 674
            self.match(MiniGoParser.ID)
            self.state = 675
            self.match(MiniGoParser.LP)
            self.state = 676
            self.method_param_lit()
            self.state = 677
            self.match(MiniGoParser.RP)
            self.state = 679
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSP) | (1 << MiniGoParser.ID))) != 0):
                self.state = 678
                self.all_type()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ignore

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnore" ):
                return visitor.visitIgnore(self)
            else:
                return visitor.visitChildren(self)




    def ignore(self):

        localctx = MiniGoParser.IgnoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_ignore)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 684
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,71,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 681
                    self.match(MiniGoParser.NEWLINE) 
                self.state = 686
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,71,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[20] = self.expr_sempred
        self._predicates[21] = self.expr1_sempred
        self._predicates[22] = self.expr2_sempred
        self._predicates[23] = self.expr3_sempred
        self._predicates[24] = self.expr4_sempred
        self._predicates[26] = self.expr6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




