grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def __init__(self, input=None, output:TextIO = sys.stdout):
    super().__init__(input, output)
    self.checkVersion("4.9.2")
    self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
    self._actions = None
    self._predicates = None
    self.preType = None

def emit(self):
    tk = self.type
    self.preType = tk;
    if tk == self.UNCLOSE_STRING:
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text);
    else:
        return super().emit();
}

options{
	language = Python3;
}
// Use ANTLR to write regular expressions describing
// Pascal strings are made up of a sequence of characters between single quotes: 'string'.
// The single quote itself can appear as two single quotes back to back in a string: 'isn''t'.

//PARSER

program: NEWLINE* declared (declared | NEWLINE)* EOF;
//declared
declared:
	(var_decl SEMICOLON)
	| (const_decl SEMICOLON)
	| func_decl
	| method_decl
	| struct_decl
	| interface_decl;
//literal
liter:INT_LIT
       | BIN_LIT
       | OCT_LIT
       | HEX_LIT
	   | FLOAT_LIT
	   | STRING_LIT
	   | TRUE
	   | FALSE
	   | NIL
	   | arr_liter
	   | struct_literal;

//basic type
all_type: INT
        | FLOAT
        | BOOLEAN
        | STRING
        | list_array_type_lit
        | ID;
basic_type: INT
          | FLOAT
          | BOOLEAN
          | STRING
          | ID;

statement:
	(
		var_decl     | const_decl
		             | ass_statement
		             | if_statement
		             | for_statement
		             | break_statement
		             | continue_statement
		             | call_statement
		             | return_statement
                     | struct_statements
                     | method_statement
	)
    end_statement;
//list literal
list_liter: list_literal_noempty | ;
list_literal_noempty: liter COMMA list_liter | liter;
list_array_type_lit: array_type_lit basic_type;
array_type_lit: array_type array_type_lit | array_type;
array_type: LSP INT_LIT RSP;
//Struct literal
struct_literal: ID LCP list_ele_lit? RCP;
list_ele_lit: list_ele COMMA list_ele_lit | list_ele;
list_ele: ID COLON expr;
//Array literal
arr_liter: dim_lit all_type LCP list_arr_ele? RCP;
dim_lit: dim dim_lit | dim;
dim: LSP INT_LIT RSP;
arr_ele: liter
       | struct_literal
       | ID LCP list_arr_ele? RCP
       | LCP list_arr_ele? RCP;

list_arr_ele: arr_ele (COMMA list_arr_ele)?;
//Expression

list_expr: expr COMMA list_expr | expr;
expr: expr OR expr1 | expr1;
expr1: expr1 AND expr2 | expr2;
expr2: expr2 (EQUAL | UNEQUAL | LT | LTE | GT | GTE) expr3 | expr3;
expr3: expr3 (ADD | SUB) expr4 | expr4;
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
expr5: (NOT | SUB) expr | expr6;
expr6: expr6 (LSP expr RSP | DOT expr) | expr7;
expr7: liter | LP expr RP | ID | ID LP functcall RP;
//function call
functcall: functcall_noempty | ;
functcall_noempty: expr | expr COMMA functcall_noempty;
//const declared
const_decl: CONST ID ASSIGN expr;
////variables declareds
var_decl: VAR ID (all_type | all_type? ASSIGN expr);
//function declared
func_decl: FUNC ID LP param_lit? RP all_type? ignore LCP (NEWLINE | list_statement)* RCP SEMICOLON;
param_lit: param COMMA param_lit | param;
param: list_ID all_type;
list_ID: ID COMMA list_ID | ID;
//method declared
method_decl: FUNC LP ID ID RP ID LP param_lit? RP all_type? ignore LCP (NEWLINE | list_statement)* RCP SEMICOLON;
//struct declared
struct_decl: TYPE ID STRUCT LCP list_statement RCP SEMICOLON;
struct_body: struct_member*;
struct_member:
    struct_statements SEMICOLON   // Fields inside struct
    | method_decl                  // Methods inside struct
    ;

//interface_declared
interface_decl: TYPE ID INTERFACE LCP list_statement RCP SEMICOLON;
//list statement
list_statement: statement list_statement | statement;
//assign statement
ass_statement: list_assignment_lhs operator expr;
operator:  COLONEQUAL | ADD_ASS | SUB_ASS | MUL_ASS | DIV_ASS | MOD_ASS;
list_assignment_lhs: assignment_lhs DOT list_assignment_lhs | assignment_lhs;
assignment_lhs: (ID (list_array_index | ));
list_array_index: array_index list_array_index | array_index;
array_index: LSP expr RSP;
//if statement
else_statement: ELSE ignore LCP (NEWLINE | list_statement)* RCP;
elif_statement: | ELSE IF LP expr RP ignore LCP (NEWLINE | list_statement)* RCP elif_statement;
if_statement: IF LP expr RP ignore LCP (NEWLINE | list_statement)* RCP NEWLINE* elif_statement NEWLINE* else_statement?;
//for statement
range_loop: ID COMMA ID COLONEQUAL RANGE expr;
init_loop: (ass_statement | var_decl) SEMICOLON expr SEMICOLON ass_statement;
basic_loop: expr;
for_statement: FOR (basic_loop | init_loop | range_loop) ignore LCP (NEWLINE | list_statement)* RCP;
//break statement
break_statement: BREAK;
//continue statement
continue_statement: CONTINUE;
//call statement
call_statement: ((list_assignment_lhs DOT) | ) ID LP (list_expr | ) RP;
//return statement
return_statement: RETURN ignore (expr | );
//end statement
end_statement: (SEMICOLON NEWLINE*) | (NEWLINE+);
//struct statement
struct_statements: ID all_type;
//method statement
method_param: ID all_type?;
method_param_lit: method_param COMMA method_param_lit | method_param;
method_statement: ID LP method_param_lit RP all_type?;

ignore: NEWLINE*;


//LEXER
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';
//operation
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQUAL: '==';
UNEQUAL: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
AND: '&&';
OR: '||';
NOT: '!';
ASSIGN: '=';
ADD_ASS: '+=';
SUB_ASS: '-=';
MUL_ASS: '*=';
DIV_ASS: '/=';
MOD_ASS: '%=';
DOT: '.';
COLON: ':';
COMMA: ',';
SEMICOLON: ';';
COLONEQUAL: ':=';
//parentheses
LP: '(';
RP: ')';
LCP: '{';
RCP: '}';
LSP: '[';
RSP: ']';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
//literals
INT_LIT: '0'| [1-9][0-9]*;
BIN_LIT: '0'[bB][0-1]+;
OCT_LIT: '0'[oO][0-7]+;
HEX_LIT: '0'[xX][0-9A-Fa-f]+;

FLOAT_LIT: DIGITS OPT_FRAC OPT_EXP?
         | DIGITS OPT_EXP;
fragment DIGIT: [0-9];
fragment DIGITS: '0' | DIGIT*;
fragment OPT_FRAC: '.' DIGIT*;
fragment OPT_EXP: [Ee][+-]? DIGITS;

STRING_LIT: '"' STRING_CHAR* '"' {self.text = self.text[1:-1]};
fragment STRING_CHAR: ~[\n\\"] | ESC_SEQ;
fragment ESC_SEQ: '\\' [ntr"\\] | '\'"';
fragment ESC_ILLEGAL: '\\' ~[ntr"\\];

BOOL_LIT: TRUE | FALSE;
NIL_LIT: NIL;

NEWLINE: '\r'? '\n' {
    if self.preType in [self.ID, self.INT_LIT, self.BIN_LIT, self.OCT_LIT,
                        self.HEX_LIT, self.STRING_LIT, self.FLOAT_LIT,
                        self.TRUE, self.FALSE, self.INT, self.FLOAT, self.STRING, self.BOOLEAN, self.NIL,
                        self.RETURN, self.CONTINUE, self.BREAK, self.CONST,
                        self.RP, self.RCP, self.RSP]:
        self.text = ";"
        self.type = self.SEMICOLON
    else:
        self.skip()
};

WS: [ \t\f\r]+ -> skip;
COMMENT_LINE: '//' ~[\n]* -> skip;
COMMENT: ('/*' (COMMENT | .)*? '*/') -> skip;
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING:'"' STRING_CHAR* ('\r\n' | '\n' | EOF){
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[1:-2])
    elif(self.text[-1] == '\n') :
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE:'"' STRING_CHAR* ESC_ILLEGAL{
    raise IllegalEscape(self.text[1:])
};