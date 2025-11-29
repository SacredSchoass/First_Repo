
#current exchange rate to USD
pesosRate = 0.00027
solesRate = 0.3
reaisRate = 0.19


print('Currency Calculator - Convert your money to US-Dollar\n')
pesos=int(input('How many 🇨🇴 Colombian pesos you still have?'))
pesosUSD=int(pesos*pesosRate)
print(f"Cool, this is worth'{pesosUSD}+'$ in US-Dollar\n")

soles=int(input('How many 🇵🇪 Peruvian soles you still have?'))
solesUSD=int(soles*solesRate)
print(f"Cool, this is worth'{solesUSD}+'$ in US-Dollar\n")


reais=int(input('WHow many 🇧🇷 Brazilian reais you still have?'))
reaisUSD=int(reais*reaisRate)
print(f"Cool, this is worth'{reaisUSD}+'$ in US-Dollar\n")

#Calculations: 
pesosUSD =pesos*pesosRate
solesUSD =soles*solesRate
reaisUSD =reais*reaisRate
total=int(pesosUSD+solesUSD+reaisUSD)

print('Perfect thank you!, Im gonna make a summary for you now\n')

print(f'You got {pesosUSD}$ worth of 🇨🇴 Colombian pesos({pesos}) \n')
print(f'You got {solesUSD}$ worth of 🇵🇪 Peruvian soles({soles}) \n')
print(f'You got {reaisUSD}$ worth of 🇧🇷 Brazilian reais({reais}) \n')
print(f'In total, you have money worth {total}$ in USD\n')