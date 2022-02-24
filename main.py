import random
import time
orig = 100
money = 100
CInMarket = 10000
Cprice = 1
COIN = 'BITCOIN'

def trade(money,name,cp):
    CName = name
    Total = money
    CAmount = 50
    Cprice = cp
    sellPrice = 0

    amountSell=0
    MToBuy=0
    for i in range (1000):
        x = random.randint(0,10)
        if x >5:
            if CAmount != 0:
                amountSell = random.randint(0,CAmount)
                CAmount = CAmount - amountSell
                sellPrice = Cprice
                money += amountSell*Cprice

                Cprice = Cprice + random.randint(-2,2)
                print(f"amout of money is{money} and amount of coins is {CAmount} ")
                time.sleep(1)
            else:

                    bought = 0
                    Cprice = Cprice + random.randint(-2,2)
                    MToBuy = random.randint(0,5)*Cprice
                    money = money - MToBuy
                    while MToBuy > Cprice:
                        MToBuy = MToBuy - Cprice
                        CAmount = CAmount+1
                        bought +=1



                    print(f"amount bought {bought}")
                    print(f"current price is {Cprice}")

                        
trade(money,COIN,Cprice)







