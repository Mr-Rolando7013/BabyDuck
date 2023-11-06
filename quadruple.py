class Quadruple:
    def __init__(self, operator, oper1, oper2, result):
        self.operator = operator
        self.oper1 = oper1
        self.oper2 = oper2
        self.result = result
        self.Poper = []
        self.Ptypes = []
        self.PilaO = []

    def addAsign(self, operator, oper1, oper2, result):
        self.PilaO.append(oper1)
        self.Poper.append(operator)
        if self.Poper[-1] == 1 or self.Poper == 2:
            pass


    def __str__(self):
        return f"({self.operator}, {self.oper1}, {self.oper2}, {self.result})"
