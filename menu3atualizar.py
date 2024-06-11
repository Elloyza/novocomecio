import bd
import conexaobd
from datetime import datetime
#menu deletar

conbd = conexaobd.conexao() 

while True:
  print("menu")
  print("1.atualizar produtos")
  print("2.atualizar Cliente")
  print("3.atualiza funcionário")
  print("4.atualiza Fornecedor")
  print("5.atualiza Promoções")
  print("6.sair")

 
  opcao = input("escolha uma opção: ")

  if opcao == '1':
    PNome = input("Digite o nome do produto: ")
    novonome = input("Digite o novo nome do produto: ")
    novadescricao =input("Digite a nova Descrição do produto: ")
    novopreco = float(input("Digite o novo preço do produto: "))
    bd.atualizarprodutos(conbd, novonome, novadescricao, novopreco,PNome)
 
  elif opcao == '2':

    PNome = input("Digite o nome do cliente: ")
    novoNome = input("Digite o novo Nome do Cliente: ")
    novoSobrenome = input("Digite o novo  Sobrenome do Cliente: ")
    novoEndereco = input("Digite o novo Endereço do Cliente: ")
    novaCidade = input("Digite a nova Cidade do Cliente: ")
    novoCodigopostal = input("Digite o novo Código Postal: ")
    bd.atualizarclientes(conbd, novoNome, novoSobrenome, novoEndereco, novaCidade, novoCodigopostal,PNome )

  elif opcao == '3':

    PNome = input("Digite o nome do Funcionario: ")
    novonome = input("Digite o novo Nome do Funcionario: ")
    novocargo = input("Digite o novo  cargo do Funcionario: ")
    novodepartamento = input("Digite o novo Departamento do Funcionario: ")
    bd.atualizarfuncionarios(conbd, novonome, novocargo, novodepartamento,PNome )
 
  elif opcao == '4':
  
    PNome = input("Digite o nome do Fornecedor: ")
    novonome = input("Digite o novo Nome do Fornecedor: ")
    novocontato = input("Digite o novo  contato do Fornecedor: ")
    novoendereco = input("Digite o novo Endereço do Fornecedor: ")
    bd.atualizarfornecedores(conbd, novonome, novocontato, novoendereco,PNome )
  
  elif opcao == '5':

    PNome = input("Digite o nome da promoção: ")
    novonome = input("Digite o novo Nome da promoção: ")
    novodescricao = input("Digite a nova descrição  da promoção: ")
    PDATAINICIAL = input("Digite a nova Data Início (formato: DD-MM-YYYY)")
    PDATAINICIAL = datetime.strptime(PDATAINICIAL, "%d-%m-%Y").strftime("%Y-%m-%d")  
    PDATAFINAL= input("Digite a nova data Fim (formato: DD-MM-YYYY): ")
    PDATAFINAL= datetime.strptime(PDATAFINAL, "%d-%m-%Y").strftime("%Y-%m-%d")
    print(PDATAINICIAL)
    print(PDATAFINAL)
    bd.atualizarpromocoes(conbd,novonome, novodescricao, PDATAINICIAL, PDATAFINAL,PNome )