#金額
price = 468
pay = 10000
money_type = [10000,5000,1000,500,100]
charge_total = pay - price
for money in money_type:
    qiot = charge_total // money
    print(money,'en= ',qiot,'mai', sep= '')
    charge_total -= qiot * money
