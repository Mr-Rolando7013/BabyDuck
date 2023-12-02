from quadruple import Quadruple
class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.temporals = []
        self.functions = {}
        self.quadruples = []
        self.vgi = 1000
        self.vgf = 2000
        self.vli = 3000
        self.vlf = 4000
        self.ti = 5000
        self.tf = 6000
        self.tb = 7000
        self.ci = 8000
        self.cf = 9000
        self.vcs = 10000
        self.Poper = []
        self.Ptypes = []
        self.PilaO = []
        self.Quad = []
        self.Psaltos = []
        self.semantic_cube = SemanticCube()
        self.operand_dict = {
            '+': 1,
            '-': 2,
            '*': 3,
            '/': 4,
            '==': 5,
            '!=': 6,
            '<': 7,
            '>': 8,
            '(': 9,
            ')': 10,
            '<=': 11,
            '>=': 12,
            'if': 13,
            'else': 14,
            '=': 15
        }

        self.constants = {}

    def push_operator(self, operator):
        self.Poper.append(self.operand_dict[operator])

    def push_factor(self, newId, newType, isConst):
        if newType == "int" and isConst:
            self.constants[self.ci] = {"id": newId}
            self.PilaO.append(self.ci)
            self.Ptypes.append(newType)
            self.ci += 1


        elif newType == "float" and isConst:
            self.constants[self.cf] = {"id": newId}
            self.PilaO.append(self.cf)
            self.Ptypes.append(newType)
            self.cf += 1

        #String goes to the stack?
        elif newType == "string" and isConst:
            self.constants[self.vcs] = {"id": newId}
            self.PilaO.append(self.vcs)
            self.Ptypes.append(newType)
            self.vcs += 1

        elif isConst == False:
            try:
                #print("Symbols", self.symbols)
                self.PilaO.append(self.symbols[newId]["memory_data"])
                self.Ptypes.append(self.symbols[newId]["data_type"])
            except KeyError:
                raise KeyError(f"Symbol '{newId}' not in this scope")

    def get_key_by_value(self, value):
        for key, val in self.operand_dict.items():
            if val == value:
                return key
        return None
    def push_term(self):
        if len(self.Poper) > 0:
            if self.Poper[-1] == 1 or self.Poper[-1] == 2:
                right_operand = self.PilaO.pop()
                right_type = self.Ptypes.pop()

                left_operand = self.PilaO.pop()
                left_type = self.Ptypes.pop()

                operator = self.Poper.pop()

                operator2 = self.get_key_by_value(operator)

                result_type = self.semantic_cube.get_result_type(operator2, left_type, right_type)
                result = 0
                if result_type == 'error':
                    raise ValueError("An Error ocurred")

                else:
                    if result_type == "int":
                        result = self.ti
                        self.ti += 1

                    elif result_type == "float":
                        result = self.tf
                        self.tf += 1

                    elif result_type == "bool":
                        result = self.tb
                        self.tb += 1

                    quad = (operator, left_operand, right_operand, result)
                    self.Quad.append(quad)

                    self.PilaO.append(result)
                    self.Ptypes.append(result_type)

    def push_term_mas_menos(self):
        if len(self.Poper) > 0:
            if self.Poper[-1] == 6 or self.Poper[-1] == 7 or self.Poper[-1] == 8:
                right_operand = self.PilaO.pop()
                right_type = self.Ptypes.pop()

                left_operand = self.PilaO.pop()
                left_type = self.Ptypes.pop()

                operator = self.Poper.pop()
                operator2 = self.get_key_by_value(operator)

                result_type = self.semantic_cube.get_result_type(operator2, left_type, right_type)
                result = 0
                if result_type == 'error':
                    raise ValueError("An Error ocurred")
                else:
                    if result_type == "int":
                        result = self.ti
                        self.ti += 1

                    elif result_type == "float":
                        result = self.tf
                        self.tf += 1

                    elif result_type == "bool":
                        result = self.tb
                        self.add_temporal("tb", "bool", 0, result)
                        self.tb += 1

                    quad = (operator, left_operand, right_operand, result)
                    self.Quad.append(quad)
                    self.PilaO.append(result)
                    self.Ptypes.append(result_type)
    def push_term_multiplication(self):
        if len(self.Poper) > 0:
            if self.Poper[-1] == 3 or self.Poper[-1] == 4:
                right_operand = self.PilaO.pop()
                right_type = self.Ptypes.pop()
                left_operand = self.PilaO.pop()
                left_type = self.Ptypes.pop()
                operator = self.Poper.pop()
                operator2 = self.get_key_by_value(operator)

                result_type = self.semantic_cube.get_result_type(operator2, left_type, right_type)
                result = 0
                if result_type == 'error':
                    raise ValueError("An Error ocurred")
                else:
                    if result_type == "int":
                        result = self.ti
                        self.ti += 1

                    elif result_type == "float":
                        result = self.tf
                        self.tf += 1

                    elif result_type == "bool":
                        result = self.tb
                        self.tb += 1

                    quad = (operator, left_operand, right_operand, result)
                    self.Quad.append(quad)
                    self.PilaO.append(result)
                    self.Ptypes.append(result_type)


    def push_parentesis(self, parentesis_izq):
        self.Poper.append(self.operand_dict[parentesis_izq])

    def pop_parentesis(self):
        self.Poper.pop()

    def assign_value(self, newId, newOperator):
        self.PilaO.append(self.symbols[newId]["memory_data"])
        self.Ptypes.append(self.symbols[newId]["data_type"])
        self.Poper.append(self.operand_dict[newOperator])

        operator = self.Poper.pop()
        operator2 = self.get_key_by_value(operator)
        operand1_type = self.Ptypes.pop()
        operand1 = self.PilaO.pop()
        target = self.PilaO.pop()

        target_type = self.Ptypes.pop()

        res_type = self.semantic_cube.get_result_type(operator2, operand1_type, target_type)
        if res_type == 'error':
            raise ValueError("An Error ocurred")
        else:
            quad = (operator, target, None, operand1)
            self.Quad.append(quad)

    def push_if(self):
        res_type = self.Ptypes.pop()

        if (res_type != 'bool'):
            print("Error, no es booleano")

        else:
            res = self.PilaO.pop()
            quad = ('GOTOF', res, None, None)
            self.Quad.append(quad)
            self.Psaltos.append(len(self.Quad) - 1)

    def push_if_finish(self):
        endIf = self.Psaltos.pop()

        quad = list(self.Quad[endIf])
        quad[3] = len(self.Quad)

        self.Quad[endIf] = tuple(quad)

    def push_else(self):
        quad = ('GOTO', None, None, None)
        self.Quad.append(quad)
        falsos = self.Psaltos.pop()
        quad = list(self.Quad[falsos])
        quad[3] = len(self.Quad)

        self.Quad[falsos] = tuple(quad)

        self.Psaltos.append(len(self.Quad) - 1)

    def push_while(self):
        self.Psaltos.append(len(self.Quad) - 1)

    def push_while_end(self):
        end = self.Psaltos.pop()
        ret = self.Psaltos.pop() + 1
        quad = ('GOTO', None, None, ret)
        self.Quad.append(quad)

        quad = list(self.Quad[end])
        quad[3] = len(self.Quad)
        self.Quad[end] = tuple(quad)

    def add_memory_number(self, symbol_name):
        if self.symbols[symbol_name]["data_type"] == "int" and self.symbols[symbol_name]["scope"] == 0:
            self.symbols[symbol_name]["memory_data"] = self.vgi
            self.vgi += 1

            if self.vgi >= 2000:
                print("Int limit counter passed !")
        elif self.symbols[symbol_name]["data_type"] == "float" and self.symbols[symbol_name]["scope"] == 0:
            self.symbols[symbol_name]["memory_data"] = self.vgf
            self.vgf += 1

            if self.vgf >= 3000:
                print("Float limit counter passed !")

        elif self.symbols[symbol_name]["data_type"] == "int" and self.symbols[symbol_name]["scope"] != 0:
            self.symbols[symbol_name]["memory_data"] = self.vli
            self.vli += 1

            if self.vli >= 4000:
                print("Int limit counter passed !")

        elif self.symbols[symbol_name]["data_type"] == "int" and self.symbols[symbol_name]["scope"] != 0:
            self.symbols[symbol_name]["memory_data"] = self.vlf
            self.vlf += 1

            if self.vlf >= 5000:
                print("Int limit counter passed !")

    def add_temporal(self, name, data_type, scope, memory):
        newName = name + str(memory)
        self.symbols[newName] = {"data_type": data_type, "scope": scope, "memory_data": memory, "valor": 0}
    def add_symbol(self, name, data_type, scope):
        newNames = name.split(",")
        for newName in newNames:
            if newName in self.symbols and self.symbols[newName]["scope"] == scope and self.symbols[newName]["scope"] == 0:
                raise ValueError(f"Symbol '{newName}' redeclared in the same scope")
            self.symbols[newName] = {"data_type": data_type, "scope": scope, "memory_data": 0, "valor": 0}
            self.add_memory_number(newName)
        return self.symbols

    def add_function(self, name, param_names, var_names):
        definitive_vars = []
        definitive_params = []
        if name in self.functions:
            raise ValueError(f"Function '{name}' redeclared")
        if var_names or param_names:
            if var_names:
                new_vars = var_names[3:].replace(";", ",").replace(":", ",")
                var_list = new_vars.split(",")
                for var in var_list:
                    if var in self.symbols:
                        definitive_vars.append(var)

            if param_names and isinstance(param_names, str):
                new_params = param_names.replace(";", ",").replace(":", ",")

                param_list = new_params.split(",")

                for param in param_list:
                    if param in self.symbols:
                        definitive_params.append(param)

            self.functions[name] = {
                "param_names": definitive_params,
                "var_names": definitive_vars,
            }

        else:
            self.functions[name] = {
                "param_names": param_names,
                "var_names": var_names,
            }

        if self.functions.items():
            for name, info in self.functions.items():
                print(f"Function: {name}, Parameters: {info['param_names']}, Vars: {info['var_names']}")

    def add_quadruple(self, operator, operand1, operand2, result):

        quadruple = Quadruple(operator, operand1, operand2, result)
        self.quadruples.append(quadruple)
    def printSymbols(self):
        for name, info in self.symbols.items():
            print(f"Name: {name}, Data Type: {info['data_type']}, Scope: {info['scope']}")

    def printFunctions(self):
        if self.functions.items():
            for name, info in self.functions.items():
                print(f"Rolis Function: {name}, Parameters: {info['param_names']}, Vars: {info['var_names']}")
        else:
            print("No functions")

    def pop_symbols(self, vars, params):
        if vars:
            for var in vars:
                del self.symbols[var]
        if params:
            for param in params:
                del self.symbols[param]
        else:
            print("No vars or parameters to delete in this function")

    def pop_function(self, name, parameters, variables):
        if name in self.functions:
            self.pop_symbols(self.functions[name]["var_names"], self.functions[name]["param_names"])
            del self.functions[name]

        else:
            raise ValueError(f"Function '{name}' not found in the function table")

    def print_function(self):
        self.Poper.append('print')
        exists = any(item.get('memory_data') == self.PilaO[-1] for item in self.symbols.values())

        if exists:
            operator = self.Poper.pop()
            operands = self.PilaO.pop()
            quad = (operator, None, None, operands)
            self.Quad.append(quad)

        else:
            existsConst = self.constants.get(self.PilaO[-1])
            if existsConst:
                operator = self.Poper.pop()
                newConst = self.PilaO.pop()
                constant_key = [key for key, value in self.constants.items() if key == newConst]
                constant = constant_key[0]
                quad = (operator, None, None, constant)
                self.Quad.append(quad)
                self.Ptypes.pop()
                print("QUADS Print function: ", self.Quad)
            else:
                print("Does not exist \n")

    def maquina_virtual(self):
        quad = 0

        while quad < len(self.Quad):
            oper1 = self.Quad[quad][1]
            #print("VIRTUAL MACHINEEEE: ", oper1)
            #print("Constants: ", self.constants)
            oper2 = self.Quad[quad][2]
            result = self.Quad[quad][3]

            constant_key = [key for key, value in self.constants.items() if key == oper1]

            oper2_key = [key for key, value in self.symbols.items() if value.get('memory_data') == oper1]

            if self.Quad[quad][0] == 15:
                constant_key = [key for key, value in self.constants.items() if key == oper1]
                oper2_key = [key for key, value in self.symbols.items() if value.get('memory_data') == oper1]
                if constant_key:
                    symbol_key = [key for key, value in self.symbols.items() if value.get('memory_data') == result]
                    str_symbol_key = symbol_key[0]
                    str_constant_key = constant_key[0]
                    self.symbols[str_symbol_key]["valor"] = self.constants[str_constant_key]["id"]

                elif oper1 >= 5000:
                    symbol_key = [key for key, value in self.symbols.items() if value.get('memory_data') == result]
                    str_symbol_key = symbol_key[0]
                    self.symbols[str_symbol_key]["valor"] = self.temporals[-1]

                elif oper1 < 5000:
                    str_oper_key = oper2_key[0]
                    symbol_key = [key for key, value in self.symbols.items() if value.get('memory_data') == result]
                    str_symbol_key = symbol_key[0]
                    self.symbols[str_symbol_key]["valor"] = self.symbols[str_oper_key]["valor"]


            #operator is +
            elif self.Quad[quad][0] == 1:
                constant_key = [key for key, value in self.constants.items() if key == oper2]
                oper2_key = [key for key, value in self.symbols.items() if value.get('memory_data') == oper2]
                oper1_key = [key for key, value in self.symbols.items() if value.get('memory_data') == oper1]
                str_oper1_key = oper1_key[0]

                if constant_key:
                    str_constant_key = constant_key[0]

                    self.temporals.append(int(self.symbols[str_oper1_key]["valor"]) + int(self.constants[str_constant_key]["id"]))

                elif oper2_key:
                    str_oper2_key = oper2_key[0]
                    self.temporals.append(int(self.symbols[str_oper1_key]["valor"]) + int(self.symbols[str_oper2_key]["valor"]))

            elif self.Quad[quad][0] == 2:
                constant_key = [key for key, value in self.constants.items() if key == oper2]
                oper2_key = [key for key, value in self.symbols.items() if value.get('memory_data') == oper2]
                oper1_key = [key for key, value in self.symbols.items() if value.get('memory_data') == oper1]
                str_oper1_key = oper1_key[0]

                if constant_key:
                    str_constant_key = constant_key[0]

                    self.temporals.append(int(self.symbols[str_oper1_key]["valor"]) - int(self.constants[str_constant_key]["id"]))


                elif oper2_key:
                    str_oper2_key = oper2_key[0]
                    self.temporals.append(int(self.symbols[str_oper1_key]["valor"]) - int(self.symbols[str_oper2_key]["valor"]))

            #operator is *
            elif self.Quad[quad][0] == 3:
                constant_key = [key for key, value in self.constants.items() if key == oper2]
                oper2_key = [key for key, value in self.symbols.items() if value.get('memory_data') == oper2]
                oper1_key = [key for key, value in self.symbols.items() if value.get('memory_data') == oper1]
                str_oper1_key = oper1_key[0]

                if constant_key:
                    str_constant_key = constant_key[0]
                    self.temporals.append(int(self.symbols[str_oper1_key]["valor"]) * int(self.constants[str_constant_key]["id"]))


                elif oper2_key:
                    str_oper2_key = oper2_key[0]
                    self.temporals.append(int(self.symbols[str_oper1_key]["valor"]) * int(
                        self.symbols[str_oper2_key]["valor"]))

            #operator is /
            elif self.Quad[quad][0] == 4:
                constant_key = [key for key, value in self.constants.items() if key == oper2]
                oper2_key = [key for key, value in self.symbols.items() if value.get('memory_data') == oper2]
                oper1_key = [key for key, value in self.symbols.items() if value.get('memory_data') == oper1]
                str_oper1_key = oper1_key[0]

                if constant_key:
                    str_constant_key = constant_key[0]
                    self.temporals.append(int(self.symbols[str_oper1_key]["valor"]) / int(
                        self.constants[str_constant_key]["id"]))

                elif oper2_key:
                    str_oper2_key = oper2_key[0]
                    self.temporals.append(int(self.symbols[str_oper1_key]["valor"]) / int(self.symbols[str_oper2_key]["valor"]))

            # operator is <
            elif self.Quad[quad][0] == 7:
                constant_key = [key for key, value in self.constants.items() if key == oper2]
                oper2_key = [key for key, value in self.symbols.items() if value.get('memory_data') == oper2]
                oper1_key = [key for key, value in self.symbols.items() if value.get('memory_data') == oper1]
                str_oper1_key = oper1_key[0]
                result_key = [key for key, value in self.symbols.items() if value.get('memory_data') == result]
                str_result_key = result_key[0]
                if constant_key:
                    str_constant_key = constant_key[0]
                    self.symbols[str_result_key]["valor"] = int(self.symbols[str_oper1_key]["valor"]) < int(
                        self.constants[str_constant_key]["id"])

                elif oper2_key:
                    str_oper2_key = oper2_key[0]

                    self.symbols[str_result_key]["valor"] = int(self.symbols[str_oper1_key]["valor"]) < int(self.symbols[str_oper2_key]["valor"])

            #operator is >
            elif self.Quad[quad][0] == 8:
                constant_key = [key for key, value in self.constants.items() if key == oper2]
                oper2_key = [key for key, value in self.symbols.items() if value.get('memory_data') == oper2]
                oper1_key = [key for key, value in self.symbols.items() if value.get('memory_data') == oper1]
                str_oper1_key = oper1_key[0]
                result_key = [key for key, value in self.symbols.items() if value.get('memory_data') == result]
                str_result_key = result_key[0]

                if constant_key:
                    str_constant_key = constant_key[0]

                    self.symbols[str_result_key]["valor"] = int(self.symbols[str_oper1_key]["valor"]) > int(
                        self.constants[str_constant_key]["id"])

                elif oper2_key:
                    str_oper2_key = oper2_key[0]

                    self.symbols[str_result_key]["valor"] = int(self.symbols[str_oper1_key]["valor"]) > int(
                        str_oper2_key)

            elif self.Quad[quad][0] == "print":
                result_key = [key for key, value in self.symbols.items() if value.get('memory_data') == result]
                constant_key = [key for key, value in self.constants.items() if key == result]
                if result_key:
                    str_result_key = result_key[0]
                    result = self.symbols[str_result_key]["valor"]

                elif constant_key:
                    str_constant_key = constant_key[0]
                    result = self.constants[str_constant_key]["id"]


                print("VALOR FINAL: ", result)


            elif self.Quad[quad][0] == "GOTOF":
                result_key = "tb" + str(self.Quad[quad-1][3])
                resultado = self.symbols[result_key]["valor"]
                if type(resultado) == bool:
                    if resultado == False:
                        quad = self.Quad[quad][3]
                        continue

            elif self.Quad[quad][0] == "GOTO":
                quad = self.Quad[quad][3]
                continue


            quad += 1
class SemanticCube:
    def __init__(self):
        self.cube = {}

        self.define('+', 'int', 'int', 'int')
        self.define('-', 'int', 'int', 'int')
        self.define('*', 'int', 'int', 'int')
        self.define('/', 'int', 'int', 'int')
        self.define('+', 'float', 'float', 'float')
        self.define('-', 'float', 'float', 'float')
        self.define('*', 'float', 'float', 'float')
        self.define('/', 'float', 'float', 'float')
        self.define('=', 'int', 'int', 'int')
        self.define('=', 'float', 'float', 'float')

        self.define('!=', 'int', 'int', 'bool')
        self.define('!=', 'float', 'float', 'bool')
        self.define('<', 'int', 'int', 'bool')
        self.define('<', 'float', 'float', 'bool')
        self.define('>', 'int', 'int', 'bool')
        self.define('>', 'float', 'float', 'bool')

    def define(self, operator, type1, type2, result_type):
        self.cube[(operator, type1, type2)] = result_type

    def get_result_type(self, operator, type1, type2):
        return self.cube.get((operator, type1, type2), 'error')
