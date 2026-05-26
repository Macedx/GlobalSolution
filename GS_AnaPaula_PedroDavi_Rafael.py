"""
Sistema de Registro e Análise de Eventos Ambientais.
Este script coleta dados sobre eventos (como desmatamento ou queimadas),
valida as métricas críticas (área e intensidade) e gera um relatório
estatístico de análise espacial.
"""

# --- INICIALIZAÇÃO DE VARIÁVEIS ---
# Utilizando listas paralelas para armazenar os atributos de cada evento
tipos_eventos = []
paises = []
regioes = []
cidades = []
areas_afetadas = []
intensidades = []
ocorrencias = []

# --- ENTRADA DE DADOS ---
quantidade = int(input("Insira a quantidade de eventos a serem registrados: "))

for i in range(quantidade):
    print(f"\n--- Registro do Evento {i + 1} ---")

    # Coleta de dados descritivos do local e do evento
    tipo = input("Tipo de evento (ex: desmatamento, queimada): ")
    pais = input("País: ")
    regiao = input("Região: ")
    cidade = input("Cidade: ")

    # Validação da Área: Impede valores negativos ou zerados que quebrariam 
    # o cálculo de densidade (divisão por zero) posteriormente.
    area = float(input("Área afetada (km²): "))
    while area <= 0:
        print("Erro: A área afetada deve ser estritamente maior que zero.")
        area = float(input("Digite a área novamente (km²): "))

    # Validação da Intensidade: Mantém a métrica dentro de uma escala padrão de 1 a 10.
    intensidade = int(input("Intensidade do impacto (1 a 10): "))
    while intensidade < 1 or intensidade > 10:
        print("Erro: A intensidade deve estar na escala de 1 a 10.")
        intensidade = int(input("Digite a intensidade novamente (1-10): "))

    num_ocorrencias = int(input("Número de ocorrências detectadas: "))

    # Salvando os dados validados nas respectivas listas
    tipos_eventos.append(tipo)
    paises.append(pais)
    regioes.append(regiao)
    cidades.append(cidade)
    areas_afetadas.append(area)
    intensidades.append(intensidade)
    ocorrencias.append(num_ocorrencias)

# --- ANÁLISE DE DADOS ---
# Cálculos estatísticos gerais para compor o escopo do relatório
total_eventos = len(tipos_eventos)
area_total = sum(areas_afetadas)
media_intensidade = sum(intensidades) / total_eventos

# Identificação de extremos buscando o índice (posição na lista) do valor máximo
indice_maior_area = areas_afetadas.index(max(areas_afetadas))

# Mapeamento da região mais afetada com base no pico absoluto de ocorrências
indice_mais_ocorrencias = ocorrencias.index(max(ocorrencias))
regiao_critica = regioes[indice_mais_ocorrencias]

# Relação de ocorrências por área territorial total (ocorrências/km²)
densidade_media = sum(ocorrencias) / area_total

# Filtragem de eventos que superam a média global de intensidade do conjunto de dados
eventos_acima_media = 0
for valor in intensidades:
    if valor > media_intensidade:
        eventos_acima_media += 1

# Localização do evento de maior gravidade. 
# Nota técnica: O método .index() retorna a primeira ocorrência em caso de empate.
indice_critico = intensidades.index(max(intensidades))

# --- GERAÇÃO DO RELATÓRIO ---
# Utilizando f-strings para alinhar textos ao centro (^40) e formatar 
# pontos flutuantes com duas casas decimais (.2f).

print("\n" + "=" * 40)
print(f"{'RELATÓRIO DE ANÁLISE ESPACIAL':^40}")
print("=" * 40)
print(f"Total de eventos registrados: {total_eventos}")

print("-" * 40)
print("Resumo Geral")
print("-" * 40)
print(f"Área total afetada: {area_total:.2f} km²")
print(f"Média de intensidade: {media_intensidade:.2f}")

print("-" * 40)
print("Análises Específicas")
print("-" * 40)
print(f"Região com mais ocorrências: {regiao_critica}")
print(f"Eventos acima da média de intensidade: {eventos_acima_media}")
print(f"Densidade média: {densidade_media:.2f} ocorrências/km²")

print("-" * 40)
print("Evento Mais Crítico")
print("-" * 40)
# Extraindo os dados das múltiplas listas usando o índice do evento mais intenso
print(f"Tipo: {tipos_eventos[indice_critico]}")
print(f"Local: {cidades[indice_critico]}, {regioes[indice_critico]}, {paises[indice_critico]}")
print(f"Intensidade: {intensidades[indice_critico]}")
print(f"Área afetada: {areas_afetadas[indice_critico]} km²")
print("=" * 40)
