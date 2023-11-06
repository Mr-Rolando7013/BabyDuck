from baby_duckListener import baby_duckListener

class MyListener(baby_duckListener):
    def enterEveryRule(self, ctx):
        print("Enter rule: ", type(ctx).__name__)
    def exitEveryRule(self, ctx):
        print("Exit rule:", type(ctx).__name__)

    def __init__(self, symbol_table):
        self.symbol_table = symbol_table
        # Other initialization code