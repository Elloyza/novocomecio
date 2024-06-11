from bd import *
from conexaobd import conexao
from datetime import datetime

conbd = conexao()

def menuprincipal():
  while True:
      print("menu")
      print("1.Cadastra")
      print("2.Atualizar")
      print("3.Lista")
      print("4.Pedido")
      print("5.sair")








def cadastrar():
     
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
       PNome =input("Digite o nome do Produtos: ")
       Pdescrição = input("Digite a descrição do Produtos: ")
       PPreco = float(input("Digite o preço do Produto: "))
       PQuantidade = int(input("Digite a Quantidade do Produto: "))
       bd.cadastrarprodutos(conbd, PNome, Pdescrição, PPreco, PQuantidade )

      elif opcao == '2':

       CNome = input("Digite o Nome do Cliente: ")
       CSobrenome = input("Digite o Sobrenome do Cliente: ")
       CEndereco = input("Digite o Endereço do Cliente: ")
       CCidade = input("Digite a Cidade do Cliente: ")
       CCodigopostal = input("Digite o Código Postal: ")
       cadastrarclientes(conbd, CNome, CSobrenome, CEndereco, CCidade, CCodigopostal)

      elif opcao == '3':
      
       FNome =input("Digite o nome do Funcionario: ")
       FCargo = input("Digite o cargo do Funcionario: ")
       FDepartamento = input("Digite o Departamento do Funcionario: ")
       cadastrarfuncionarios(conbd,  FNome,  FCargo, FDepartamento)
 
      elif opcao == '4':

       FNome = input("Digite o Nome do Fornecedor: ")
       FContato = input("Digite o Contato do Fornecedor: ")
       FEndereco = input("Digite o Endereço do Fornecedor: ")
       cadastrarfornecedores (conbd, FNome, FContato, FEndereco)
 
      elif opcao == '5':
       PNome = input("Digite o Nome do Promoção: ") 
       PDescricao = input("Digite a Descrição do Promoção: ")
       PDATAINICIAL = input("Digite o Data Início (formato: DD-MM-YYYY)")
       PDATAINICIAL = datetime.strptime(PDATAINICIAL, "%d-%m-%Y").strftime("%Y-%m-%d")  
       PDATAFINAL= input("Digite o Data Fim (formato: DD-MM-YYYY): ")
       PDATAFINAL= datetime.strptime(PDATAFINAL, "%d-%m-%Y").strftime("%Y-%m-%d")

       print(PDATAINICIAL)
       print(PDATAFINAL)
       cadastrarpromocoes (conbd, PNome,PDescricao, PDATAINICIAL, PDATAFINAL )

      else:
       print("Opção inválida. Tente novamente.")
cadastrar()

def atualizar():
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
atualizar()

def lista():

  while True:
     print("Menu:")
     print("1.Listar produtos")
     print("2.lstar clientes")
     print("3.listar funcionarios")
     print("4.lista fornecedor")
     print("5.lista promoções")    
     opcao = input("Escolha uma opção: ")
 
     if opcao == '1':
        
        bd.listarprodutos(conbd) 

     elif opcao =='2':  
        bd.listarclientes(conbd)  

     elif opcao =='3':  
        bd.listarfuncionarios(conbd) 

     elif opcao =='4':  
        bd.listarfornecedores(conbd)
        
     elif opcao =='5':  
        bd.listarpromocoes(conbd)  

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
       PProduto = input("Digite o Nome do Produto: ")
       PQuantidade = int(input("Digite a Quantidade do Produto: "))
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
         
