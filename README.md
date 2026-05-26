# GlobalSolution
Avaliação semestral FIAP - Semestre 1

# Monitoramento de Eventos Ambientais

## Descrição
Este projeto em Python realiza o registro e a análise de eventos ambientais.

O sistema coleta informações dos eventos, valida os dados inseridos pelo usuário e gera um relatório com estatísticas e análises espaciais.

---

## Funcionalidades

- Registro de múltiplos eventos ambientais
- Validação de dados de entrada
- Cálculo da área total afetada
- Cálculo da média de intensidade
- Identificação da região com mais ocorrências
- Identificação automática do evento mais crítico, considerando a maior intensidade do impacto e utilizando a área afetada como critério de desempate
- Geração de relatório formatado

---

## Exemplo de Uso

```text
Insira a quantidade de eventos a serem registrados: 1

--- Registro do Evento 1 ---

Tipo de evento: queimada
País: Brasil
Região: Norte
Cidade: Manaus
Área afetada (km²): 120
Intensidade do impacto (1 a 10): 8
Número de ocorrências detectadas: 15
```

---

## Exemplo de Saída

```text
========================================
     RELATÓRIO DE ANÁLISE ESPACIAL
========================================

Total de eventos registrados: 1

Resumo Geral
----------------------------------------
Área total afetada: 120.00 km²
Média de intensidade: 8.00

Análises Específicas
----------------------------------------
Região com mais ocorrências: Norte
Eventos acima da média de intensidade: 0
Densidade média: 0.12 ocorrências/km²

Evento Mais Crítico
----------------------------------------
Tipo: queimada
Local: Manaus, Norte, Brasil
Intensidade: 8
Área afetada: 120.0 km²
========================================
```

---

## Validações Implementadas

- Área afetada deve ser maior que zero
- Intensidade deve estar entre 1 e 10

---

## Autores

Ana Paula Macedo Batista - 573979
Pedro Davi Silva Conceição - 573644
Rafael de Souza Campos - 571659
