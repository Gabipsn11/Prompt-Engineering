# Questão 1: Algoritmo de Ray Tracing

## Enunciado
Utilize uma ferramenta de IA Generativa para saber como o algoritmo de Ray Tracing calcula a cor de um pixel em uma imagem renderizada.

## Prompt
Explique passo a passo como o algoritmo de Ray Tracing calcula a cor de um pixel em uma imagem renderizada. Inclua os conceitos principais, como traçado de raios, interseção com objetos, cálculo de iluminação e efeitos de materiais (reflexão/refração). Use uma linguagem clara, com exemplos simples, e evite jargões técnicos sem explicação. Estruture a resposta em etapas numeradas.

## Resposta
O algoritmo de Ray Tracing calcula a cor de um pixel simulando o caminho da luz em uma cena 3D. Aqui estão os passos:

1. **Disparo do Raio Primário**:
   - Um raio é disparado da câmera (observador) através do pixel em direção à cena 3D, representando a linha de visão.
   - Exemplo: Para um pixel no centro da tela, o raio aponta diretamente à frente.

2. **Verificação de Interseção**:
   - O algoritmo verifica se o raio atinge algum objeto (ex.: esfera, cubo) usando cálculos geométricos para encontrar o ponto de interseção mais próximo.
   - Exemplo: Se o raio atinge uma esfera vermelha, o ponto de interseção é calculado.

3. **Cálculo de Iluminação**:
   - No ponto de interseção, a cor é calculada com base:
     - **Raios de Sombra**: Raios secundários são disparados até as fontes de luz para verificar obstruções (sombras).
     - **Modelo de Iluminação**: Usa o modelo Phong, considerando:
       - **Luz Difusa**: Cor do objeto sob luz direta (ex.: esfera vermelha parece vermelha).
       - **Luz Especular**: Reflexos brilhantes em superfícies lisas.
       - **Luz Ambiente**: Iluminação geral para áreas sem luz direta.
   - Exemplo: Uma esfera vermelha sob luz branca tem cor difusa vermelha ajustada pela intensidade.

4. **Reflexões e Refrações**:
   - Para objetos reflexivos (ex.: espelho), um raio refletido é disparado, capturando a cor de outros objetos.
   - Para objetos transparentes (ex.: vidro), um raio refratado é disparado, considerando o índice de refração.
   - Exemplo: Um espelho reflete uma parede azul, adicionando azul à cor do pixel.

5. **Combinação de Cores**:
   - A cor final combina luz direta, reflexões, refrações e luz ambiente. A recursão é limitada (ex.: 3 reflexões) para otimizar.
   - Exemplo: A cor de um pixel pode ser 70% vermelha (esfera) + 20% azul (reflexão) + 10% ambiente.

6. **Antialiasing (Opcional)**:
   - Múltiplos raios por pixel são disparados, e as cores são médias para suavizar bordas.
   - Exemplo: Um pixel na borda de uma esfera mistura cores da esfera e do fundo.