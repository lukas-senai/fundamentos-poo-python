# 12 · Exercícios e Projetos Guiados

Aprender POO é principalmente **praticar**. Aqui vão desafios graduais, com dicas do que observar.

## Aquecimento (básico)
1) Crie uma classe `Carro` com `marca` e `ano`. Instancie dois objetos e imprima informações amigáveis.
2) Modele `Aluno` com método `media(n1, n2)` e um método que diz se está aprovado.

## Intermediário
3) Implemente `ContaBancaria` com `depositar`, `sacar`, `saldo` (usar `@property`). Dispare exceção própria ao sacar sem saldo.
4) Modele `Livro` com `preco` validado por `@property` e método `aplicar_desconto(percentual)`.

## Herança e Polimorfismo
5) Crie `Funcionario` (nome, salário base) e duas subclasses (`Gerente`, `Dev`) que calculam bônus de forma diferente. Faça uma função que recebe uma lista heterogênea e soma a folha.
6) Crie `Forma` abstrata e implementações `Quadrado`, `Circulo`, `Triangulo`. Escreva uma função que imprime a área de qualquer forma (duck typing).

## Projetinho 1: Catálogo de Itens (composição + dataclasses)
- Use `dataclasses` para `Item` (nome, preço).
- Faça `Carrinho` que guarda itens (composição) e calcula total. Adicione cupom por Strategy.

## Projetinho 2: Sistema de Notificações (Observer)
- Um `Publicador` dispara eventos; `AssinanteEmail` e `AssinanteSMS` reagem.
- Permita adicionar/remover assinantes em tempo de execução.

## Dicas de Avaliação (para professores)
- Observe se o aluno separa responsabilidades (sem classes “faz-tudo”).
- Veja se validam entradas com `property` e tratam erros com exceções próprias.
- Procure por nomes autoexplicativos e `__repr__` úteis para depuração.
- Estimule o uso de testes simples (mesmo que `assert` em scripts).

>*Observação*: Todos os blocos de código abaixo usam **recuo de 4 espaços** para evitar falhas em renderizadores que quebram com cercas de código.

