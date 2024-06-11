def cadastrarprodutos(conbd,nome,descricao,preco, quantidadeestoque, categoria,fornecedor):
    mycursor = conbd.cursor()
    sql = "insert into produtos (Nome, Descricao, Preco) values (%s,%s,%s)"
    valores=(nome, descricao, preco)
    mycursor.execute(sql, valores)
    ID_Produto = mycursor.lastrowid
    sql1 = "insert into estoque (ID_Produto, quantidade) values (%s,%s)"
    valores1 = (ID_Produto, quantidadeestoque)
    mycursor.execute(sql1, valores1)
    conbd.commit()
    mycursor.close()
    ID_Fornecedor = mycursor.lastrowid
    sql2 = "insert into fornecedores (ID_Fornecedor, Nome) values (%s,%s)"
    valores2 = (ID_Fornecedor, fornecedor)
    mycursor.execute(sql2, valores2)
    conbd.commit()
    print("produto cadastrado com sucesso")
    mycursor.close()

def cadastrarclientes(conbd,nome,sobrenome,endereco,cidade,codigopostal):
    mycursor = conbd.cursor()
    sql = "insert into clientes (Nome,Sobrenome,Endereco,Cidade,Codigopostal) values (%s,%s,%s,%s,%s)"
    valores=(nome,sobrenome,endereco,cidade,codigopostal)
    mycursor.execute(sql, valores)
    conbd.commit()
    print("cliente cadastrado com sucesso")

    mycursor.close()

def cadastrarfuncionarios(conbd,nome,cargo,departamento):
    mycursor = conbd.cursor()
    sql = "insert into funcionarios (Nome,cargo,departamento) values (%s,%s,%s)"
    valores=(nome,cargo,departamento)
    mycursor.execute(sql, valores)
    conbd.commit()
    print("funcionario cadastrado com sucesso")

    mycursor.close()

def cadastrarfornecedores(conbd,nome,contato,endereco):
    mycursor = conbd.cursor()
    sql = "insert into fornecedores(Nome,contato,endereco) values (%s,%s,%s)"
    valores=(nome,contato,endereco)
    mycursor.execute(sql, valores)
    conbd.commit()
    print("fornecedor cadastrado com sucesso")

    mycursor.close()  

def cadastrarpromocoes(conbd,nome,descricao,datainicial,datafinal):
    mycursor = conbd.cursor()
    sql = "insert into promocoes(Nome,Descricao,DataInicio,DataFim) values (%s,%s,%s,%s)"
    valores=(nome,descricao,datainicial,datafinal)
    mycursor.execute(sql, valores)
    conbd.commit()
    print("promoções cadastrado com sucesso")

    mycursor.close()  

def atualizarprodutos(conbd,nome, descricao, preco, PNome):
    mycursor = conbd.cursor()
    sql = "UPDATE produtos SET Nome = %s, Descricao = %s, Preco = %s  WHERE Nome = %s"  
    valores = (nome, descricao, preco, PNome)  
    mycursor.execute(sql, valores)
    conbd.commit()
    print("Produto atualizado com sucesso")
   
    mycursor.close()

def atualizarclientes(conbd, nome, Sobrenome, endereco, cidade, codigopostal,PNome):
    mycursor = conbd.cursor()
    sql = "UPDATE clientes SET Nome = %s, Sobrenome = %s, Endereco = %s, Cidade = %s, CodigoPostal = %s  WHERE Nome = %s"  
    valores = (nome, Sobrenome, endereco, cidade, codigopostal,PNome)  
    mycursor.execute(sql, valores)
    conbd.commit()
    print("cliente atualizado com sucesso")
   
    mycursor.close()

def atualizarfuncionarios(conbd, novonome, novocargo, novodepartamento,PNome,):
    mycursor = conbd.cursor()
    sql = "UPDATE funcionarios SET Nome = %s, Cargo = %s, Departamento = %s WHERE Nome = %s"  
    valores = ( novonome, novocargo, novodepartamento,PNome)  
    mycursor.execute(sql, valores)
    conbd.commit()
    print("Funcionario atualizado com sucesso")
   
    mycursor.close()

def atualizarfornecedores(conbd, novonome, novocontato, novoendereco,PNome):
    mycursor = conbd.cursor()
    sql = "UPDATE fornecedores SET Nome = %s, Contato = %s, Endereco = %s WHERE Nome = %s"  
    valores = (novonome, novocontato, novoendereco,PNome)  
    mycursor.execute(sql, valores)
    conbd.commit()
    print("Foenecedor atualizado com sucesso")
   
    mycursor.close()

def atualizarpromocoes(conbd,novonome, novodescricao, novadatainicial, novadatafinal,PNome):
    mycursor = conbd.cursor() 
    sql = "UPDATE promocoes SET Nome = %s, Descricao = %s, DataInicio = %s DataFim = %s  WHERE Nome = %s"  
    valores = (novonome, novodescricao, novadatainicial, novadatafinal,PNome)  
    mycursor.execute(sql, valores)
    conbd.commit()
    print("Promoções atualizado com sucesso")
   
    mycursor.close()

def listarprodutos(conbd):
    mycursor = conbd.cursor()
    sql = "SELECT * FROM produtos;"
    mycursor.execute(sql)
    listagem = mycursor.fetchall()
    for i in (listagem):
        print(i)
    conbd.commit()
    mycursor.close()

def listarclientes(conbd):
    mycursor = conbd.cursor()
    sql = "SELECT * FROM clientes;"
    mycursor.execute(sql)
    listagem = mycursor.fetchall()
    for i in (listagem):
        print(i)

    mycursor.close()

def listarfuncionarios(conbd):
    mycursor = conbd.cursor()
    sql = "SELECT * FROM funcionarios;"
    mycursor.execute(sql)
    listagem = mycursor.fetchall()
    for i in (listagem):
        print(i)

    mycursor.close()

def listarfornecedores(conbd):
    mycursor = conbd.cursor()
    sql = "SELECT * FROM fornecedores;"
    mycursor.execute(sql)
    listagem = mycursor.fetchall()
    for i in (listagem):
        print(i)

    mycursor.close()

def listarpromocoes(conbd):

    mycursor = conbd.cursor()
    sql = "SELECT * FROM promocoes;"
    mycursor.execute(sql)
    listagem = mycursor.fetchall()
    for i in (listagem):
        print(i)

    mycursor.close()


def obterProdutoID(conbd, nome):
    try:
        with conbd.cursor() as cursor:
            sql = 'SELECT ID_Produto FROM produtos WHERE Nome = %s'
            cursor.execute(sql, (nome,))
            resultado = cursor.fetchone()
            if resultado:
                return resultado[0]
            else:
                print(f"Produto com nome '{nome}' não encontrado.")
                return None
    except Error as e:
        print(f"Ocorreu um erro ao obter o ID do produto: {e}")
        return None
    
def deletarProduto(conbd, nome_produto):
    try:
        produto_id = obterProdutoID(conbd, nome_produto)
        if not produto_id:
            return
        
        conbd.start_transaction()
        with conbd.cursor() as cursor:
            sql_detalhes_pedido = 'DELETE FROM detalhespedido WHERE ID_Produto = %s'
            cursor.execute(sql_detalhes_pedido, (produto_id,))
        with conbd.cursor() as cursor:
            sql_estoque = 'DELETE FROM estoque WHERE ID_Produto = %s'
            cursor.execute(sql_estoque, (produto_id,))
        with conbd.cursor() as cursor:
            sql_produto = 'DELETE FROM produtos WHERE ID_Produto = %s'
            cursor.execute(sql_produto, (produto_id,))
        conbd.commit()
        print("Produto e suas referências deletadas com sucesso")

    except Error as e:
        conbd.rollback()
        print(f"Ocorreu um erro ao deletar o produto: {e}")

    finally:
        conbd.close()    
    

def deletarprodutos(conbd,nome):
    mycursor = conbd.cursor()
    sql = "DELETE FROM produtos WHERE Nome = %s"
    valores=(nome,)
    mycursor.execute(sql, valores)
    conbd.commit()
    print("produto deletado com sucesso")
    
    mycursor.close() 

def deletarclientes(conbd,nome):
    mycursor = conbd.cursor()
    sql = "DELETE FROM clientes WHERE Nome = %s"
    valores=(nome,)
    mycursor.execute(sql, valores)
    conbd.commit()
    print("cliente deletado com sucesso")
    
    mycursor.close() 

def deletarfuncionarios(conbd,nome):
    mycursor = conbd.cursor()
    sql = "DELETE FROM funcionarios WHERE Nome = %s"
    valores=(nome,)
    mycursor.execute(sql, valores)
    conbd.commit()
    print("funcionario deletado com sucesso")
    
    mycursor.close() 

def deletarfornecedores(conbd,nome):
    mycursor = conbd.cursor()
    sql = "DELETE FROM fornecedores WHERE Nome = %s"
    valores=(nome,)
    mycursor.execute(sql, valores)
    conbd.commit()
    print("fornecedor deletado com sucesso")
    
    mycursor.close() 

def deletarpromocoes(conbd,nome):
    mycursor = conbd.cursor()
    sql = "DELETE FROM promocoes WHERE Nome = %s"
    valores=(nome,)
    mycursor.execute(sql, valores)
    conbd.commit()
    print("promoção deletada com sucesso")
   
    mycursor.close()

def precoproduto(conbd,IDProduto,Quantidade):
  
   mycursor = conbd.cursor()
   sql = "SELECT Preco FROM produtos WHERE ID_Produto = %s"
   val = (IDProduto,)
   mycursor.execute(sql, val)
   preco = mycursor.fetchone()[0]
   float(preco)
   int(Quantidade)
   valortotal = preco * Quantidade
   conbd.comit()
   print("Valor Total do Pedido", valortotal)
   mycursor.close()

def IDProduto(conbd,Produto):
    mycursor = conbd.cursor()
    sql = "SELECT ID_Produto FROM produtos WHERE Nome = %s"
    val = (Produto,)
    mycursor.execute(sql, val)
    ID = mycursor.fetchone()[0]
    conbd.comit()
    print(" o ID do Produto " ,Produto," é: ",ID)
    mycursor.close()

def MovEstoque(conbd,IDProduto,Quantidade):
     mycursor = conbd.cursor()
     sql = "SELECT ID_Produto FROM produtos WHERE Nome = %s"
     val = (Produto,)
     mycursor.execute(sql, val)
       ID = mycursor.fetchone()[0]

