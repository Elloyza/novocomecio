import bd
import conexaobd

conbd = conexaobd.conexao()

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