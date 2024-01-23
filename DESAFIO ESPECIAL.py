dia = int(input("Digite o dia do seu nascimento: "))
mês = int(input("Digite o mês do seu nascimento: "))
ano = int(input("Digite o ano do seu nascimento: "))

datanasc = print(dia,mês,ano,sep='/')

dia1 = int(input("Digite o dia de hoje: "))
mês2 = int(input("Digite o mês atual: "))
ano3 = int(input("Digite o ano atual: "))

dataatt = print(dia1,mês2,ano3,sep='/')

idade = (ano3 - ano)

meses=(idade*12)
dias=(meses*365)
print(idade,"anos", meses,"meses e", dias,"dias")

