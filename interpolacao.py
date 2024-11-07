In [13]: email_tmpl = """
    ...: Olá, %(nome)s
    ...:
    ...: Tem interesse em comprar %(produto)s?
    ...:
    ...: Este produto é ótimo para resolver
    ...: %(texto)s
    ...:
    ...: Clique agora em %(link)s
    ...:
    ...: Apenas %(quantidade)d disponíveis!
    ...:
    ...: Preço promocional %(preco).2f
    ...: """
    ...:
    ...:

In [14]: clientes = ["Maria", "João", "Bruno"]

In [15]: for cliente in clientes:
    ...:     print(
    ...:     % {
  Cell In[15], line 3
    % {
    ^
SyntaxError: invalid syntax


In [16]: for cliente in clientes:
    ...:     print(
    ...:     email_tmpl
    ...:     % {
    ...:     "nome": cliente,
    ...:     "produto": "caneta",
    ...:     "texto": "Escrever muito bem",
    ...:     "link": "https://canetaslegais.com",
    ...:     "quantidade": 1,
    ...:     "preco": 50.50,
    ...:     }
    ...:     )
    ...:

Olá, Maria

Tem interesse em comprar caneta?

Este produto é ótimo para resolver
Escrever muito bem

Clique agora em https://canetaslegais.com

Apenas 1 disponíveis!

Preço promocional 50.50


Olá, João

Tem interesse em comprar caneta?

Este produto é ótimo para resolver
Escrever muito bem

Clique agora em https://canetaslegais.com

Apenas 1 disponíveis!

Preço promocional 50.50


Olá, Bruno

Tem interesse em comprar caneta?

Este produto é ótimo para resolver
Escrever muito bem

Clique agora em https://canetaslegais.com

Apenas 1 disponíveis!

Preço promocional 50.50
