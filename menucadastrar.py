import bd
import conexaobd
import principal
from datetime import datetime
#menu principal

conbd = conexaobd.conexao() 

while True:
  print("menu")
  print("1.cadastrar Produtos")
  print("2.cadastrar Clientes")
  print("3.cadastrar Funcionários")
  print("4.cadastrar Fornecedor")
  print("5.cadastrar Promoções")
  print("6.sair")

  opcao = input("Escolha uma opção: ")

  if opcao =='1':
    PNome = a =input("Digite o nome do Produtos: ")
    Pdescrição = input("Digite a descrição do Produtos: ")
    PPreco = float(input("Digite o preço do Produto: "))
    PQuantidade = int(input("Digite a Quantidade do Produto: "))
    fornecedor = input("Digite o nome do fornecedor: ")
    bd.cadastrarprodutos(conbd, PNome, Pdescrição, PPreco, PQuantidade, fornecedor )

  elif opcao == '2':

     CNome = input("Digite o Nome do Cliente: ")
     CSobrenome = input("Digite o Sobrenome do Cliente: ")
     CEndereco = input("Digite o Endereço do Cliente: ")
     CCidade = input("Digite a Cidade do Cliente: ")
     CCodigopostal = input("Digite o Código Postal: ")
     bd.cadastrarclientes(conbd, CNome, CSobrenome, CEndereco, CCidade, CCodigopostal)

  elif opcao == '3':
     
     FNome =input("Digite o nome do Funcionario: ")
     FCargo = input("Digite o cargo do Funcionario: ")
     FDepartamento = input("Digite o Departamento do Funcionario: ")
     bd.cadastrarfuncionarios(conbd,  FNome,  FCargo, FDepartamento)
 
  elif opcao == '4':

     FNome = input("Digite o Nome do Fornecedor: ")
     FContato = input("Digite o Contato do Fornecedor: ")
     FEndereco = input("Digite o Endereço do Fornecedor: ")
     bd.cadastrarfornecedores (conbd, FNome, FContato, FEndereco)
 
  elif opcao == '5':
     PNome = input("Digite o Nome do Promoção: ") 
     PDescricao = input("Digite a Descrição do Promoção: ")
     PDATAINICIAL = input("Digite o Data Início (formato: DD-MM-YYYY)")
     PDATAINICIAL = datetime.strptime(PDATAINICIAL, "%d-%m-%Y").strftime("%Y-%m-%d")  
     PDATAFINAL= input("Digite o Data Fim (formato: DD-MM-YYYY): ")
     PDATAFINAL= datetime.strptime(PDATAFINAL, "%d-%m-%Y").strftime("%Y-%m-%d")

     print(PDATAINICIAL)
     print(PDATAFINAL)
     bd.cadastrarpromocoes (conbd, PNome,PDescricao, PDATAINICIAL, PDATAFINAL )

  else:
      print("Opção inválida. Tente novamente.")
      