from bd import *
from conexaobd import conexao
from datetime import datetime

conbd = conexao()

def menupedido():
  
  while True:
     print("Menu:")
     print("1.Fazer Pedido")
     print("2.Lista pedido")
     print("3.Altera Pedido")
     print("4.Deletar pedido")
     print("5.lista promoções")    
     opcao = input("Escolha uma opção: ")
    
     if opcao == '1':
       PClientes = input("Digite o Nome do Cliente: ")
       print("Escolha algum dos Produtos da Lista")
       bd.listarprodutos(conbd)
       PProduto = input("Digite o Nome do Produto: ")
       PQuantidade = int(input("Digite a Quantidade do Produto: "))
       funcpedido.precoproduto(conbd,PProduto,PQuantidade)
       print("Método de Pagamento")
       print("1. Cartão De Crédito")
       print("2. Cartão De Débito")
       print("3. Boleto Bancário")
       print("4. pix")
       print("3. Dinheiro")

       opcao2 = input("selecione o Método de Pagamento: ")

       if opcao2 == 1:
         PMetodo = "cartão de Crédito"
       elif opcao2 == 2:
         PMetodo = "Cartão De Débito"
       elif opcao2 == 3:
         PMetodo = "Boleto Bancário"
       elif opcao2 == 4:
         PMetodo = "pix"
       elif opcao2 == 5:
         PMetodo = "Dinheiro"
menupedido()
         
