from numeral import Numeral
class Solution:
    def romanToInt(self, s):
        numerals = [
            Numeral(4, "IV"),
            Numeral(9, "IX"),
            Numeral(40, "XL"),
            Numeral(90, "XC"),
            Numeral(400, "CD"),
            Numeral(900, "CM"),
            Numeral(1, "I"),
            Numeral(5, "V"),
            Numeral(10, "X"),
            Numeral(50, "L"),
            Numeral(100, "C"),
            Numeral(500, "D"),
            Numeral(1000, "M")
        ]
        rems = s
        total = 0
        for numeral in numerals:
            (subtotal, rems) = numeral.process(rems)
            total = total + subtotal
        return total
