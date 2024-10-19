import tiktoken

#   Cargamos el modelo de tokenización (usaremos gpt2)
encoding = tiktoken.get_encoding('gpt2')

#   texto de ejemplo para tokenizar
text = 'Oíd mortales, el grito sagrado! Libertad, Libertad, Libertad!'

#   tokenizamos el texto
tokens = encoding.encode(text)

#   texto original
print(f'Texto original: {text}')
#   texto tokenizado
print(f'Tokens: {tokens}')
#   texto decodificado
print(f'Texto decodificado: {encoding.decode(tokens)}')

######################################################################################

#   ahora mostramos la correspondencia entre palabras, subpalabras o caracteres con sus respectivos tokens
print('\nLista de palabras y sus tokens:')

#   texto de ejemplo
text_0 = 'Vamos a relacionar las palabras con sus tokens'

tokens_text_0 = encoding.encode(text_0)

#   texto original
print(f'Texto original: {text_0}')

#   texto tokenizado
print(f'Tokens: {tokens_text_0}')

#   correspondencia entre tokens y texto
token_text_0_pairs = [(token, encoding.decode([token])) for token in tokens_text_0]
print(f'\nCorrespondencia de tokens:')
for token, token_text in token_text_0_pairs:
   print(f'Token: {token} -> Texto: {token_text}')

#   decodificamos los tokens para obtener el texto original
decoded_text_0 = encoding.decode(tokens_text_0)
print(f'\nTexto decodificado: {decoded_text_0}')
