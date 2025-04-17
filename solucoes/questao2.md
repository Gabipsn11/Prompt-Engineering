# Questão 2: Decomposição Numérica de 142.981

## Enunciado
Utilize uma ferramenta de IA Generativa para obter uma resposta completa de como fazer a decomposição numérica de 142.981.

## Prompt
Explique passo a passo como realizar a decomposição numérica (fatoração em números primos) do número 142.981. Mostre cada divisão realizada, verifique a primalidade dos fatores e apresente o resultado final na forma de fatores primos multiplicados. Inclua uma verificação para confirmar que o produto dos fatores é igual a 142.981. Estruture a resposta em etapas numeradas.

## Resposta
A decomposição numérica consiste em fatorar 142.981 em números primos. Aqui estão os passos:

1. **Teste de Divisibilidade por Primos Pequenos**:
   - **2**: 142.981 é ímpar, não divisível.
   - **3**: Soma dos dígitos (1 + 4 + 2 + 9 + 8 + 1 = 25) não é divisível por 3.
   - **5**: Não termina em 0 ou 5.
   - **7**: 142.981 ÷ 7 ≈ 20.426,42 (não inteiro).

2. **Teste com Primos Maiores**:
   - Testamos 11, 13, 17, etc. Vamos tentar 379 (primo, pois não divisível por 2, 3, 5, 7, etc. até √379 ≈ 19):
     - 142.981 ÷ 379 = 377 (divisão exata).

3. **Fatoração do Quociente (377)**:
   - Testamos 377:
     - Não divisível por 2, 3 (soma 3 + 7 + 7 = 17), 5.
     - Tentamos 13: 377 ÷ 13 = 29 (divisão exata).
   - Testamos 29:
     - 29 é primo (não divisível por 2, 3, 5, etc.).

4. **Combinação dos Fatores**:
   - 142.981 = 379 × 13 × 29.

5. **Verificação**:
   - Calculamos: 13 × 29 = 377.
   - 377 × 379 = 142.981 (correto).

## Resultado Final
\[ 142.981 = 13 \times 29 \times 379 \]