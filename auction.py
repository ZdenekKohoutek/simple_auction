print('Vítejte v tiché aukční dražbě!')
auctioners = {}
others = 'ano'

while others == 'ano':
    name = input('Jaké je Vaše jméno? ')
    money = int(input('Jaký je Váš vklad? '))
    auctioners[name] = money
    others = input('Jsou za Vámi další kupci? Odpovězte "ano" nebo "ne". ')
    #if others == 'ne':
     #   os.system("clear")

highest_bid = 0
winner = ''
for key in auctioners:
    if auctioners[key] > highest_bid:
        highest_bid = auctioners[key]
        winner = key
print(f'Vítězem aukce je {winner} s nabídkou {highest_bid}Kč.')