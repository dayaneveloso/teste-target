import json

# Caminho para o arquivo JSON
arquivo_json = 'dados.json'

# Ler o arquivo JSON
with open(arquivo_json, 'r') as f:
    faturamento_mensal = json.load(f)

# Filtrar apenas os dias com faturamento
faturamentos_validos = [dia["valor"] for dia in faturamento_mensal if dia["valor"] > 0]

# Menor valor de faturamento
menor_faturamento = min(faturamentos_validos)

# Maior valor de faturamento
maior_faturamento = max(faturamentos_validos)

# Média mensal de faturamento (ignorando os dias sem faturamento)
media_mensal = sum(faturamentos_validos) / len(faturamentos_validos)

# Dias com faturamento acima da média
dias_acima_da_media = len([dia for dia in faturamentos_validos if dia > media_mensal])

# Exibir os resultados
print(f"Menor faturamento: {menor_faturamento:.2f}")
print(f"Maior faturamento: {maior_faturamento:.2f}")
print(f"Média de faturamento: {media_mensal:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
