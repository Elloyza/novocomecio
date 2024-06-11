import bd
import conexaobd
#menu deletar

conbd = conexaobd.conexao() 

while True:
  print("menu")
  print("1.deletar produtos")
  print("2.deletar Cliente")
  print("3.deletar funcionário")
  print("4.deletar Fornecedor")
  print("5.deletar Promoções")
  print("6.sair")

  opcao = input("escolha uma opção: ")

  if opcao =='1':
    PNome = input("Digite o nome do produto: ")
    bd.deletarprodutos(conbd, PNome)
    print("Produto deletado com sucesso!")
  
  elif  opcao =='2':
    PNome = input("Digite o nome do Cliente: ")
    bd.deletarclientes(conbd, PNome)
    print("Produto deletado com sucesso!")
  
  elif  opcao =='3':
    PNome = input("Digite o nome do funcionário: ")
    bd.deletarfuncionarios(conbd, PNome)

  elif  opcao =='4':
    PNome = input("Digite o nome do fornecedor: ")
    bd.deletarfornecedor(conbd, PNome)

  elif  opcao =='5':
    PNome = input("Digite o nome do promoção: ")
    bd.deletarpromocoes(conbd, PNome)

  else:
      print("Opção inválida. Tente novamente.")
  
  