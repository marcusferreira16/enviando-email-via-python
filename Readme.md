# Enviando um e-mail via Python

Esse repositório tem o intuito de ter um código que mande uma mensagem via e-mail, a partir de um e-mail para envio. O código foi feito usando um e-mail via outlook, no entanto, pode ser alterado por qualquer host e port que escolher.

## Diagrama do código

```mermaid
  graph LR;
      A[Importar as bibliotecas]-->B[Fazer a configuração do host e port];
      B{Configuração do e-mail de saída}-->C[Cria o objeto servidor];
      C[Faz login no servidor de acordo com a configuração do e-mail de saída]-->D{Cria a mensagem que deseja enviar};
      D{Adiciona o e-mail que irá receber}-->E[Envia a mensagem];
```
