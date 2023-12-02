# Generated from ./baby_duck.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from symbol_table import *
symbol_table1 = SymbolTable()
current_scope = 0


def serializedATN():
    return [
        4,1,34,313,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,0,1,0,1,
        1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,
        9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,12,1,12,3,12,95,8,12,
        1,12,1,12,1,12,1,12,5,12,101,8,12,10,12,12,12,104,9,12,1,12,1,12,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,116,8,13,10,13,12,13,
        119,9,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,129,8,14,10,
        14,12,14,132,9,14,1,15,3,15,135,8,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,149,8,15,1,16,1,16,5,16,153,
        8,16,10,16,12,16,156,9,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,176,8,18,
        1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,199,8,20,1,20,1,20,
        1,20,3,20,204,8,20,5,20,206,8,20,10,20,12,20,209,9,20,1,20,1,20,
        1,20,1,21,1,21,1,21,1,21,1,21,5,21,219,8,21,10,21,12,21,222,9,21,
        3,21,224,8,21,1,21,1,21,1,21,1,22,1,22,3,22,231,8,22,1,23,1,23,5,
        23,235,8,23,10,23,12,23,238,9,23,1,24,1,24,1,24,1,24,1,24,1,24,1,
        25,1,25,1,25,1,26,1,26,3,26,251,8,26,1,27,1,27,1,27,1,27,1,27,1,
        27,5,27,259,8,27,10,27,12,27,262,9,27,1,27,1,27,1,27,3,27,267,8,
        27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,5,28,278,8,28,10,
        28,12,28,281,9,28,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,3,
        30,292,8,30,1,30,1,30,5,30,296,8,30,10,30,12,30,299,9,30,1,30,1,
        30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,3,31,311,8,31,1,31,0,
        0,32,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,0,1,1,0,15,16,310,0,64,1,0,0,0,2,67,
        1,0,0,0,4,69,1,0,0,0,6,71,1,0,0,0,8,73,1,0,0,0,10,75,1,0,0,0,12,
        77,1,0,0,0,14,79,1,0,0,0,16,81,1,0,0,0,18,83,1,0,0,0,20,85,1,0,0,
        0,22,87,1,0,0,0,24,89,1,0,0,0,26,107,1,0,0,0,28,120,1,0,0,0,30,134,
        1,0,0,0,32,150,1,0,0,0,34,159,1,0,0,0,36,165,1,0,0,0,38,180,1,0,
        0,0,40,191,1,0,0,0,42,213,1,0,0,0,44,230,1,0,0,0,46,232,1,0,0,0,
        48,239,1,0,0,0,50,245,1,0,0,0,52,250,1,0,0,0,54,252,1,0,0,0,56,274,
        1,0,0,0,58,282,1,0,0,0,60,287,1,0,0,0,62,310,1,0,0,0,64,65,3,60,
        30,0,65,66,5,0,0,1,66,1,1,0,0,0,67,68,5,1,0,0,68,3,1,0,0,0,69,70,
        5,2,0,0,70,5,1,0,0,0,71,72,5,3,0,0,72,7,1,0,0,0,73,74,5,4,0,0,74,
        9,1,0,0,0,75,76,5,5,0,0,76,11,1,0,0,0,77,78,5,6,0,0,78,13,1,0,0,
        0,79,80,5,7,0,0,80,15,1,0,0,0,81,82,5,8,0,0,82,17,1,0,0,0,83,84,
        5,9,0,0,84,19,1,0,0,0,85,86,5,10,0,0,86,21,1,0,0,0,87,88,5,11,0,
        0,88,23,1,0,0,0,89,102,3,26,13,0,90,91,5,12,0,0,91,95,6,12,-1,0,
        92,93,5,13,0,0,93,95,6,12,-1,0,94,90,1,0,0,0,94,92,1,0,0,0,95,96,
        1,0,0,0,96,101,3,26,13,0,97,98,5,14,0,0,98,99,6,12,-1,0,99,101,3,
        26,13,0,100,94,1,0,0,0,100,97,1,0,0,0,101,104,1,0,0,0,102,100,1,
        0,0,0,102,103,1,0,0,0,103,105,1,0,0,0,104,102,1,0,0,0,105,106,6,
        12,-1,0,106,25,1,0,0,0,107,108,3,28,14,0,108,117,6,13,-1,0,109,110,
        5,15,0,0,110,111,6,13,-1,0,111,116,3,26,13,0,112,113,5,16,0,0,113,
        114,6,13,-1,0,114,116,3,26,13,0,115,109,1,0,0,0,115,112,1,0,0,0,
        116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,27,1,0,0,0,119,
        117,1,0,0,0,120,121,3,30,15,0,121,130,6,14,-1,0,122,123,5,17,0,0,
        123,124,6,14,-1,0,124,129,3,28,14,0,125,126,5,18,0,0,126,127,6,14,
        -1,0,127,129,3,28,14,0,128,122,1,0,0,0,128,125,1,0,0,0,129,132,1,
        0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,29,1,0,0,0,132,130,1,0,
        0,0,133,135,7,0,0,0,134,133,1,0,0,0,134,135,1,0,0,0,135,148,1,0,
        0,0,136,137,5,30,0,0,137,149,6,15,-1,0,138,139,5,32,0,0,139,149,
        6,15,-1,0,140,141,5,33,0,0,141,149,6,15,-1,0,142,143,5,19,0,0,143,
        144,6,15,-1,0,144,145,3,24,12,0,145,146,5,20,0,0,146,147,6,15,-1,
        0,147,149,1,0,0,0,148,136,1,0,0,0,148,138,1,0,0,0,148,140,1,0,0,
        0,148,142,1,0,0,0,149,31,1,0,0,0,150,154,5,21,0,0,151,153,3,62,31,
        0,152,151,1,0,0,0,153,156,1,0,0,0,154,152,1,0,0,0,154,155,1,0,0,
        0,155,157,1,0,0,0,156,154,1,0,0,0,157,158,5,22,0,0,158,33,1,0,0,
        0,159,160,5,30,0,0,160,161,5,23,0,0,161,162,3,24,12,0,162,163,6,
        17,-1,0,163,164,5,24,0,0,164,35,1,0,0,0,165,166,3,18,9,0,166,167,
        5,19,0,0,167,168,3,24,12,0,168,169,5,20,0,0,169,170,6,18,-1,0,170,
        175,3,32,16,0,171,172,3,16,8,0,172,173,6,18,-1,0,173,174,3,32,16,
        0,174,176,1,0,0,0,175,171,1,0,0,0,175,176,1,0,0,0,176,177,1,0,0,
        0,177,178,6,18,-1,0,178,179,5,24,0,0,179,37,1,0,0,0,180,181,3,20,
        10,0,181,182,6,19,-1,0,182,183,3,32,16,0,183,184,3,22,11,0,184,185,
        5,19,0,0,185,186,3,24,12,0,186,187,5,20,0,0,187,188,6,19,-1,0,188,
        189,6,19,-1,0,189,190,5,24,0,0,190,39,1,0,0,0,191,192,5,25,0,0,192,
        198,5,19,0,0,193,194,3,24,12,0,194,195,6,20,-1,0,195,199,1,0,0,0,
        196,197,5,31,0,0,197,199,6,20,-1,0,198,193,1,0,0,0,198,196,1,0,0,
        0,199,207,1,0,0,0,200,203,5,26,0,0,201,204,3,24,12,0,202,204,5,31,
        0,0,203,201,1,0,0,0,203,202,1,0,0,0,204,206,1,0,0,0,205,200,1,0,
        0,0,206,209,1,0,0,0,207,205,1,0,0,0,207,208,1,0,0,0,208,210,1,0,
        0,0,209,207,1,0,0,0,210,211,5,20,0,0,211,212,5,24,0,0,212,41,1,0,
        0,0,213,214,5,30,0,0,214,223,5,19,0,0,215,220,3,24,12,0,216,217,
        5,26,0,0,217,219,3,24,12,0,218,216,1,0,0,0,219,222,1,0,0,0,220,218,
        1,0,0,0,220,221,1,0,0,0,221,224,1,0,0,0,222,220,1,0,0,0,223,215,
        1,0,0,0,223,224,1,0,0,0,224,225,1,0,0,0,225,226,5,20,0,0,226,227,
        5,24,0,0,227,43,1,0,0,0,228,231,3,12,6,0,229,231,3,14,7,0,230,228,
        1,0,0,0,230,229,1,0,0,0,231,45,1,0,0,0,232,236,3,8,4,0,233,235,3,
        48,24,0,234,233,1,0,0,0,235,238,1,0,0,0,236,234,1,0,0,0,236,237,
        1,0,0,0,237,47,1,0,0,0,238,236,1,0,0,0,239,240,3,50,25,0,240,241,
        5,27,0,0,241,242,3,44,22,0,242,243,5,24,0,0,243,244,6,24,-1,0,244,
        49,1,0,0,0,245,246,5,30,0,0,246,247,3,52,26,0,247,51,1,0,0,0,248,
        249,5,26,0,0,249,251,3,50,25,0,250,248,1,0,0,0,250,251,1,0,0,0,251,
        53,1,0,0,0,252,253,6,27,-1,0,253,254,3,10,5,0,254,255,6,27,-1,0,
        255,256,5,30,0,0,256,260,5,19,0,0,257,259,3,56,28,0,258,257,1,0,
        0,0,259,262,1,0,0,0,260,258,1,0,0,0,260,261,1,0,0,0,261,263,1,0,
        0,0,262,260,1,0,0,0,263,264,5,20,0,0,264,266,5,28,0,0,265,267,3,
        46,23,0,266,265,1,0,0,0,266,267,1,0,0,0,267,268,1,0,0,0,268,269,
        3,32,16,0,269,270,6,27,-1,0,270,271,5,29,0,0,271,272,5,24,0,0,272,
        273,6,27,-1,0,273,55,1,0,0,0,274,279,3,58,29,0,275,276,5,26,0,0,
        276,278,3,58,29,0,277,275,1,0,0,0,278,281,1,0,0,0,279,277,1,0,0,
        0,279,280,1,0,0,0,280,57,1,0,0,0,281,279,1,0,0,0,282,283,5,30,0,
        0,283,284,5,27,0,0,284,285,3,44,22,0,285,286,6,29,-1,0,286,59,1,
        0,0,0,287,288,3,2,1,0,288,289,5,30,0,0,289,291,5,24,0,0,290,292,
        3,46,23,0,291,290,1,0,0,0,291,292,1,0,0,0,292,293,1,0,0,0,293,297,
        6,30,-1,0,294,296,3,54,27,0,295,294,1,0,0,0,296,299,1,0,0,0,297,
        295,1,0,0,0,297,298,1,0,0,0,298,300,1,0,0,0,299,297,1,0,0,0,300,
        301,3,4,2,0,301,302,3,32,16,0,302,303,3,6,3,0,303,304,6,30,-1,0,
        304,61,1,0,0,0,305,311,3,34,17,0,306,311,3,36,18,0,307,311,3,38,
        19,0,308,311,3,40,20,0,309,311,3,42,21,0,310,305,1,0,0,0,310,306,
        1,0,0,0,310,307,1,0,0,0,310,308,1,0,0,0,310,309,1,0,0,0,311,63,1,
        0,0,0,25,94,100,102,115,117,128,130,134,148,154,175,198,203,207,
        220,223,230,236,250,260,266,279,291,297,310
    ]

class baby_duckParser ( Parser ):

    grammarFileName = "baby_duck.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'main'", "'end'", "'var'", 
                     "'void'", "'int'", "'float'", "'else'", "'if'", "'while'", 
                     "'do'", "'>'", "'<'", "'!='", "'+'", "'-'", "'*'", 
                     "'/'", "'('", "')'", "'{'", "'}'", "'='", "';'", "'print'", 
                     "','", "':'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "Id", "CTE_STRING", "CTE_INT", 
                      "CTE_FLOAT", "WS" ]

    RULE_programRule = 0
    RULE_programa = 1
    RULE_main = 2
    RULE_end = 3
    RULE_var = 4
    RULE_void = 5
    RULE_int = 6
    RULE_float = 7
    RULE_else = 8
    RULE_if = 9
    RULE_while = 10
    RULE_do = 11
    RULE_expression = 12
    RULE_exp = 13
    RULE_term = 14
    RULE_factor = 15
    RULE_body = 16
    RULE_assign = 17
    RULE_condition = 18
    RULE_cycle = 19
    RULE_print = 20
    RULE_functionCall = 21
    RULE_type = 22
    RULE_variables = 23
    RULE_listvars = 24
    RULE_listaId = 25
    RULE_idExtra = 26
    RULE_function = 27
    RULE_parameters = 28
    RULE_parameter = 29
    RULE_program = 30
    RULE_statement = 31

    ruleNames =  [ "programRule", "programa", "main", "end", "var", "void", 
                   "int", "float", "else", "if", "while", "do", "expression", 
                   "exp", "term", "factor", "body", "assign", "condition", 
                   "cycle", "print", "functionCall", "type", "variables", 
                   "listvars", "listaId", "idExtra", "function", "parameters", 
                   "parameter", "program", "statement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    Id=30
    CTE_STRING=31
    CTE_INT=32
    CTE_FLOAT=33
    WS=34

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None








    class ProgramRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program(self):
            return self.getTypedRuleContext(baby_duckParser.ProgramContext,0)


        def EOF(self):
            return self.getToken(baby_duckParser.EOF, 0)

        def getRuleIndex(self):
            return baby_duckParser.RULE_programRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgramRule" ):
                listener.enterProgramRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgramRule" ):
                listener.exitProgramRule(self)




    def programRule(self):

        localctx = baby_duckParser.ProgramRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.program()
            self.state = 65
            self.match(baby_duckParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return baby_duckParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = baby_duckParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(baby_duckParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return baby_duckParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = baby_duckParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(baby_duckParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return baby_duckParser.RULE_end

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnd" ):
                listener.enterEnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnd" ):
                listener.exitEnd(self)




    def end(self):

        localctx = baby_duckParser.EndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(baby_duckParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return baby_duckParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)




    def var(self):

        localctx = baby_duckParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(baby_duckParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return baby_duckParser.RULE_void

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoid" ):
                listener.enterVoid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoid" ):
                listener.exitVoid(self)




    def void(self):

        localctx = baby_duckParser.VoidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_void)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(baby_duckParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return baby_duckParser.RULE_int

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)




    def int_(self):

        localctx = baby_duckParser.IntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(baby_duckParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return baby_duckParser.RULE_float

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)




    def float_(self):

        localctx = baby_duckParser.FloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(baby_duckParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return baby_duckParser.RULE_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse" ):
                listener.enterElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse" ):
                listener.exitElse(self)




    def else_(self):

        localctx = baby_duckParser.ElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(baby_duckParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return baby_duckParser.RULE_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)




    def if_(self):

        localctx = baby_duckParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(baby_duckParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return baby_duckParser.RULE_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)




    def while_(self):

        localctx = baby_duckParser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(baby_duckParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return baby_duckParser.RULE_do

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDo" ):
                listener.enterDo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDo" ):
                listener.exitDo(self)




    def do(self):

        localctx = baby_duckParser.DoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_do)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(baby_duckParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duckParser.ExpContext)
            else:
                return self.getTypedRuleContext(baby_duckParser.ExpContext,i)


        def getRuleIndex(self):
            return baby_duckParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = baby_duckParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.exp()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0):
                self.state = 100
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12, 13]:
                    self.state = 94
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [12]:
                        self.state = 90
                        self.match(baby_duckParser.T__11)
                        symbol_table1.push_operator('>')
                        pass
                    elif token in [13]:
                        self.state = 92
                        self.match(baby_duckParser.T__12)
                        symbol_table1.push_operator('<')
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 96
                    self.exp()
                    pass
                elif token in [14]:
                    self.state = 97
                    self.match(baby_duckParser.T__13)
                    symbol_table1.push_operator('!=')
                    self.state = 99
                    self.exp()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            symbol_table1.push_term_mas_menos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(baby_duckParser.TermContext,0)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duckParser.ExpContext)
            else:
                return self.getTypedRuleContext(baby_duckParser.ExpContext,i)


        def getRuleIndex(self):
            return baby_duckParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = baby_duckParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.term()
            symbol_table1.push_term()
            self.state = 117
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 115
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [15]:
                        self.state = 109
                        self.match(baby_duckParser.T__14)
                        symbol_table1.push_operator('+')
                        self.state = 111
                        self.exp()
                        pass
                    elif token in [16]:
                        self.state = 112
                        self.match(baby_duckParser.T__15)
                        symbol_table1.push_operator('-')
                        self.state = 114
                        self.exp()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 119
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(baby_duckParser.FactorContext,0)


        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duckParser.TermContext)
            else:
                return self.getTypedRuleContext(baby_duckParser.TermContext,i)


        def getRuleIndex(self):
            return baby_duckParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = baby_duckParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.factor()
            symbol_table1.push_term_multiplication()
            self.state = 130
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 128
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [17]:
                        self.state = 122
                        self.match(baby_duckParser.T__16)
                        symbol_table1.push_operator('*')
                        self.state = 124
                        self.term()
                        pass
                    elif token in [18]:
                        self.state = 125
                        self.match(baby_duckParser.T__17)
                        symbol_table1.push_operator('/')
                        self.state = 127
                        self.term()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 132
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._Id = None # Token
            self._CTE_INT = None # Token
            self._CTE_FLOAT = None # Token

        def Id(self):
            return self.getToken(baby_duckParser.Id, 0)

        def CTE_INT(self):
            return self.getToken(baby_duckParser.CTE_INT, 0)

        def CTE_FLOAT(self):
            return self.getToken(baby_duckParser.CTE_FLOAT, 0)

        def expression(self):
            return self.getTypedRuleContext(baby_duckParser.ExpressionContext,0)


        def getRuleIndex(self):
            return baby_duckParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = baby_duckParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15 or _la==16:
                self.state = 133
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.state = 136
                localctx._Id = self.match(baby_duckParser.Id)
                symbol_table1.push_factor((None if localctx._Id is None else localctx._Id.text), None, False)
                pass
            elif token in [32]:
                self.state = 138
                localctx._CTE_INT = self.match(baby_duckParser.CTE_INT)
                symbol_table1.push_factor((None if localctx._CTE_INT is None else localctx._CTE_INT.text), "int", True)
                pass
            elif token in [33]:
                self.state = 140
                localctx._CTE_FLOAT = self.match(baby_duckParser.CTE_FLOAT)
                symbol_table1.push_factor((None if localctx._CTE_FLOAT is None else localctx._CTE_FLOAT.text), "float", True)
                pass
            elif token in [19]:
                self.state = 142
                self.match(baby_duckParser.T__18)
                symbol_table1.push_parentesis('(')
                self.state = 144
                self.expression()
                self.state = 145
                self.match(baby_duckParser.T__19)
                symbol_table1.pop_parentesis()
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


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duckParser.StatementContext)
            else:
                return self.getTypedRuleContext(baby_duckParser.StatementContext,i)


        def getRuleIndex(self):
            return baby_duckParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = baby_duckParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(baby_duckParser.T__20)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1107297792) != 0):
                self.state = 151
                self.statement()
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 157
            self.match(baby_duckParser.T__21)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._Id = None # Token

        def Id(self):
            return self.getToken(baby_duckParser.Id, 0)

        def expression(self):
            return self.getTypedRuleContext(baby_duckParser.ExpressionContext,0)


        def getRuleIndex(self):
            return baby_duckParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = baby_duckParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            localctx._Id = self.match(baby_duckParser.Id)
            self.state = 160
            self.match(baby_duckParser.T__22)
            self.state = 161
            self.expression()
            symbol_table1.assign_value((None if localctx._Id is None else localctx._Id.text), '=')
            self.state = 163
            self.match(baby_duckParser.T__23)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_(self):
            return self.getTypedRuleContext(baby_duckParser.IfContext,0)


        def expression(self):
            return self.getTypedRuleContext(baby_duckParser.ExpressionContext,0)


        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duckParser.BodyContext)
            else:
                return self.getTypedRuleContext(baby_duckParser.BodyContext,i)


        def else_(self):
            return self.getTypedRuleContext(baby_duckParser.ElseContext,0)


        def getRuleIndex(self):
            return baby_duckParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = baby_duckParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.if_()
            self.state = 166
            self.match(baby_duckParser.T__18)
            self.state = 167
            self.expression()
            self.state = 168
            self.match(baby_duckParser.T__19)
            symbol_table1.push_if()
            self.state = 170
            self.body()
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 171
                self.else_()
                symbol_table1.push_else()
                self.state = 173
                self.body()


            symbol_table1.push_if_finish()
            self.state = 178
            self.match(baby_duckParser.T__23)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CycleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def while_(self):
            return self.getTypedRuleContext(baby_duckParser.WhileContext,0)


        def body(self):
            return self.getTypedRuleContext(baby_duckParser.BodyContext,0)


        def do(self):
            return self.getTypedRuleContext(baby_duckParser.DoContext,0)


        def expression(self):
            return self.getTypedRuleContext(baby_duckParser.ExpressionContext,0)


        def getRuleIndex(self):
            return baby_duckParser.RULE_cycle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCycle" ):
                listener.enterCycle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCycle" ):
                listener.exitCycle(self)




    def cycle(self):

        localctx = baby_duckParser.CycleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_cycle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.while_()
            symbol_table1.push_while()
            self.state = 182
            self.body()
            self.state = 183
            self.do()
            self.state = 184
            self.match(baby_duckParser.T__18)
            self.state = 185
            self.expression()
            self.state = 186
            self.match(baby_duckParser.T__19)
            symbol_table1.push_if()
            symbol_table1.push_while_end()
            self.state = 189
            self.match(baby_duckParser.T__23)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._CTE_STRING = None # Token

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duckParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(baby_duckParser.ExpressionContext,i)


        def CTE_STRING(self, i:int=None):
            if i is None:
                return self.getTokens(baby_duckParser.CTE_STRING)
            else:
                return self.getToken(baby_duckParser.CTE_STRING, i)

        def getRuleIndex(self):
            return baby_duckParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)




    def print_(self):

        localctx = baby_duckParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_print)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(baby_duckParser.T__24)
            self.state = 192
            self.match(baby_duckParser.T__18)
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16, 19, 30, 32, 33]:
                self.state = 193
                self.expression()
                symbol_table1.print_function()
                pass
            elif token in [31]:
                self.state = 196
                localctx._CTE_STRING = self.match(baby_duckParser.CTE_STRING)
                symbol_table1.push_factor((None if localctx._CTE_STRING is None else localctx._CTE_STRING.text), "string", True); symbol_table1.print_function()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 200
                self.match(baby_duckParser.T__25)
                self.state = 203
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [15, 16, 19, 30, 32, 33]:
                    self.state = 201
                    self.expression()
                    pass
                elif token in [31]:
                    self.state = 202
                    localctx._CTE_STRING = self.match(baby_duckParser.CTE_STRING)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 210
            self.match(baby_duckParser.T__19)
            self.state = 211
            self.match(baby_duckParser.T__23)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(baby_duckParser.Id, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duckParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(baby_duckParser.ExpressionContext,i)


        def getRuleIndex(self):
            return baby_duckParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = baby_duckParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(baby_duckParser.Id)
            self.state = 214
            self.match(baby_duckParser.T__18)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 13959266304) != 0):
                self.state = 215
                self.expression()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==26:
                    self.state = 216
                    self.match(baby_duckParser.T__25)
                    self.state = 217
                    self.expression()
                    self.state = 222
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 225
            self.match(baby_duckParser.T__19)
            self.state = 226
            self.match(baby_duckParser.T__23)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_(self):
            return self.getTypedRuleContext(baby_duckParser.IntContext,0)


        def float_(self):
            return self.getTypedRuleContext(baby_duckParser.FloatContext,0)


        def getRuleIndex(self):
            return baby_duckParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = baby_duckParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_type)
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.int_()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.float_()
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


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(baby_duckParser.VarContext,0)


        def listvars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duckParser.ListvarsContext)
            else:
                return self.getTypedRuleContext(baby_duckParser.ListvarsContext,i)


        def getRuleIndex(self):
            return baby_duckParser.RULE_variables

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariables" ):
                listener.enterVariables(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariables" ):
                listener.exitVariables(self)




    def variables(self):

        localctx = baby_duckParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_variables)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.var()
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 233
                self.listvars()
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListvarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._listaId = None # ListaIdContext
            self._type = None # TypeContext

        def listaId(self):
            return self.getTypedRuleContext(baby_duckParser.ListaIdContext,0)


        def type_(self):
            return self.getTypedRuleContext(baby_duckParser.TypeContext,0)


        def getRuleIndex(self):
            return baby_duckParser.RULE_listvars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListvars" ):
                listener.enterListvars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListvars" ):
                listener.exitListvars(self)




    def listvars(self):

        localctx = baby_duckParser.ListvarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_listvars)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            localctx._listaId = self.listaId()
            self.state = 240
            self.match(baby_duckParser.T__26)
            self.state = 241
            localctx._type = self.type_()
            self.state = 242
            self.match(baby_duckParser.T__23)

            symbol_table1.add_symbol((None if localctx._listaId is None else self._input.getText(localctx._listaId.start,localctx._listaId.stop)), (None if localctx._type is None else self._input.getText(localctx._type.start,localctx._type.stop)), current_scope);

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(baby_duckParser.Id, 0)

        def idExtra(self):
            return self.getTypedRuleContext(baby_duckParser.IdExtraContext,0)


        def getRuleIndex(self):
            return baby_duckParser.RULE_listaId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaId" ):
                listener.enterListaId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaId" ):
                listener.exitListaId(self)




    def listaId(self):

        localctx = baby_duckParser.ListaIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_listaId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(baby_duckParser.Id)
            self.state = 246
            self.idExtra()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdExtraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listaId(self):
            return self.getTypedRuleContext(baby_duckParser.ListaIdContext,0)


        def getRuleIndex(self):
            return baby_duckParser.RULE_idExtra

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExtra" ):
                listener.enterIdExtra(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExtra" ):
                listener.exitIdExtra(self)




    def idExtra(self):

        localctx = baby_duckParser.IdExtraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_idExtra)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 248
                self.match(baby_duckParser.T__25)
                self.state = 249
                self.listaId()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._Id = None # Token
            self._parameters = None # ParametersContext
            self._variables = None # VariablesContext

        def void(self):
            return self.getTypedRuleContext(baby_duckParser.VoidContext,0)


        def Id(self):
            return self.getToken(baby_duckParser.Id, 0)

        def body(self):
            return self.getTypedRuleContext(baby_duckParser.BodyContext,0)


        def parameters(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duckParser.ParametersContext)
            else:
                return self.getTypedRuleContext(baby_duckParser.ParametersContext,i)


        def variables(self):
            return self.getTypedRuleContext(baby_duckParser.VariablesContext,0)


        def getRuleIndex(self):
            return baby_duckParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = baby_duckParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            global current_scope
            self.state = 253
            self.void()
            current_scope+=1
            self.state = 255
            localctx._Id = self.match(baby_duckParser.Id)
            self.state = 256
            self.match(baby_duckParser.T__18)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 257
                localctx._parameters = self.parameters()
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 263
            self.match(baby_duckParser.T__19)
            self.state = 264
            self.match(baby_duckParser.T__27)
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 265
                localctx._variables = self.variables()


            self.state = 268
            self.body()
            symbol_table1.add_function((None if localctx._Id is None else localctx._Id.text), (None if localctx._parameters is None else self._input.getText(localctx._parameters.start,localctx._parameters.stop)), (None if localctx._variables is None else self._input.getText(localctx._variables.start,localctx._variables.stop)))
            self.state = 270
            self.match(baby_duckParser.T__28)
            self.state = 271
            self.match(baby_duckParser.T__23)

            current_scope-=1;
            symbol_table1.pop_function((None if localctx._Id is None else localctx._Id.text), (None if localctx._parameters is None else self._input.getText(localctx._parameters.start,localctx._parameters.stop)), (None if localctx._variables is None else self._input.getText(localctx._variables.start,localctx._variables.stop)));

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duckParser.ParameterContext)
            else:
                return self.getTypedRuleContext(baby_duckParser.ParameterContext,i)


        def getRuleIndex(self):
            return baby_duckParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = baby_duckParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.parameter()
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 275
                self.match(baby_duckParser.T__25)
                self.state = 276
                self.parameter()
                self.state = 281
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._Id = None # Token
            self._type = None # TypeContext

        def Id(self):
            return self.getToken(baby_duckParser.Id, 0)

        def type_(self):
            return self.getTypedRuleContext(baby_duckParser.TypeContext,0)


        def getRuleIndex(self):
            return baby_duckParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = baby_duckParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            localctx._Id = self.match(baby_duckParser.Id)
            self.state = 283
            self.match(baby_duckParser.T__26)
            self.state = 284
            localctx._type = self.type_()

            symbol_table1.add_symbol((None if localctx._Id is None else localctx._Id.text), (None if localctx._type is None else self._input.getText(localctx._type.start,localctx._type.stop)), current_scope)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._Id = None # Token
            self._variables = None # VariablesContext

        def programa(self):
            return self.getTypedRuleContext(baby_duckParser.ProgramaContext,0)


        def Id(self):
            return self.getToken(baby_duckParser.Id, 0)

        def main(self):
            return self.getTypedRuleContext(baby_duckParser.MainContext,0)


        def body(self):
            return self.getTypedRuleContext(baby_duckParser.BodyContext,0)


        def end(self):
            return self.getTypedRuleContext(baby_duckParser.EndContext,0)


        def variables(self):
            return self.getTypedRuleContext(baby_duckParser.VariablesContext,0)


        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duckParser.FunctionContext)
            else:
                return self.getTypedRuleContext(baby_duckParser.FunctionContext,i)


        def getRuleIndex(self):
            return baby_duckParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = baby_duckParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.programa()
            self.state = 288
            localctx._Id = self.match(baby_duckParser.Id)
            self.state = 289
            self.match(baby_duckParser.T__23)
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 290
                localctx._variables = self.variables()


            symbol_table1.add_function((None if localctx._Id is None else localctx._Id.text), 0, (None if localctx._variables is None else self._input.getText(localctx._variables.start,localctx._variables.stop)))
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 294
                self.function()
                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 300
            self.main()
            self.state = 301
            self.body()
            self.state = 302
            self.end()
            symbol_table1.maquina_virtual()
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

        def assign(self):
            return self.getTypedRuleContext(baby_duckParser.AssignContext,0)


        def condition(self):
            return self.getTypedRuleContext(baby_duckParser.ConditionContext,0)


        def cycle(self):
            return self.getTypedRuleContext(baby_duckParser.CycleContext,0)


        def print_(self):
            return self.getTypedRuleContext(baby_duckParser.PrintContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(baby_duckParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return baby_duckParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = baby_duckParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 305
                self.assign()
                pass

            elif la_ == 2:
                self.state = 306
                self.condition()
                pass

            elif la_ == 3:
                self.state = 307
                self.cycle()
                pass

            elif la_ == 4:
                self.state = 308
                self.print_()
                pass

            elif la_ == 5:
                self.state = 309
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





