from datetime import datetime

# Obtenha a data de nascimento do usuário
data_nascimento_str = input("Digite sua data de nascimento (formato: DD-MM-YYYY): ")

# Converta a data de nascimento para o formato esperado
data_nascimento = datetime.strptime(data_nascimento_str, "%d-%m-%Y")

# Obtenha a data atual
data_atual = datetime.now()

# Calcule a diferença entre as datas
diferenca = data_atual - data_nascimento

# Calcule a idade em anos, meses e dias
anos = diferenca.days // 365
meses = (diferenca.days % 365) // 30
dias = (diferenca.days % 365) % 30

# Exiba a idade
print(f"Sua idade é: {anos} anos, {meses} meses e {dias} dias.")