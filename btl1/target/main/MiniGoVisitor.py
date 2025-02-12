# Generated from main/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared.
    def visitDeclared(self, ctx:MiniGoParser.DeclaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#liter.
    def visitLiter(self, ctx:MiniGoParser.LiterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#all_type.
    def visitAll_type(self, ctx:MiniGoParser.All_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basic_type.
    def visitBasic_type(self, ctx:MiniGoParser.Basic_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_liter.
    def visitList_liter(self, ctx:MiniGoParser.List_literContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_literal_noempty.
    def visitList_literal_noempty(self, ctx:MiniGoParser.List_literal_noemptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_array_type_lit.
    def visitList_array_type_lit(self, ctx:MiniGoParser.List_array_type_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type_lit.
    def visitArray_type_lit(self, ctx:MiniGoParser.Array_type_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_ele_lit.
    def visitList_ele_lit(self, ctx:MiniGoParser.List_ele_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_ele.
    def visitList_ele(self, ctx:MiniGoParser.List_eleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_liter.
    def visitArr_liter(self, ctx:MiniGoParser.Arr_literContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dim_lit.
    def visitDim_lit(self, ctx:MiniGoParser.Dim_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dim.
    def visitDim(self, ctx:MiniGoParser.DimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_ele.
    def visitArr_ele(self, ctx:MiniGoParser.Arr_eleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_arr_ele.
    def visitList_arr_ele(self, ctx:MiniGoParser.List_arr_eleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_expr.
    def visitList_expr(self, ctx:MiniGoParser.List_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr1.
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr2.
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr3.
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr4.
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr5.
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr6.
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr7.
    def visitExpr7(self, ctx:MiniGoParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#functcall.
    def visitFunctcall(self, ctx:MiniGoParser.FunctcallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#functcall_noempty.
    def visitFunctcall_noempty(self, ctx:MiniGoParser.Functcall_noemptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_decl.
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl.
    def visitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_decl.
    def visitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param_lit.
    def visitParam_lit(self, ctx:MiniGoParser.Param_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param.
    def visitParam(self, ctx:MiniGoParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_ID.
    def visitList_ID(self, ctx:MiniGoParser.List_IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_decl.
    def visitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_decl.
    def visitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_decl.
    def visitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_statement.
    def visitList_statement(self, ctx:MiniGoParser.List_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ass_statement.
    def visitAss_statement(self, ctx:MiniGoParser.Ass_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#operator.
    def visitOperator(self, ctx:MiniGoParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_assignment_lhs.
    def visitList_assignment_lhs(self, ctx:MiniGoParser.List_assignment_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment_lhs.
    def visitAssignment_lhs(self, ctx:MiniGoParser.Assignment_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_array_index.
    def visitList_array_index(self, ctx:MiniGoParser.List_array_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_index.
    def visitArray_index(self, ctx:MiniGoParser.Array_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_statement.
    def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elif_statement.
    def visitElif_statement(self, ctx:MiniGoParser.Elif_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#range_loop.
    def visitRange_loop(self, ctx:MiniGoParser.Range_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#init_loop.
    def visitInit_loop(self, ctx:MiniGoParser.Init_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basic_loop.
    def visitBasic_loop(self, ctx:MiniGoParser.Basic_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_statement.
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_statement.
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#end_statement.
    def visitEnd_statement(self, ctx:MiniGoParser.End_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_statements.
    def visitStruct_statements(self, ctx:MiniGoParser.Struct_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_param.
    def visitMethod_param(self, ctx:MiniGoParser.Method_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_param_lit.
    def visitMethod_param_lit(self, ctx:MiniGoParser.Method_param_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_statement.
    def visitMethod_statement(self, ctx:MiniGoParser.Method_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ignore.
    def visitIgnore(self, ctx:MiniGoParser.IgnoreContext):
        return self.visitChildren(ctx)



del MiniGoParser