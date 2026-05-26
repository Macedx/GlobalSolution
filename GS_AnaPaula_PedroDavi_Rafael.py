"""
Sistema de Monitoramento de Eventos Ambientais por Satélite
-----------------------------------------------------------
Desenvolvido para atender aos requisitos do desafio prático.
Utiliza listas para armazenamento de dados, laços de repetição (for e while)
para coleta e validação, e estruturas condicionais (if/elif) para análise
e identificação do evento mais crítico com base em múltiplos critérios.
"""

# --- 1. ARMAZENAMENTO EM LISTAS ---
# Utilizando listas paralelas para armazenar os atributos de cada evento
tipos_eventos = []
paises = []
regioes = []
cidades = []
areas_afetadas = []
intensidades = []
ocorrencias = []

# --- 2. ENTRADA E VALIDAÇÃO DE DADOS ---
quantidade = int(input("Insira a quantidade de eventos: "))

# Laço for para percorrer a quantidade de eventos solicitada
for i in range(quantidade):
    print(f"\n--- Evento {i + 1} ---")

    tipo = input("Tipo: ")
    pais = input("País: ")
    regiao = input("Região: ")
    cidade = input("Cidade: ")

    # Validação com while: Área deve ser estritamente maior que zero
    area = float(input("Área: "))
    while area <= 0:
        print("Erro: A área afetada deve ser maior que zero.")
        area = float(input("Digite a área novamente: "))

    # Validação com while: Intensidade deve estar na escala de 1 a 10
    intensidade = int(input("Intensidade: "))
    while intensidade < 1 or intensidade > 10:
        print("Erro: A intensidade deve estar entre 1 e 10.")
        intensidade = int(input("Digite a intensidade novamente: "))

    num_ocorrencias = int(input("Ocorrências: "))

    # Adicionando os dados validados às suas respectivas listas
    tipos_eventos.append(tipo)
    paises.append(pais)
    regioes.append(regiao)
    cidades.append(cidade)
    areas_afetadas.append(area)
    intensidades.append(intensidade)
    ocorrencias.append(num_ocorrencias)

# --- 3. ANÁLISE DE DADOS ---

# a. Total de eventos registrados
total_eventos = len(tipos_eventos)

# b. Soma total das áreas afetadas
area_total = sum(areas_afetadas)

# c. Média das intensidades
media_intensidade = sum(intensidades) / total_eventos

# d. Evento com maior área afetada (usando max e index conforme dicas)
indice_maior_area = areas_afetadas.index(max(areas_afetadas))

# e. Região com maior número de ocorrências (usando max e index)
indice_mais_ocorrencias = ocorrencias.index(max(ocorrencias))
regiao_critica = regioes[indice_mais_ocorrencias]

# f. Densidade média (ocorrências ÷ área)
densidade_media = sum(ocorrencias) / area_total

# g. Quantidade de eventos acima da média de intensidade
eventos_acima_media = 0
for valor in intensidades:
    if valor > media_intensidade:
        eventos_acima_media += 1

# h. Identificação do Evento Mais Crítico
# Prioridade 1: Maior intensidade
# Prioridade 2 (Desempate): Maior área
# Prioridade 3 (Empate de Intensidade e Área): Mantém o primeiro registro
indice_critico = 0  # Assumimos inicialmente que o evento 0 é o mais crítico

# Começamos a comparar a partir do segundo evento (índice 1)
for i in range(1, total_eventos):
    # Verifica se a intensidade do evento atual é maior
    if intensidades[i] > intensidades[indice_critico]:
        indice_critico = i
        
    # Caso a intensidade seja igual, aplicamos o critério de desempate pela área
    elif intensidades[i] == intensidades[indice_critico]:
        if areas_afetadas[i] > areas_afetadas[indice_critico]:
            indice_critico = i
        # Nota: Se a área também for igual, não fazemos nada. Isso garante que, 
        # em caso de empate total, o primeiro registro encontrado permaneça.


# --- 4. RELATÓRIO DE RESULTADOS ---
# Formatação baseada estritamente no exemplo de saída fornecido no desafio

print("\n" + "=" * 40)
print(f"{'RELATÓRIO DE ANÁLISE':^40}")
print("=" * 40)
print(f"\nTotal de eventos registrados: {total_eventos}\n")

print("-" * 40)
print("Resumo Geral")
print("-" * 40)
# Formatando para remover casas decimais na área e deixar uma casa na média, igual ao exemplo
print(f"Área total afetada: {area_total:.0f} km²")
print(f"Média de intensidade: {media_intensidade:.1f}")

print("\n" + "-" * 40)
print("Análises")
print("-" * 40)
print(f"Região com maior número de ocorrências: {regiao_critica}")
print(f"Quantidade de eventos acima da média de intensidade: {eventos_acima_media}")
print(f"Densidade média de ocorrências: {densidade_media:.2f} ocorrências/km²")

print("\n" + "-" * 40)
print("Evento Mais Crítico")
print("-" * 40)
print(f"Tipo: {tipos_eventos[indice_critico]}")
print(f"Local: {cidades[indice_critico]}, {regioes[indice_critico]}, {paises[indice_critico]}")
print(f"Intensidade: {intensidades[indice_critico]}")
print(f"Área afetada: {areas_afetadas[indice_critico]:.0f} km²")

print("\n" + "=" * 40)
print(f"Total de desastres registrados: {total_eventos}")
