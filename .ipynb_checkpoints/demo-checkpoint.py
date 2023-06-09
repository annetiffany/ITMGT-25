print ("hello world")
def savings(gross_pay,tax_rate,expenses,wow):
    rawr = gross_pay-round(gross_pay*tax_rate)-expenses
    return str(rawr) + wow
print ("hello world")
a = savings(1000,0.10,100,"kg")
print(a)
