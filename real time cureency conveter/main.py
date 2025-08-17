from forex_python.converter import CurrencyRates
c = CurrencyRates()
amount = int(input("Enter the amount : "))
from_currency = input("From currency : ")
to_currency = input("To currency : ")

result = c.convert(from_currency, to_currency, amount)
print("result : ", result)
print("result : ", c.convert(from_currency, to_currency, amount))
