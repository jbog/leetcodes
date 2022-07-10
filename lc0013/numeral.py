class Numeral:
    def __init__(self, number, symbol):
        self.number = number
        self.symbol = symbol

    def process(self, input):
        output = input
        subtotal = 0
        while output.find(self.symbol) is not -1:
            start = output.index(self.symbol)
            output = output[:start] + output[(start+len(self.symbol)):]
            subtotal = subtotal + self.number
        return (subtotal, output)
