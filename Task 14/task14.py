money = input("how much NZD do you want to convert into AUD and USD? ")
money = float(money)
aud = money / 1.08
usd = money / 1.40
roundusd = round(usd, 2)
roundaud = round(aud, 2)
print(roundusd, "USD", roundaud, "AUD")