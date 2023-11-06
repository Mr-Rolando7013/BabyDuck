# Generated from ./baby_duck.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .baby_duckParser import baby_duckParser
else:
    from baby_duckParser import baby_duckParser

# This class defines a complete listener for a parse tree produced by baby_duckParser.
class baby_duckListener(ParseTreeListener):

    # Enter a parse tree produced by baby_duckParser#programRule.
    def enterProgramRule(self, ctx:baby_duckParser.ProgramRuleContext):
        pass

    # Exit a parse tree produced by baby_duckParser#programRule.
    def exitProgramRule(self, ctx:baby_duckParser.ProgramRuleContext):
        pass


    # Enter a parse tree produced by baby_duckParser#programa.
    def enterPrograma(self, ctx:baby_duckParser.ProgramaContext):
        pass

    # Exit a parse tree produced by baby_duckParser#programa.
    def exitPrograma(self, ctx:baby_duckParser.ProgramaContext):
        pass


    # Enter a parse tree produced by baby_duckParser#main.
    def enterMain(self, ctx:baby_duckParser.MainContext):
        pass

    # Exit a parse tree produced by baby_duckParser#main.
    def exitMain(self, ctx:baby_duckParser.MainContext):
        pass


    # Enter a parse tree produced by baby_duckParser#end.
    def enterEnd(self, ctx:baby_duckParser.EndContext):
        pass

    # Exit a parse tree produced by baby_duckParser#end.
    def exitEnd(self, ctx:baby_duckParser.EndContext):
        pass


    # Enter a parse tree produced by baby_duckParser#var.
    def enterVar(self, ctx:baby_duckParser.VarContext):
        pass

    # Exit a parse tree produced by baby_duckParser#var.
    def exitVar(self, ctx:baby_duckParser.VarContext):
        pass


    # Enter a parse tree produced by baby_duckParser#void.
    def enterVoid(self, ctx:baby_duckParser.VoidContext):
        pass

    # Exit a parse tree produced by baby_duckParser#void.
    def exitVoid(self, ctx:baby_duckParser.VoidContext):
        pass


    # Enter a parse tree produced by baby_duckParser#int.
    def enterInt(self, ctx:baby_duckParser.IntContext):
        pass

    # Exit a parse tree produced by baby_duckParser#int.
    def exitInt(self, ctx:baby_duckParser.IntContext):
        pass


    # Enter a parse tree produced by baby_duckParser#float.
    def enterFloat(self, ctx:baby_duckParser.FloatContext):
        pass

    # Exit a parse tree produced by baby_duckParser#float.
    def exitFloat(self, ctx:baby_duckParser.FloatContext):
        pass


    # Enter a parse tree produced by baby_duckParser#else.
    def enterElse(self, ctx:baby_duckParser.ElseContext):
        pass

    # Exit a parse tree produced by baby_duckParser#else.
    def exitElse(self, ctx:baby_duckParser.ElseContext):
        pass


    # Enter a parse tree produced by baby_duckParser#if.
    def enterIf(self, ctx:baby_duckParser.IfContext):
        pass

    # Exit a parse tree produced by baby_duckParser#if.
    def exitIf(self, ctx:baby_duckParser.IfContext):
        pass


    # Enter a parse tree produced by baby_duckParser#while.
    def enterWhile(self, ctx:baby_duckParser.WhileContext):
        pass

    # Exit a parse tree produced by baby_duckParser#while.
    def exitWhile(self, ctx:baby_duckParser.WhileContext):
        pass


    # Enter a parse tree produced by baby_duckParser#do.
    def enterDo(self, ctx:baby_duckParser.DoContext):
        pass

    # Exit a parse tree produced by baby_duckParser#do.
    def exitDo(self, ctx:baby_duckParser.DoContext):
        pass


    # Enter a parse tree produced by baby_duckParser#expression.
    def enterExpression(self, ctx:baby_duckParser.ExpressionContext):
        pass

    # Exit a parse tree produced by baby_duckParser#expression.
    def exitExpression(self, ctx:baby_duckParser.ExpressionContext):
        pass


    # Enter a parse tree produced by baby_duckParser#exp.
    def enterExp(self, ctx:baby_duckParser.ExpContext):
        pass

    # Exit a parse tree produced by baby_duckParser#exp.
    def exitExp(self, ctx:baby_duckParser.ExpContext):
        pass


    # Enter a parse tree produced by baby_duckParser#term.
    def enterTerm(self, ctx:baby_duckParser.TermContext):
        pass

    # Exit a parse tree produced by baby_duckParser#term.
    def exitTerm(self, ctx:baby_duckParser.TermContext):
        pass


    # Enter a parse tree produced by baby_duckParser#factor.
    def enterFactor(self, ctx:baby_duckParser.FactorContext):
        pass

    # Exit a parse tree produced by baby_duckParser#factor.
    def exitFactor(self, ctx:baby_duckParser.FactorContext):
        pass


    # Enter a parse tree produced by baby_duckParser#body.
    def enterBody(self, ctx:baby_duckParser.BodyContext):
        pass

    # Exit a parse tree produced by baby_duckParser#body.
    def exitBody(self, ctx:baby_duckParser.BodyContext):
        pass


    # Enter a parse tree produced by baby_duckParser#assign.
    def enterAssign(self, ctx:baby_duckParser.AssignContext):
        pass

    # Exit a parse tree produced by baby_duckParser#assign.
    def exitAssign(self, ctx:baby_duckParser.AssignContext):
        pass


    # Enter a parse tree produced by baby_duckParser#condition.
    def enterCondition(self, ctx:baby_duckParser.ConditionContext):
        pass

    # Exit a parse tree produced by baby_duckParser#condition.
    def exitCondition(self, ctx:baby_duckParser.ConditionContext):
        pass


    # Enter a parse tree produced by baby_duckParser#cycle.
    def enterCycle(self, ctx:baby_duckParser.CycleContext):
        pass

    # Exit a parse tree produced by baby_duckParser#cycle.
    def exitCycle(self, ctx:baby_duckParser.CycleContext):
        pass


    # Enter a parse tree produced by baby_duckParser#print.
    def enterPrint(self, ctx:baby_duckParser.PrintContext):
        pass

    # Exit a parse tree produced by baby_duckParser#print.
    def exitPrint(self, ctx:baby_duckParser.PrintContext):
        pass


    # Enter a parse tree produced by baby_duckParser#functionCall.
    def enterFunctionCall(self, ctx:baby_duckParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by baby_duckParser#functionCall.
    def exitFunctionCall(self, ctx:baby_duckParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by baby_duckParser#type.
    def enterType(self, ctx:baby_duckParser.TypeContext):
        pass

    # Exit a parse tree produced by baby_duckParser#type.
    def exitType(self, ctx:baby_duckParser.TypeContext):
        pass


    # Enter a parse tree produced by baby_duckParser#variables.
    def enterVariables(self, ctx:baby_duckParser.VariablesContext):
        pass

    # Exit a parse tree produced by baby_duckParser#variables.
    def exitVariables(self, ctx:baby_duckParser.VariablesContext):
        pass


    # Enter a parse tree produced by baby_duckParser#listvars.
    def enterListvars(self, ctx:baby_duckParser.ListvarsContext):
        pass

    # Exit a parse tree produced by baby_duckParser#listvars.
    def exitListvars(self, ctx:baby_duckParser.ListvarsContext):
        pass


    # Enter a parse tree produced by baby_duckParser#listaId.
    def enterListaId(self, ctx:baby_duckParser.ListaIdContext):
        pass

    # Exit a parse tree produced by baby_duckParser#listaId.
    def exitListaId(self, ctx:baby_duckParser.ListaIdContext):
        pass


    # Enter a parse tree produced by baby_duckParser#idExtra.
    def enterIdExtra(self, ctx:baby_duckParser.IdExtraContext):
        pass

    # Exit a parse tree produced by baby_duckParser#idExtra.
    def exitIdExtra(self, ctx:baby_duckParser.IdExtraContext):
        pass


    # Enter a parse tree produced by baby_duckParser#function.
    def enterFunction(self, ctx:baby_duckParser.FunctionContext):
        pass

    # Exit a parse tree produced by baby_duckParser#function.
    def exitFunction(self, ctx:baby_duckParser.FunctionContext):
        pass


    # Enter a parse tree produced by baby_duckParser#parameters.
    def enterParameters(self, ctx:baby_duckParser.ParametersContext):
        pass

    # Exit a parse tree produced by baby_duckParser#parameters.
    def exitParameters(self, ctx:baby_duckParser.ParametersContext):
        pass


    # Enter a parse tree produced by baby_duckParser#parameter.
    def enterParameter(self, ctx:baby_duckParser.ParameterContext):
        pass

    # Exit a parse tree produced by baby_duckParser#parameter.
    def exitParameter(self, ctx:baby_duckParser.ParameterContext):
        pass


    # Enter a parse tree produced by baby_duckParser#program.
    def enterProgram(self, ctx:baby_duckParser.ProgramContext):
        pass

    # Exit a parse tree produced by baby_duckParser#program.
    def exitProgram(self, ctx:baby_duckParser.ProgramContext):
        pass


    # Enter a parse tree produced by baby_duckParser#statement.
    def enterStatement(self, ctx:baby_duckParser.StatementContext):
        pass

    # Exit a parse tree produced by baby_duckParser#statement.
    def exitStatement(self, ctx:baby_duckParser.StatementContext):
        pass



del baby_duckParser