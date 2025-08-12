usd = input("what's your balance in USD? ")
aud = input("what's your balance in AUD? ")
usd = float(usd)
aud = float(aud)
usdconvert = usd * 1.154
usdround = round(usdconvert, 2)
audconvert = aud * 1.22
audround = round(audconvert, 2)
audround = float(audround)
usdround = float(usdround)
total = audround + usdround
print("the total is", total )