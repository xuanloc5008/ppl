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
        buf.write("\u0299\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\7\2\u0082\n\2\f\2")
        buf.write("\16\2\u0085\13\2\3\2\3\2\3\2\7\2\u008a\n\2\f\2\16\2\u008d")
        buf.write("\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\5\3\u009b\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\5\4\u00a7\n\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00af\n\5\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7")
        buf.write("\u00be\n\7\3\7\3\7\3\b\3\b\5\b\u00c4\n\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\5\t\u00cb\n\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\5")
        buf.write("\13\u00d4\n\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\5\r\u00dd\n")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\5\16\u00e6\n\16\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u00f6\n\21\3\22\3\22\3\22\3\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\5\23\u0101\n\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\5\24\u0108\n\24\3\25\3\25\3\25\3\25\3\25\5")
        buf.write("\25\u010f\n\25\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u0117")
        buf.write("\n\26\f\26\16\26\u011a\13\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\7\27\u0122\n\27\f\27\16\27\u0125\13\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\7\30\u012d\n\30\f\30\16\30\u0130")
        buf.write("\13\30\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u0138\n\31\f")
        buf.write("\31\16\31\u013b\13\31\3\32\3\32\3\32\3\32\3\32\3\32\7")
        buf.write("\32\u0143\n\32\f\32\16\32\u0146\13\32\3\33\3\33\3\33\5")
        buf.write("\33\u014b\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\5\34\u0157\n\34\7\34\u0159\n\34\f\34\16\34")
        buf.write("\u015c\13\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\5\35\u0169\n\35\3\36\3\36\5\36\u016d\n\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\5\37\u0174\n\37\3 \3 \3 \3 ")
        buf.write("\3 \3!\3!\3!\3!\5!\u017f\n!\3!\3!\5!\u0183\n!\3\"\3\"")
        buf.write("\3\"\3\"\5\"\u0189\n\"\3\"\3\"\5\"\u018d\n\"\3\"\3\"\3")
        buf.write("\"\3\"\7\"\u0193\n\"\f\"\16\"\u0196\13\"\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3#\3#\5#\u01a0\n#\3$\3$\3$\3%\3%\3%\3%\5%\u01a9")
        buf.write("\n%\3&\3&\3&\3&\3&\3&\3&\3&\5&\u01b3\n&\3&\3&\5&\u01b7")
        buf.write("\n&\3&\3&\3&\3&\7&\u01bd\n&\f&\16&\u01c0\13&\3&\3&\3&")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(")
        buf.write("\3(\3)\3)\3)\3)\5)\u01d9\n)\3*\3*\3*\3*\3+\3+\3,\3,\3")
        buf.write(",\3,\3,\5,\u01e6\n,\3-\3-\3-\5-\u01eb\n-\3.\3.\3.\3.\5")
        buf.write(".\u01f1\n.\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\7\60\u01fc")
        buf.write("\n\60\f\60\16\60\u01ff\13\60\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\3\61\7\61\u020d\n\61\f")
        buf.write("\61\16\61\u0210\13\61\3\61\3\61\3\61\5\61\u0215\n\61\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\7\62\u021f\n\62")
        buf.write("\f\62\16\62\u0222\13\62\3\62\3\62\7\62\u0226\n\62\f\62")
        buf.write("\16\62\u0229\13\62\3\62\3\62\7\62\u022d\n\62\f\62\16\62")
        buf.write("\u0230\13\62\3\62\5\62\u0233\n\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\64\3\64\5\64\u023e\n\64\3\64\3\64\3")
        buf.write("\64\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\66\5\66\u024b")
        buf.write("\n\66\3\66\3\66\3\66\3\66\7\66\u0251\n\66\f\66\16\66\u0254")
        buf.write("\13\66\3\66\3\66\3\67\3\67\38\38\39\39\39\39\59\u0260")
        buf.write("\n9\39\39\39\39\59\u0266\n9\39\39\3:\3:\3:\3:\5:\u026e")
        buf.write("\n:\3;\3;\7;\u0272\n;\f;\16;\u0275\13;\3;\6;\u0278\n;")
        buf.write("\r;\16;\u0279\5;\u027c\n;\3<\3<\3<\3=\3=\5=\u0283\n=\3")
        buf.write(">\3>\3>\3>\3>\5>\u028a\n>\3?\3?\3?\3?\3?\5?\u0291\n?\3")
        buf.write("@\7@\u0294\n@\f@\16@\u0297\13@\3@\2\b*,.\60\62\66A\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\2\b\4\2\13\16")
        buf.write("\66\66\3\2\34!\3\2\27\30\3\2\31\33\4\2\30\30$$\4\2&*/")
        buf.write("/\2\u02b8\2\u0083\3\2\2\2\4\u009a\3\2\2\2\6\u00a6\3\2")
        buf.write("\2\2\b\u00ae\3\2\2\2\n\u00b0\3\2\2\2\f\u00bd\3\2\2\2\16")
        buf.write("\u00c3\3\2\2\2\20\u00ca\3\2\2\2\22\u00cc\3\2\2\2\24\u00d3")
        buf.write("\3\2\2\2\26\u00d5\3\2\2\2\30\u00d9\3\2\2\2\32\u00e5\3")
        buf.write("\2\2\2\34\u00e7\3\2\2\2\36\u00eb\3\2\2\2 \u00f5\3\2\2")
        buf.write("\2\"\u00f7\3\2\2\2$\u0100\3\2\2\2&\u0107\3\2\2\2(\u010e")
        buf.write("\3\2\2\2*\u0110\3\2\2\2,\u011b\3\2\2\2.\u0126\3\2\2\2")
        buf.write("\60\u0131\3\2\2\2\62\u013c\3\2\2\2\64\u014a\3\2\2\2\66")
        buf.write("\u014c\3\2\2\28\u0168\3\2\2\2:\u016c\3\2\2\2<\u0173\3")
        buf.write("\2\2\2>\u0175\3\2\2\2@\u017a\3\2\2\2B\u0184\3\2\2\2D\u019f")
        buf.write("\3\2\2\2F\u01a1\3\2\2\2H\u01a8\3\2\2\2J\u01aa\3\2\2\2")
        buf.write("L\u01c4\3\2\2\2N\u01cc\3\2\2\2P\u01d8\3\2\2\2R\u01da\3")
        buf.write("\2\2\2T\u01de\3\2\2\2V\u01e5\3\2\2\2X\u01e7\3\2\2\2Z\u01f0")
        buf.write("\3\2\2\2\\\u01f2\3\2\2\2^\u01f6\3\2\2\2`\u0214\3\2\2\2")
        buf.write("b\u0216\3\2\2\2d\u0234\3\2\2\2f\u023d\3\2\2\2h\u0244\3")
        buf.write("\2\2\2j\u0246\3\2\2\2l\u0257\3\2\2\2n\u0259\3\2\2\2p\u025f")
        buf.write("\3\2\2\2r\u0269\3\2\2\2t\u027b\3\2\2\2v\u027d\3\2\2\2")
        buf.write("x\u0280\3\2\2\2z\u0289\3\2\2\2|\u028b\3\2\2\2~\u0295\3")
        buf.write("\2\2\2\u0080\u0082\7?\2\2\u0081\u0080\3\2\2\2\u0082\u0085")
        buf.write("\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084")
        buf.write("\u0086\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u008b\5\4\3\2")
        buf.write("\u0087\u008a\5\4\3\2\u0088\u008a\7?\2\2\u0089\u0087\3")
        buf.write("\2\2\2\u0089\u0088\3\2\2\2\u008a\u008d\3\2\2\2\u008b\u0089")
        buf.write("\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008e\3\2\2\2\u008d")
        buf.write("\u008b\3\2\2\2\u008e\u008f\7\2\2\3\u008f\3\3\2\2\2\u0090")
        buf.write("\u0091\5@!\2\u0091\u0092\7.\2\2\u0092\u009b\3\2\2\2\u0093")
        buf.write("\u0094\5> \2\u0094\u0095\7.\2\2\u0095\u009b\3\2\2\2\u0096")
        buf.write("\u009b\5B\"\2\u0097\u009b\5J&\2\u0098\u009b\5L\'\2\u0099")
        buf.write("\u009b\5N(\2\u009a\u0090\3\2\2\2\u009a\u0093\3\2\2\2\u009a")
        buf.write("\u0096\3\2\2\2\u009a\u0097\3\2\2\2\u009a\u0098\3\2\2\2")
        buf.write("\u009a\u0099\3\2\2\2\u009b\5\3\2\2\2\u009c\u00a7\7\67")
        buf.write("\2\2\u009d\u00a7\78\2\2\u009e\u00a7\79\2\2\u009f\u00a7")
        buf.write("\7:\2\2\u00a0\u00a7\7;\2\2\u00a1\u00a7\7<\2\2\u00a2\u00a7")
        buf.write("\7\25\2\2\u00a3\u00a7\7\26\2\2\u00a4\u00a7\5\36\20\2\u00a5")
        buf.write("\u00a7\5\30\r\2\u00a6\u009c\3\2\2\2\u00a6\u009d\3\2\2")
        buf.write("\2\u00a6\u009e\3\2\2\2\u00a6\u009f\3\2\2\2\u00a6\u00a0")
        buf.write("\3\2\2\2\u00a6\u00a1\3\2\2\2\u00a6\u00a2\3\2\2\2\u00a6")
        buf.write("\u00a3\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a5\3\2\2\2")
        buf.write("\u00a7\7\3\2\2\2\u00a8\u00af\7\f\2\2\u00a9\u00af\7\r\2")
        buf.write("\2\u00aa\u00af\7\16\2\2\u00ab\u00af\7\13\2\2\u00ac\u00af")
        buf.write("\5\22\n\2\u00ad\u00af\7\66\2\2\u00ae\u00a8\3\2\2\2\u00ae")
        buf.write("\u00a9\3\2\2\2\u00ae\u00aa\3\2\2\2\u00ae\u00ab\3\2\2\2")
        buf.write("\u00ae\u00ac\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af\t\3\2\2")
        buf.write("\2\u00b0\u00b1\t\2\2\2\u00b1\13\3\2\2\2\u00b2\u00be\5")
        buf.write("@!\2\u00b3\u00be\5> \2\u00b4\u00be\5R*\2\u00b5\u00be\5")
        buf.write("b\62\2\u00b6\u00be\5j\66\2\u00b7\u00be\5l\67\2\u00b8\u00be")
        buf.write("\5n8\2\u00b9\u00be\5p9\2\u00ba\u00be\5r:\2\u00bb\u00be")
        buf.write("\5v<\2\u00bc\u00be\5|?\2\u00bd\u00b2\3\2\2\2\u00bd\u00b3")
        buf.write("\3\2\2\2\u00bd\u00b4\3\2\2\2\u00bd\u00b5\3\2\2\2\u00bd")
        buf.write("\u00b6\3\2\2\2\u00bd\u00b7\3\2\2\2\u00bd\u00b8\3\2\2\2")
        buf.write("\u00bd\u00b9\3\2\2\2\u00bd\u00ba\3\2\2\2\u00bd\u00bb\3")
        buf.write("\2\2\2\u00bd\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c0")
        buf.write("\5t;\2\u00c0\r\3\2\2\2\u00c1\u00c4\5\20\t\2\u00c2\u00c4")
        buf.write("\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4")
        buf.write("\17\3\2\2\2\u00c5\u00c6\5\6\4\2\u00c6\u00c7\7-\2\2\u00c7")
        buf.write("\u00c8\5\16\b\2\u00c8\u00cb\3\2\2\2\u00c9\u00cb\5\6\4")
        buf.write("\2\u00ca\u00c5\3\2\2\2\u00ca\u00c9\3\2\2\2\u00cb\21\3")
        buf.write("\2\2\2\u00cc\u00cd\5\24\13\2\u00cd\u00ce\5\n\6\2\u00ce")
        buf.write("\23\3\2\2\2\u00cf\u00d0\5\26\f\2\u00d0\u00d1\5\24\13\2")
        buf.write("\u00d1\u00d4\3\2\2\2\u00d2\u00d4\5\26\f\2\u00d3\u00cf")
        buf.write("\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4\25\3\2\2\2\u00d5\u00d6")
        buf.write("\7\64\2\2\u00d6\u00d7\7\67\2\2\u00d7\u00d8\7\65\2\2\u00d8")
        buf.write("\27\3\2\2\2\u00d9\u00da\7\66\2\2\u00da\u00dc\7\62\2\2")
        buf.write("\u00db\u00dd\5\32\16\2\u00dc\u00db\3\2\2\2\u00dc\u00dd")
        buf.write("\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00df\7\63\2\2\u00df")
        buf.write("\31\3\2\2\2\u00e0\u00e1\5\34\17\2\u00e1\u00e2\7-\2\2\u00e2")
        buf.write("\u00e3\5\32\16\2\u00e3\u00e6\3\2\2\2\u00e4\u00e6\5\34")
        buf.write("\17\2\u00e5\u00e0\3\2\2\2\u00e5\u00e4\3\2\2\2\u00e6\33")
        buf.write("\3\2\2\2\u00e7\u00e8\7\66\2\2\u00e8\u00e9\7,\2\2\u00e9")
        buf.write("\u00ea\5*\26\2\u00ea\35\3\2\2\2\u00eb\u00ec\5 \21\2\u00ec")
        buf.write("\u00ed\5\b\5\2\u00ed\u00ee\7\62\2\2\u00ee\u00ef\5&\24")
        buf.write("\2\u00ef\u00f0\7\63\2\2\u00f0\37\3\2\2\2\u00f1\u00f2\5")
        buf.write("\"\22\2\u00f2\u00f3\5 \21\2\u00f3\u00f6\3\2\2\2\u00f4")
        buf.write("\u00f6\5\"\22\2\u00f5\u00f1\3\2\2\2\u00f5\u00f4\3\2\2")
        buf.write("\2\u00f6!\3\2\2\2\u00f7\u00f8\7\64\2\2\u00f8\u00f9\7\67")
        buf.write("\2\2\u00f9\u00fa\7\65\2\2\u00fa#\3\2\2\2\u00fb\u0101\5")
        buf.write("\6\4\2\u00fc\u00fd\7\62\2\2\u00fd\u00fe\5\16\b\2\u00fe")
        buf.write("\u00ff\7\63\2\2\u00ff\u0101\3\2\2\2\u0100\u00fb\3\2\2")
        buf.write("\2\u0100\u00fc\3\2\2\2\u0101%\3\2\2\2\u0102\u0103\5$\23")
        buf.write("\2\u0103\u0104\7-\2\2\u0104\u0105\5&\24\2\u0105\u0108")
        buf.write("\3\2\2\2\u0106\u0108\5$\23\2\u0107\u0102\3\2\2\2\u0107")
        buf.write("\u0106\3\2\2\2\u0108\'\3\2\2\2\u0109\u010a\5*\26\2\u010a")
        buf.write("\u010b\7-\2\2\u010b\u010c\5(\25\2\u010c\u010f\3\2\2\2")
        buf.write("\u010d\u010f\5*\26\2\u010e\u0109\3\2\2\2\u010e\u010d\3")
        buf.write("\2\2\2\u010f)\3\2\2\2\u0110\u0111\b\26\1\2\u0111\u0112")
        buf.write("\5,\27\2\u0112\u0118\3\2\2\2\u0113\u0114\f\4\2\2\u0114")
        buf.write("\u0115\7#\2\2\u0115\u0117\5,\27\2\u0116\u0113\3\2\2\2")
        buf.write("\u0117\u011a\3\2\2\2\u0118\u0116\3\2\2\2\u0118\u0119\3")
        buf.write("\2\2\2\u0119+\3\2\2\2\u011a\u0118\3\2\2\2\u011b\u011c")
        buf.write("\b\27\1\2\u011c\u011d\5.\30\2\u011d\u0123\3\2\2\2\u011e")
        buf.write("\u011f\f\4\2\2\u011f\u0120\7\"\2\2\u0120\u0122\5.\30\2")
        buf.write("\u0121\u011e\3\2\2\2\u0122\u0125\3\2\2\2\u0123\u0121\3")
        buf.write("\2\2\2\u0123\u0124\3\2\2\2\u0124-\3\2\2\2\u0125\u0123")
        buf.write("\3\2\2\2\u0126\u0127\b\30\1\2\u0127\u0128\5\60\31\2\u0128")
        buf.write("\u012e\3\2\2\2\u0129\u012a\f\4\2\2\u012a\u012b\t\3\2\2")
        buf.write("\u012b\u012d\5\60\31\2\u012c\u0129\3\2\2\2\u012d\u0130")
        buf.write("\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f")
        buf.write("/\3\2\2\2\u0130\u012e\3\2\2\2\u0131\u0132\b\31\1\2\u0132")
        buf.write("\u0133\5\62\32\2\u0133\u0139\3\2\2\2\u0134\u0135\f\4\2")
        buf.write("\2\u0135\u0136\t\4\2\2\u0136\u0138\5\62\32\2\u0137\u0134")
        buf.write("\3\2\2\2\u0138\u013b\3\2\2\2\u0139\u0137\3\2\2\2\u0139")
        buf.write("\u013a\3\2\2\2\u013a\61\3\2\2\2\u013b\u0139\3\2\2\2\u013c")
        buf.write("\u013d\b\32\1\2\u013d\u013e\5\64\33\2\u013e\u0144\3\2")
        buf.write("\2\2\u013f\u0140\f\4\2\2\u0140\u0141\t\5\2\2\u0141\u0143")
        buf.write("\5\64\33\2\u0142\u013f\3\2\2\2\u0143\u0146\3\2\2\2\u0144")
        buf.write("\u0142\3\2\2\2\u0144\u0145\3\2\2\2\u0145\63\3\2\2\2\u0146")
        buf.write("\u0144\3\2\2\2\u0147\u0148\t\6\2\2\u0148\u014b\5*\26\2")
        buf.write("\u0149\u014b\5\66\34\2\u014a\u0147\3\2\2\2\u014a\u0149")
        buf.write("\3\2\2\2\u014b\65\3\2\2\2\u014c\u014d\b\34\1\2\u014d\u014e")
        buf.write("\58\35\2\u014e\u015a\3\2\2\2\u014f\u0156\f\4\2\2\u0150")
        buf.write("\u0151\7\64\2\2\u0151\u0152\5*\26\2\u0152\u0153\7\65\2")
        buf.write("\2\u0153\u0157\3\2\2\2\u0154\u0155\7+\2\2\u0155\u0157")
        buf.write("\5*\26\2\u0156\u0150\3\2\2\2\u0156\u0154\3\2\2\2\u0157")
        buf.write("\u0159\3\2\2\2\u0158\u014f\3\2\2\2\u0159\u015c\3\2\2\2")
        buf.write("\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\67\3\2")
        buf.write("\2\2\u015c\u015a\3\2\2\2\u015d\u0169\5\6\4\2\u015e\u015f")
        buf.write("\7\60\2\2\u015f\u0160\5*\26\2\u0160\u0161\7\61\2\2\u0161")
        buf.write("\u0169\3\2\2\2\u0162\u0169\7\66\2\2\u0163\u0164\7\66\2")
        buf.write("\2\u0164\u0165\7\60\2\2\u0165\u0166\5:\36\2\u0166\u0167")
        buf.write("\7\61\2\2\u0167\u0169\3\2\2\2\u0168\u015d\3\2\2\2\u0168")
        buf.write("\u015e\3\2\2\2\u0168\u0162\3\2\2\2\u0168\u0163\3\2\2\2")
        buf.write("\u01699\3\2\2\2\u016a\u016d\5<\37\2\u016b\u016d\3\2\2")
        buf.write("\2\u016c\u016a\3\2\2\2\u016c\u016b\3\2\2\2\u016d;\3\2")
        buf.write("\2\2\u016e\u0174\5*\26\2\u016f\u0170\5*\26\2\u0170\u0171")
        buf.write("\7-\2\2\u0171\u0172\5<\37\2\u0172\u0174\3\2\2\2\u0173")
        buf.write("\u016e\3\2\2\2\u0173\u016f\3\2\2\2\u0174=\3\2\2\2\u0175")
        buf.write("\u0176\7\17\2\2\u0176\u0177\7\66\2\2\u0177\u0178\7%\2")
        buf.write("\2\u0178\u0179\5*\26\2\u0179?\3\2\2\2\u017a\u017b\7\20")
        buf.write("\2\2\u017b\u0182\7\66\2\2\u017c\u0183\5\b\5\2\u017d\u017f")
        buf.write("\5\b\5\2\u017e\u017d\3\2\2\2\u017e\u017f\3\2\2\2\u017f")
        buf.write("\u0180\3\2\2\2\u0180\u0181\7%\2\2\u0181\u0183\5*\26\2")
        buf.write("\u0182\u017c\3\2\2\2\u0182\u017e\3\2\2\2\u0183A\3\2\2")
        buf.write("\2\u0184\u0185\7\7\2\2\u0185\u0186\7\66\2\2\u0186\u0188")
        buf.write("\7\60\2\2\u0187\u0189\5D#\2\u0188\u0187\3\2\2\2\u0188")
        buf.write("\u0189\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018c\7\61\2")
        buf.write("\2\u018b\u018d\5\b\5\2\u018c\u018b\3\2\2\2\u018c\u018d")
        buf.write("\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u018f\5~@\2\u018f\u0194")
        buf.write("\7\62\2\2\u0190\u0193\7?\2\2\u0191\u0193\5P)\2\u0192\u0190")
        buf.write("\3\2\2\2\u0192\u0191\3\2\2\2\u0193\u0196\3\2\2\2\u0194")
        buf.write("\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0197\3\2\2\2")
        buf.write("\u0196\u0194\3\2\2\2\u0197\u0198\7\63\2\2\u0198\u0199")
        buf.write("\7.\2\2\u0199C\3\2\2\2\u019a\u019b\5F$\2\u019b\u019c\7")
        buf.write("-\2\2\u019c\u019d\5D#\2\u019d\u01a0\3\2\2\2\u019e\u01a0")
        buf.write("\5F$\2\u019f\u019a\3\2\2\2\u019f\u019e\3\2\2\2\u01a0E")
        buf.write("\3\2\2\2\u01a1\u01a2\5H%\2\u01a2\u01a3\5\b\5\2\u01a3G")
        buf.write("\3\2\2\2\u01a4\u01a5\7\66\2\2\u01a5\u01a6\7-\2\2\u01a6")
        buf.write("\u01a9\5H%\2\u01a7\u01a9\7\66\2\2\u01a8\u01a4\3\2\2\2")
        buf.write("\u01a8\u01a7\3\2\2\2\u01a9I\3\2\2\2\u01aa\u01ab\7\7\2")
        buf.write("\2\u01ab\u01ac\7\60\2\2\u01ac\u01ad\7\66\2\2\u01ad\u01ae")
        buf.write("\7\66\2\2\u01ae\u01af\7\61\2\2\u01af\u01b0\7\66\2\2\u01b0")
        buf.write("\u01b2\7\60\2\2\u01b1\u01b3\5D#\2\u01b2\u01b1\3\2\2\2")
        buf.write("\u01b2\u01b3\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b6\7")
        buf.write("\61\2\2\u01b5\u01b7\5\b\5\2\u01b6\u01b5\3\2\2\2\u01b6")
        buf.write("\u01b7\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01b9\5~@\2\u01b9")
        buf.write("\u01be\7\62\2\2\u01ba\u01bd\7?\2\2\u01bb\u01bd\5P)\2\u01bc")
        buf.write("\u01ba\3\2\2\2\u01bc\u01bb\3\2\2\2\u01bd\u01c0\3\2\2\2")
        buf.write("\u01be\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c1\3")
        buf.write("\2\2\2\u01c0\u01be\3\2\2\2\u01c1\u01c2\7\63\2\2\u01c2")
        buf.write("\u01c3\7.\2\2\u01c3K\3\2\2\2\u01c4\u01c5\7\b\2\2\u01c5")
        buf.write("\u01c6\7\66\2\2\u01c6\u01c7\7\t\2\2\u01c7\u01c8\7\62\2")
        buf.write("\2\u01c8\u01c9\5P)\2\u01c9\u01ca\7\63\2\2\u01ca\u01cb")
        buf.write("\7.\2\2\u01cbM\3\2\2\2\u01cc\u01cd\7\b\2\2\u01cd\u01ce")
        buf.write("\7\66\2\2\u01ce\u01cf\7\n\2\2\u01cf\u01d0\7\62\2\2\u01d0")
        buf.write("\u01d1\5P)\2\u01d1\u01d2\7\63\2\2\u01d2\u01d3\7.\2\2\u01d3")
        buf.write("O\3\2\2\2\u01d4\u01d5\5\f\7\2\u01d5\u01d6\5P)\2\u01d6")
        buf.write("\u01d9\3\2\2\2\u01d7\u01d9\5\f\7\2\u01d8\u01d4\3\2\2\2")
        buf.write("\u01d8\u01d7\3\2\2\2\u01d9Q\3\2\2\2\u01da\u01db\5V,\2")
        buf.write("\u01db\u01dc\5T+\2\u01dc\u01dd\5*\26\2\u01ddS\3\2\2\2")
        buf.write("\u01de\u01df\t\7\2\2\u01dfU\3\2\2\2\u01e0\u01e1\5X-\2")
        buf.write("\u01e1\u01e2\7+\2\2\u01e2\u01e3\5V,\2\u01e3\u01e6\3\2")
        buf.write("\2\2\u01e4\u01e6\5X-\2\u01e5\u01e0\3\2\2\2\u01e5\u01e4")
        buf.write("\3\2\2\2\u01e6W\3\2\2\2\u01e7\u01ea\7\66\2\2\u01e8\u01eb")
        buf.write("\5Z.\2\u01e9\u01eb\3\2\2\2\u01ea\u01e8\3\2\2\2\u01ea\u01e9")
        buf.write("\3\2\2\2\u01ebY\3\2\2\2\u01ec\u01ed\5\\/\2\u01ed\u01ee")
        buf.write("\5Z.\2\u01ee\u01f1\3\2\2\2\u01ef\u01f1\5\\/\2\u01f0\u01ec")
        buf.write("\3\2\2\2\u01f0\u01ef\3\2\2\2\u01f1[\3\2\2\2\u01f2\u01f3")
        buf.write("\7\64\2\2\u01f3\u01f4\5*\26\2\u01f4\u01f5\7\65\2\2\u01f5")
        buf.write("]\3\2\2\2\u01f6\u01f7\7\4\2\2\u01f7\u01f8\5~@\2\u01f8")
        buf.write("\u01fd\7\62\2\2\u01f9\u01fc\7?\2\2\u01fa\u01fc\5P)\2\u01fb")
        buf.write("\u01f9\3\2\2\2\u01fb\u01fa\3\2\2\2\u01fc\u01ff\3\2\2\2")
        buf.write("\u01fd\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u0200\3")
        buf.write("\2\2\2\u01ff\u01fd\3\2\2\2\u0200\u0201\7\63\2\2\u0201")
        buf.write("_\3\2\2\2\u0202\u0215\3\2\2\2\u0203\u0204\7\4\2\2\u0204")
        buf.write("\u0205\7\3\2\2\u0205\u0206\7\60\2\2\u0206\u0207\5*\26")
        buf.write("\2\u0207\u0208\7\61\2\2\u0208\u0209\5~@\2\u0209\u020e")
        buf.write("\7\62\2\2\u020a\u020d\7?\2\2\u020b\u020d\5P)\2\u020c\u020a")
        buf.write("\3\2\2\2\u020c\u020b\3\2\2\2\u020d\u0210\3\2\2\2\u020e")
        buf.write("\u020c\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u0211\3\2\2\2")
        buf.write("\u0210\u020e\3\2\2\2\u0211\u0212\7\63\2\2\u0212\u0213")
        buf.write("\5`\61\2\u0213\u0215\3\2\2\2\u0214\u0202\3\2\2\2\u0214")
        buf.write("\u0203\3\2\2\2\u0215a\3\2\2\2\u0216\u0217\7\3\2\2\u0217")
        buf.write("\u0218\7\60\2\2\u0218\u0219\5*\26\2\u0219\u021a\7\61\2")
        buf.write("\2\u021a\u021b\5~@\2\u021b\u0220\7\62\2\2\u021c\u021f")
        buf.write("\7?\2\2\u021d\u021f\5P)\2\u021e\u021c\3\2\2\2\u021e\u021d")
        buf.write("\3\2\2\2\u021f\u0222\3\2\2\2\u0220\u021e\3\2\2\2\u0220")
        buf.write("\u0221\3\2\2\2\u0221\u0223\3\2\2\2\u0222\u0220\3\2\2\2")
        buf.write("\u0223\u0227\7\63\2\2\u0224\u0226\7?\2\2\u0225\u0224\3")
        buf.write("\2\2\2\u0226\u0229\3\2\2\2\u0227\u0225\3\2\2\2\u0227\u0228")
        buf.write("\3\2\2\2\u0228\u022a\3\2\2\2\u0229\u0227\3\2\2\2\u022a")
        buf.write("\u022e\5`\61\2\u022b\u022d\7?\2\2\u022c\u022b\3\2\2\2")
        buf.write("\u022d\u0230\3\2\2\2\u022e\u022c\3\2\2\2\u022e\u022f\3")
        buf.write("\2\2\2\u022f\u0232\3\2\2\2\u0230\u022e\3\2\2\2\u0231\u0233")
        buf.write("\5^\60\2\u0232\u0231\3\2\2\2\u0232\u0233\3\2\2\2\u0233")
        buf.write("c\3\2\2\2\u0234\u0235\7\66\2\2\u0235\u0236\7-\2\2\u0236")
        buf.write("\u0237\7\66\2\2\u0237\u0238\7/\2\2\u0238\u0239\7\23\2")
        buf.write("\2\u0239\u023a\5*\26\2\u023ae\3\2\2\2\u023b\u023e\5R*")
        buf.write("\2\u023c\u023e\5@!\2\u023d\u023b\3\2\2\2\u023d\u023c\3")
        buf.write("\2\2\2\u023e\u023f\3\2\2\2\u023f\u0240\7.\2\2\u0240\u0241")
        buf.write("\5*\26\2\u0241\u0242\7.\2\2\u0242\u0243\5R*\2\u0243g\3")
        buf.write("\2\2\2\u0244\u0245\5*\26\2\u0245i\3\2\2\2\u0246\u024a")
        buf.write("\7\5\2\2\u0247\u024b\5h\65\2\u0248\u024b\5f\64\2\u0249")
        buf.write("\u024b\5d\63\2\u024a\u0247\3\2\2\2\u024a\u0248\3\2\2\2")
        buf.write("\u024a\u0249\3\2\2\2\u024b\u024c\3\2\2\2\u024c\u024d\5")
        buf.write("~@\2\u024d\u0252\7\62\2\2\u024e\u0251\7?\2\2\u024f\u0251")
        buf.write("\5P)\2\u0250\u024e\3\2\2\2\u0250\u024f\3\2\2\2\u0251\u0254")
        buf.write("\3\2\2\2\u0252\u0250\3\2\2\2\u0252\u0253\3\2\2\2\u0253")
        buf.write("\u0255\3\2\2\2\u0254\u0252\3\2\2\2\u0255\u0256\7\63\2")
        buf.write("\2\u0256k\3\2\2\2\u0257\u0258\7\22\2\2\u0258m\3\2\2\2")
        buf.write("\u0259\u025a\7\21\2\2\u025ao\3\2\2\2\u025b\u025c\5V,\2")
        buf.write("\u025c\u025d\7+\2\2\u025d\u0260\3\2\2\2\u025e\u0260\3")
        buf.write("\2\2\2\u025f\u025b\3\2\2\2\u025f\u025e\3\2\2\2\u0260\u0261")
        buf.write("\3\2\2\2\u0261\u0262\7\66\2\2\u0262\u0265\7\60\2\2\u0263")
        buf.write("\u0266\5(\25\2\u0264\u0266\3\2\2\2\u0265\u0263\3\2\2\2")
        buf.write("\u0265\u0264\3\2\2\2\u0266\u0267\3\2\2\2\u0267\u0268\7")
        buf.write("\61\2\2\u0268q\3\2\2\2\u0269\u026a\7\6\2\2\u026a\u026d")
        buf.write("\5~@\2\u026b\u026e\5*\26\2\u026c\u026e\3\2\2\2\u026d\u026b")
        buf.write("\3\2\2\2\u026d\u026c\3\2\2\2\u026es\3\2\2\2\u026f\u0273")
        buf.write("\7.\2\2\u0270\u0272\7?\2\2\u0271\u0270\3\2\2\2\u0272\u0275")
        buf.write("\3\2\2\2\u0273\u0271\3\2\2\2\u0273\u0274\3\2\2\2\u0274")
        buf.write("\u027c\3\2\2\2\u0275\u0273\3\2\2\2\u0276\u0278\7?\2\2")
        buf.write("\u0277\u0276\3\2\2\2\u0278\u0279\3\2\2\2\u0279\u0277\3")
        buf.write("\2\2\2\u0279\u027a\3\2\2\2\u027a\u027c\3\2\2\2\u027b\u026f")
        buf.write("\3\2\2\2\u027b\u0277\3\2\2\2\u027cu\3\2\2\2\u027d\u027e")
        buf.write("\7\66\2\2\u027e\u027f\5\b\5\2\u027fw\3\2\2\2\u0280\u0282")
        buf.write("\7\66\2\2\u0281\u0283\5\b\5\2\u0282\u0281\3\2\2\2\u0282")
        buf.write("\u0283\3\2\2\2\u0283y\3\2\2\2\u0284\u0285\5x=\2\u0285")
        buf.write("\u0286\7-\2\2\u0286\u0287\5z>\2\u0287\u028a\3\2\2\2\u0288")
        buf.write("\u028a\5x=\2\u0289\u0284\3\2\2\2\u0289\u0288\3\2\2\2\u028a")
        buf.write("{\3\2\2\2\u028b\u028c\7\66\2\2\u028c\u028d\7\60\2\2\u028d")
        buf.write("\u028e\5z>\2\u028e\u0290\7\61\2\2\u028f\u0291\5\b\5\2")
        buf.write("\u0290\u028f\3\2\2\2\u0290\u0291\3\2\2\2\u0291}\3\2\2")
        buf.write("\2\u0292\u0294\7?\2\2\u0293\u0292\3\2\2\2\u0294\u0297")
        buf.write("\3\2\2\2\u0295\u0293\3\2\2\2\u0295\u0296\3\2\2\2\u0296")
        buf.write("\177\3\2\2\2\u0297\u0295\3\2\2\2E\u0083\u0089\u008b\u009a")
        buf.write("\u00a6\u00ae\u00bd\u00c3\u00ca\u00d3\u00dc\u00e5\u00f5")
        buf.write("\u0100\u0107\u010e\u0118\u0123\u012e\u0139\u0144\u014a")
        buf.write("\u0156\u015a\u0168\u016c\u0173\u017e\u0182\u0188\u018c")
        buf.write("\u0192\u0194\u019f\u01a8\u01b2\u01b6\u01bc\u01be\u01d8")
        buf.write("\u01e5\u01ea\u01f0\u01fb\u01fd\u020c\u020e\u0214\u021e")
        buf.write("\u0220\u0227\u022e\u0232\u023d\u024a\u0250\u0252\u025f")
        buf.write("\u0265\u026d\u0273\u0279\u027b\u0282\u0289\u0290\u0295")
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
    RULE_interface_decl = 38
    RULE_list_statement = 39
    RULE_ass_statement = 40
    RULE_operator = 41
    RULE_list_assignment_lhs = 42
    RULE_assignment_lhs = 43
    RULE_list_array_index = 44
    RULE_array_index = 45
    RULE_else_statement = 46
    RULE_elif_statement = 47
    RULE_if_statement = 48
    RULE_range_loop = 49
    RULE_init_loop = 50
    RULE_basic_loop = 51
    RULE_for_statement = 52
    RULE_break_statement = 53
    RULE_continue_statement = 54
    RULE_call_statement = 55
    RULE_return_statement = 56
    RULE_end_statement = 57
    RULE_struct_statements = 58
    RULE_method_param = 59
    RULE_method_param_lit = 60
    RULE_method_statement = 61
    RULE_ignore = 62

    ruleNames =  [ "program", "declared", "liter", "all_type", "basic_type", 
                   "statement", "list_liter", "list_literal_noempty", "list_array_type_lit", 
                   "array_type_lit", "array_type", "struct_literal", "list_ele_lit", 
                   "list_ele", "arr_liter", "dim_lit", "dim", "arr_ele", 
                   "list_arr_ele", "list_expr", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "functcall", 
                   "functcall_noempty", "const_decl", "var_decl", "func_decl", 
                   "param_lit", "param", "list_ID", "method_decl", "struct_decl", 
                   "interface_decl", "list_statement", "ass_statement", 
                   "operator", "list_assignment_lhs", "assignment_lhs", 
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
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.NEWLINE:
                self.state = 126
                self.match(MiniGoParser.NEWLINE)
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 132
            self.declared()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.NEWLINE))) != 0):
                self.state = 135
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                    self.state = 133
                    self.declared()
                    pass
                elif token in [MiniGoParser.NEWLINE]:
                    self.state = 134
                    self.match(MiniGoParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 140
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
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.var_decl()
                self.state = 143
                self.match(MiniGoParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.const_decl()
                self.state = 146
                self.match(MiniGoParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.func_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 149
                self.method_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 150
                self.struct_decl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 151
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
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.BIN_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(MiniGoParser.BIN_LIT)
                pass
            elif token in [MiniGoParser.OCT_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.match(MiniGoParser.OCT_LIT)
                pass
            elif token in [MiniGoParser.HEX_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 157
                self.match(MiniGoParser.HEX_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 158
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 159
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 160
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 8)
                self.state = 161
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.LSP]:
                self.enterOuterAlt(localctx, 9)
                self.state = 162
                self.arr_liter()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 10)
                self.state = 163
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
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 168
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 169
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.LSP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 170
                self.list_array_type_lit()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 171
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
            self.state = 174
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
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 176
                self.var_decl()
                pass

            elif la_ == 2:
                self.state = 177
                self.const_decl()
                pass

            elif la_ == 3:
                self.state = 178
                self.ass_statement()
                pass

            elif la_ == 4:
                self.state = 179
                self.if_statement()
                pass

            elif la_ == 5:
                self.state = 180
                self.for_statement()
                pass

            elif la_ == 6:
                self.state = 181
                self.break_statement()
                pass

            elif la_ == 7:
                self.state = 182
                self.continue_statement()
                pass

            elif la_ == 8:
                self.state = 183
                self.call_statement()
                pass

            elif la_ == 9:
                self.state = 184
                self.return_statement()
                pass

            elif la_ == 10:
                self.state = 185
                self.struct_statements()
                pass

            elif la_ == 11:
                self.state = 186
                self.method_statement()
                pass


            self.state = 189
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
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LSP, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.list_literal_noempty()
                pass
            elif token in [MiniGoParser.RCP]:
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
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.liter()
                self.state = 196
                self.match(MiniGoParser.COMMA)
                self.state = 197
                self.list_liter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
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
            self.state = 202
            self.array_type_lit()
            self.state = 203
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
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.array_type()
                self.state = 206
                self.array_type_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
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
            self.state = 211
            self.match(MiniGoParser.LSP)
            self.state = 212
            self.match(MiniGoParser.INT_LIT)
            self.state = 213
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
            self.state = 215
            self.match(MiniGoParser.ID)
            self.state = 216
            self.match(MiniGoParser.LCP)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 217
                self.list_ele_lit()


            self.state = 220
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
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.list_ele()
                self.state = 223
                self.match(MiniGoParser.COMMA)
                self.state = 224
                self.list_ele_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
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
            self.state = 229
            self.match(MiniGoParser.ID)
            self.state = 230
            self.match(MiniGoParser.COLON)
            self.state = 231
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

        def list_arr_ele(self):
            return self.getTypedRuleContext(MiniGoParser.List_arr_eleContext,0)


        def RCP(self):
            return self.getToken(MiniGoParser.RCP, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.dim_lit()
            self.state = 234
            self.all_type()
            self.state = 235
            self.match(MiniGoParser.LCP)
            self.state = 236
            self.list_arr_ele()
            self.state = 237
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
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.dim()
                self.state = 240
                self.dim_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
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
            self.state = 245
            self.match(MiniGoParser.LSP)
            self.state = 246
            self.match(MiniGoParser.INT_LIT)
            self.state = 247
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


        def LCP(self):
            return self.getToken(MiniGoParser.LCP, 0)

        def list_liter(self):
            return self.getTypedRuleContext(MiniGoParser.List_literContext,0)


        def RCP(self):
            return self.getToken(MiniGoParser.RCP, 0)

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
        try:
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LSP, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.liter()
                pass
            elif token in [MiniGoParser.LCP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.match(MiniGoParser.LCP)
                self.state = 251
                self.list_liter()
                self.state = 252
                self.match(MiniGoParser.RCP)
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
        try:
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.arr_ele()
                self.state = 257
                self.match(MiniGoParser.COMMA)
                self.state = 258
                self.list_arr_ele()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.arr_ele()
                pass


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
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.expr(0)
                self.state = 264
                self.match(MiniGoParser.COMMA)
                self.state = 265
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
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
            self.state = 271
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 278
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 273
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 274
                    self.match(MiniGoParser.OR)
                    self.state = 275
                    self.expr1(0) 
                self.state = 280
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
            self.state = 282
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 289
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 284
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 285
                    self.match(MiniGoParser.AND)
                    self.state = 286
                    self.expr2(0) 
                self.state = 291
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
            self.state = 293
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 300
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 295
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 296
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.UNEQUAL) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LTE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GTE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 297
                    self.expr3(0) 
                self.state = 302
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
            self.state = 304
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 311
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 306
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 307
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 308
                    self.expr4(0) 
                self.state = 313
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
            self.state = 315
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 322
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 317
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 318
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 319
                    self.expr5() 
                self.state = 324
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
            self.state = 328
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 326
                self.expr(0)
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LP, MiniGoParser.LSP, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
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
            self.state = 331
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 344
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 333
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 340
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LSP]:
                        self.state = 334
                        self.match(MiniGoParser.LSP)
                        self.state = 335
                        self.expr(0)
                        self.state = 336
                        self.match(MiniGoParser.RSP)
                        pass
                    elif token in [MiniGoParser.DOT]:
                        self.state = 338
                        self.match(MiniGoParser.DOT)
                        self.state = 339
                        self.expr(0)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 346
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.liter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.match(MiniGoParser.LP)
                self.state = 349
                self.expr(0)
                self.state = 350
                self.match(MiniGoParser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 352
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 353
                self.match(MiniGoParser.ID)
                self.state = 354
                self.match(MiniGoParser.LP)
                self.state = 355
                self.functcall()
                self.state = 356
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
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LP, MiniGoParser.LSP, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
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
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                self.expr(0)
                self.state = 366
                self.match(MiniGoParser.COMMA)
                self.state = 367
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
            self.state = 371
            self.match(MiniGoParser.CONST)
            self.state = 372
            self.match(MiniGoParser.ID)
            self.state = 373
            self.match(MiniGoParser.ASSIGN)
            self.state = 374
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
            self.state = 376
            self.match(MiniGoParser.VAR)
            self.state = 377
            self.match(MiniGoParser.ID)
            self.state = 384
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 378
                self.all_type()
                pass

            elif la_ == 2:
                self.state = 380
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSP) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 379
                    self.all_type()


                self.state = 382
                self.match(MiniGoParser.ASSIGN)
                self.state = 383
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
            self.state = 386
            self.match(MiniGoParser.FUNC)
            self.state = 387
            self.match(MiniGoParser.ID)
            self.state = 388
            self.match(MiniGoParser.LP)
            self.state = 390
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 389
                self.param_lit()


            self.state = 392
            self.match(MiniGoParser.RP)
            self.state = 394
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSP) | (1 << MiniGoParser.ID))) != 0):
                self.state = 393
                self.all_type()


            self.state = 396
            self.ignore()
            self.state = 397
            self.match(MiniGoParser.LCP)
            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.NEWLINE))) != 0):
                self.state = 400
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.NEWLINE]:
                    self.state = 398
                    self.match(MiniGoParser.NEWLINE)
                    pass
                elif token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                    self.state = 399
                    self.list_statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 404
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 405
            self.match(MiniGoParser.RCP)
            self.state = 406
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
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                self.param()
                self.state = 409
                self.match(MiniGoParser.COMMA)
                self.state = 410
                self.param_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
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
            self.state = 415
            self.list_ID()
            self.state = 416
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
            self.state = 422
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.match(MiniGoParser.ID)
                self.state = 419
                self.match(MiniGoParser.COMMA)
                self.state = 420
                self.list_ID()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
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
            self.state = 424
            self.match(MiniGoParser.FUNC)
            self.state = 425
            self.match(MiniGoParser.LP)
            self.state = 426
            self.match(MiniGoParser.ID)
            self.state = 427
            self.match(MiniGoParser.ID)
            self.state = 428
            self.match(MiniGoParser.RP)
            self.state = 429
            self.match(MiniGoParser.ID)
            self.state = 430
            self.match(MiniGoParser.LP)
            self.state = 432
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 431
                self.param_lit()


            self.state = 434
            self.match(MiniGoParser.RP)
            self.state = 436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSP) | (1 << MiniGoParser.ID))) != 0):
                self.state = 435
                self.all_type()


            self.state = 438
            self.ignore()
            self.state = 439
            self.match(MiniGoParser.LCP)
            self.state = 444
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.NEWLINE))) != 0):
                self.state = 442
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.NEWLINE]:
                    self.state = 440
                    self.match(MiniGoParser.NEWLINE)
                    pass
                elif token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                    self.state = 441
                    self.list_statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 446
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 447
            self.match(MiniGoParser.RCP)
            self.state = 448
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
            self.state = 450
            self.match(MiniGoParser.TYPE)
            self.state = 451
            self.match(MiniGoParser.ID)
            self.state = 452
            self.match(MiniGoParser.STRUCT)
            self.state = 453
            self.match(MiniGoParser.LCP)
            self.state = 454
            self.list_statement()
            self.state = 455
            self.match(MiniGoParser.RCP)
            self.state = 456
            self.match(MiniGoParser.SEMICOLON)
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
        self.enterRule(localctx, 76, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(MiniGoParser.TYPE)
            self.state = 459
            self.match(MiniGoParser.ID)
            self.state = 460
            self.match(MiniGoParser.INTERFACE)
            self.state = 461
            self.match(MiniGoParser.LCP)
            self.state = 462
            self.list_statement()
            self.state = 463
            self.match(MiniGoParser.RCP)
            self.state = 464
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
        self.enterRule(localctx, 78, self.RULE_list_statement)
        try:
            self.state = 470
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.statement()
                self.state = 467
                self.list_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 469
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
        self.enterRule(localctx, 80, self.RULE_ass_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.list_assignment_lhs()
            self.state = 473
            self.operator()
            self.state = 474
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
        self.enterRule(localctx, 82, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
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
        self.enterRule(localctx, 84, self.RULE_list_assignment_lhs)
        try:
            self.state = 483
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.assignment_lhs()
                self.state = 479
                self.match(MiniGoParser.DOT)
                self.state = 480
                self.list_assignment_lhs()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
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
        self.enterRule(localctx, 86, self.RULE_assignment_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(MiniGoParser.ID)
            self.state = 488
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LSP]:
                self.state = 486
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
        self.enterRule(localctx, 88, self.RULE_list_array_index)
        try:
            self.state = 494
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 490
                self.array_index()
                self.state = 491
                self.list_array_index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 493
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
        self.enterRule(localctx, 90, self.RULE_array_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self.match(MiniGoParser.LSP)
            self.state = 497
            self.expr(0)
            self.state = 498
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
        self.enterRule(localctx, 92, self.RULE_else_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(MiniGoParser.ELSE)
            self.state = 501
            self.ignore()
            self.state = 502
            self.match(MiniGoParser.LCP)
            self.state = 507
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.NEWLINE))) != 0):
                self.state = 505
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.NEWLINE]:
                    self.state = 503
                    self.match(MiniGoParser.NEWLINE)
                    pass
                elif token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                    self.state = 504
                    self.list_statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 509
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 510
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
        self.enterRule(localctx, 94, self.RULE_elif_statement)
        self._la = 0 # Token type
        try:
            self.state = 530
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 513
                self.match(MiniGoParser.ELSE)
                self.state = 514
                self.match(MiniGoParser.IF)
                self.state = 515
                self.match(MiniGoParser.LP)
                self.state = 516
                self.expr(0)
                self.state = 517
                self.match(MiniGoParser.RP)
                self.state = 518
                self.ignore()
                self.state = 519
                self.match(MiniGoParser.LCP)
                self.state = 524
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.NEWLINE))) != 0):
                    self.state = 522
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.NEWLINE]:
                        self.state = 520
                        self.match(MiniGoParser.NEWLINE)
                        pass
                    elif token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                        self.state = 521
                        self.list_statement()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 526
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 527
                self.match(MiniGoParser.RCP)
                self.state = 528
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
        self.enterRule(localctx, 96, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.match(MiniGoParser.IF)
            self.state = 533
            self.match(MiniGoParser.LP)
            self.state = 534
            self.expr(0)
            self.state = 535
            self.match(MiniGoParser.RP)
            self.state = 536
            self.ignore()
            self.state = 537
            self.match(MiniGoParser.LCP)
            self.state = 542
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.NEWLINE))) != 0):
                self.state = 540
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.NEWLINE]:
                    self.state = 538
                    self.match(MiniGoParser.NEWLINE)
                    pass
                elif token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                    self.state = 539
                    self.list_statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 544
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 545
            self.match(MiniGoParser.RCP)
            self.state = 549
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 546
                    self.match(MiniGoParser.NEWLINE) 
                self.state = 551
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

            self.state = 552
            self.elif_statement()
            self.state = 556
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 553
                    self.match(MiniGoParser.NEWLINE) 
                self.state = 558
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

            self.state = 560
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 559
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
        self.enterRule(localctx, 98, self.RULE_range_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            self.match(MiniGoParser.ID)
            self.state = 563
            self.match(MiniGoParser.COMMA)
            self.state = 564
            self.match(MiniGoParser.ID)
            self.state = 565
            self.match(MiniGoParser.COLONEQUAL)
            self.state = 566
            self.match(MiniGoParser.RANGE)
            self.state = 567
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
        self.enterRule(localctx, 100, self.RULE_init_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 571
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 569
                self.ass_statement()
                pass
            elif token in [MiniGoParser.VAR]:
                self.state = 570
                self.var_decl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 573
            self.match(MiniGoParser.SEMICOLON)
            self.state = 574
            self.expr(0)
            self.state = 575
            self.match(MiniGoParser.SEMICOLON)
            self.state = 576
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
        self.enterRule(localctx, 102, self.RULE_basic_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 578
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
        self.enterRule(localctx, 104, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
            self.match(MiniGoParser.FOR)
            self.state = 584
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.state = 581
                self.basic_loop()
                pass

            elif la_ == 2:
                self.state = 582
                self.init_loop()
                pass

            elif la_ == 3:
                self.state = 583
                self.range_loop()
                pass


            self.state = 586
            self.ignore()
            self.state = 587
            self.match(MiniGoParser.LCP)
            self.state = 592
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.NEWLINE))) != 0):
                self.state = 590
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.NEWLINE]:
                    self.state = 588
                    self.match(MiniGoParser.NEWLINE)
                    pass
                elif token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.ID]:
                    self.state = 589
                    self.list_statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 594
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 595
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
        self.enterRule(localctx, 106, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 597
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
        self.enterRule(localctx, 108, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 599
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
        self.enterRule(localctx, 110, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.state = 601
                self.list_assignment_lhs()
                self.state = 602
                self.match(MiniGoParser.DOT)
                pass

            elif la_ == 2:
                pass


            self.state = 607
            self.match(MiniGoParser.ID)
            self.state = 608
            self.match(MiniGoParser.LP)
            self.state = 611
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LP, MiniGoParser.LSP, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 609
                self.list_expr()
                pass
            elif token in [MiniGoParser.RP]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 613
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
        self.enterRule(localctx, 112, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            self.match(MiniGoParser.RETURN)
            self.state = 616
            self.ignore()
            self.state = 619
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LP, MiniGoParser.LSP, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.OCT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 617
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
        self.enterRule(localctx, 114, self.RULE_end_statement)
        try:
            self.state = 633
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SEMICOLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 621
                self.match(MiniGoParser.SEMICOLON)
                self.state = 625
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 622
                        self.match(MiniGoParser.NEWLINE) 
                    self.state = 627
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,60,self._ctx)

                pass
            elif token in [MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 629 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 628
                        self.match(MiniGoParser.NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 631 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,61,self._ctx)

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
        self.enterRule(localctx, 116, self.RULE_struct_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635
            self.match(MiniGoParser.ID)
            self.state = 636
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
        self.enterRule(localctx, 118, self.RULE_method_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 638
            self.match(MiniGoParser.ID)
            self.state = 640
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSP) | (1 << MiniGoParser.ID))) != 0):
                self.state = 639
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
        self.enterRule(localctx, 120, self.RULE_method_param_lit)
        try:
            self.state = 647
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 642
                self.method_param()
                self.state = 643
                self.match(MiniGoParser.COMMA)
                self.state = 644
                self.method_param_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 646
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
        self.enterRule(localctx, 122, self.RULE_method_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 649
            self.match(MiniGoParser.ID)
            self.state = 650
            self.match(MiniGoParser.LP)
            self.state = 651
            self.method_param_lit()
            self.state = 652
            self.match(MiniGoParser.RP)
            self.state = 654
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSP) | (1 << MiniGoParser.ID))) != 0):
                self.state = 653
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
        self.enterRule(localctx, 124, self.RULE_ignore)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 659
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,66,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 656
                    self.match(MiniGoParser.NEWLINE) 
                self.state = 661
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,66,self._ctx)

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
         




