
# Explicaciones del Código

### Explicación número 1:
#### ¿Qué hace la siguiente línea?
```python
import tiktoken
```
Esta línea **importa la librería `tiktoken`**, una librería utilizada para el **procesamiento de texto**, en particular para la **tokenización**. La tokenización es el proceso de dividir texto en partes más pequeñas como palabras, subpalabras o caracteres que luego se utilizan en modelos de lenguaje como GPT.

- **Tiktoken** está optimizada para trabajar con modelos de OpenAI como GPT-3 y GPT-4, pero en este caso se usa el modelo de tokenización de GPT-2.
- **`tiktoken`** provee varias funciones y clases, pero las más importantes están relacionadas con la **tokenización** y **decodificación** de texto.

#### Métodos importantes de `tiktoken`:
1. **`get_encoding(encoding_name)`**: Carga un modelo de tokenización específico. En el ejemplo, se carga el tokenizador de GPT-2.
2. **`encode(text)`**: Toma una cadena de texto y la convierte en una lista de tokens (números).
3. **`decode(tokens)`**: Toma una lista de tokens y los convierte de nuevo en texto legible.

### Explicación número 2:
#### ¿Qué hace la siguiente línea?
```python
encoding = tiktoken.get_encoding('gpt2')
```
Esta línea **carga el tokenizador** utilizando el método **`get_encoding()`** de la librería **`tiktoken`**.

- **`'gpt2'`** es el nombre del esquema de tokenización específico que se va a usar.
- Al ejecutar esta línea, la variable **`encoding`** contendrá el modelo de tokenización basado en **GPT-2**, permitiendo luego **tokenizar** y **decodificar** texto usando ese modelo.

Este modelo de tokenización es el mismo que se usó para entrenar modelos de lenguaje GPT-2. Los modelos más grandes como GPT-3 y GPT-4 pueden utilizar esquemas más avanzados, pero este es suficiente para demostrar la tokenización.

### Explicación número 3:
#### Texto de ejemplo para tokenizar
```python
text = 'Oíd mortales, el grito sagrado! Libertad, Libertad, Libertad!'
```
Esta línea define una variable **`text`** que contiene el texto en español **"Oíd mortales, el grito sagrado! Libertad, Libertad, Libertad!"**. Este texto será el **ejemplo** que se tokenizará usando el modelo cargado en **`encoding`**.

### Explicación número 4:
#### Tokenizamos el texto
```python
tokens = encoding.encode(text)
```
Esta línea **tokeniza** el texto contenido en la variable **`text`** usando el modelo de tokenización previamente cargado en **`encoding`**.

- **`encoding.encode()`** convierte el texto en una lista de **tokens** (números), donde cada token representa una palabra, subpalabra o carácter en el texto original.
- Los tokens resultantes se guardan en la variable **`tokens`**, que es una lista de números enteros.

Ejemplo de la salida:
```python
[40, 5408, 11, 262, 10332, 11794, 0, 15425, 15425, 15425, 0]
```

### Explicación número 5:
#### Imprimir el texto original, tokens y texto decodificado
```python
print(f'Texto original: {text}')
print(f'Tokens: {tokens}')
print(f'Texto decodificado: {encoding.decode(tokens)}')
```
Estas tres líneas imprimen el **texto original**, los **tokens generados** por la tokenización y luego el **texto decodificado** a partir de esos tokens.

- **`print(f'Texto original: {text}')`** muestra el texto tal como fue definido.
- **`print(f'Tokens: {tokens}')`** imprime la lista de tokens generada por el proceso de tokenización.
- **`encoding.decode(tokens)`** convierte la lista de tokens nuevamente en texto, y luego se imprime con **`print(f'Texto decodificado: {encoding.decode(tokens)})`**.

Esto sirve para comprobar que los tokens generados efectivamente corresponden al texto original.

### Explicación número 6:
#### Mostrar la correspondencia entre palabras, subpalabras o caracteres con sus respectivos tokens
```python
print('
Lista de palabras y sus tokens:')
text_0 = 'Vamos a relacionar las palabras con sus tokens'
tokens_text_0 = encoding.encode(text_0)
print(f'Texto original: {text_0}')
print(f'Tokens: {tokens_text_0}')
```
Estas líneas de código muestran la **correspondencia entre las palabras, subpalabras o caracteres** y sus respectivos tokens. Primero imprimen el texto original y luego lo tokenizan, mostrando los tokens generados.

- **`text_0`** contiene un nuevo texto que se va a tokenizar.
- **`tokens_text_0`** almacena la lista de tokens que representa el texto.
- **`print(f'Texto original: {text_0}')`** imprime el texto original.
- **`print(f'Tokens: {tokens_text_0}')`** muestra los tokens generados a partir del texto, facilitando la comprensión de cómo el texto se convierte en números para ser procesado por el modelo.

### Explicación número 7:
#### Correspondencia entre tokens y texto
```python
token_text_0_pairs = [(token, encoding.decode([token])) for token in tokens_text_0]
print(f'
Correspondencia de tokens:')
for token, token_text in token_text_0_pairs:
   print(f'Token: {token} -> Texto: {token_text}')
```
Estas líneas de código muestran la **correspondencia exacta entre cada token y su representación textual**. Primero crean una lista de pares token-texto y luego la imprimen, mostrando qué fragmento de texto corresponde a cada token.

- **`token_text_0_pairs`** genera una lista de tuplas donde cada tupla contiene un token y su fragmento de texto decodificado.
- El **bucle `for`** imprime cada par **token -> texto**, mostrando cómo cada número (token) corresponde a una palabra, subpalabra o carácter del texto.

### Explicación número 8:
#### Decodificamos los tokens para obtener el texto original
```python
decoded_text_0 = encoding.decode(tokens_text_0)
print(f'
Texto decodificado: {decoded_text_0}')
```
Estas líneas de código **decodifican los tokens** para reconstruir el **texto original**. En esencia, toman la lista de tokens que representan el texto y la convierten nuevamente en palabras legibles para los humanos. Finalmente, el texto decodificado se imprime.

- **`encoding.decode(tokens_text_0)`** toma la lista de tokens y la decodifica para generar el **texto original**.
- El texto **decodificado** se imprime para compararlo con el texto antes de ser tokenizado.
