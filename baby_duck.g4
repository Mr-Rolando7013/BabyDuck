grammar baby_duck;

@parser::header {
from symbol_table import *
symbol_table1 = SymbolTable()
current_scope = 0

}

@parser::members {


}

programRule : program EOF;

programa : 'program';
Id : [a-zA-Z]+[0-9]*;
main : 'main';
end : 'end';
var : 'var';
void : 'void';
int : 'int';
float : 'float';
else: 'else';
if : 'if';
while : 'while';
do : 'do';
CTE_STRING : '"'.*?'"';
CTE_INT : [0-9]+;
CTE_FLOAT: [0-9]+ '.' [0-9]+;
WS: [ \t\r\n]+ -> skip;

expression: exp (('>' {symbol_table1.push_operator('>')} | '<' {symbol_table1.push_operator('<')}) exp | '!=' {symbol_table1.push_operator('!=')} exp)*{symbol_table1.push_term_mas_menos()};
exp : term {symbol_table1.push_term()}('+' {symbol_table1.push_operator('+')} exp | '-' {symbol_table1.push_operator('-')} exp)*;
term: factor {symbol_table1.push_term_multiplication()}('*' {symbol_table1.push_operator('*')} term | '/' {symbol_table1.push_operator('/')} term)*;
factor: ('+'| '-')? (Id {symbol_table1.push_factor($Id.text, None, False)} | CTE_INT {symbol_table1.push_factor($CTE_INT.text, "int", True)} | CTE_FLOAT {symbol_table1.push_factor($CTE_FLOAT.text, "float", True)} | '(' {symbol_table1.push_parentesis('(')} expression ')' {symbol_table1.pop_parentesis()});
body: '{' statement* '}';
assign: Id '=' expression {symbol_table1.assign_value($Id.text, '=')}';';
condition: if '(' expression ')' {symbol_table1.push_if()} body (else {symbol_table1.push_else()} body)? {symbol_table1.push_if_finish()}';';
cycle: while body {symbol_table1.push_while()} do '(' expression ')' {symbol_table1.push_while_end()} ';';
print: 'print' '(' (expression | CTE_STRING) (',' (expression | CTE_STRING))* ')' ';'{
symbol_table1.printSymbols();
};
functionCall: Id '(' (expression (',' expression)*)? ')' ';';
type: int | float;
variables: var listvars*;
listvars: listaId ':' type ';'{
symbol_table1.add_symbol($listaId.text, $type.text, current_scope);
};
listaId : Id idExtra;
idExtra : (',' listaId)?;
function: {global current_scope}void {current_scope+=1} Id '(' parameters* ')' '[' variables? body {symbol_table1.add_function($Id.text, $parameters.text, $variables.text, current_scope)}']' ';'{
current_scope-=1;
symbol_table1.pop_function($Id.text, $parameters.text, $variables.text);
};
parameters : parameter (',' parameter)*;

parameter: Id ':' type{
symbol_table1.add_symbol($Id.text, $type.text, current_scope)
};

program: programa Id ';' variables? {symbol_table1.add_function($Id.text, 0, $variables.text, current_scope)}(function)* main body end;
statement: (assign | condition | cycle | print | functionCall);
