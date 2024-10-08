from conexao_bd import conexao_fechar, conexao_abrir

def clienteListar(con):
    cursor = con.cursor()
    sql = "SELECT * FROM cliente"
    # Criando o cursor com a opção de retorno como dicionário   
    cursor = con.cursor(dictionary=True)
    cursor.execute(sql)

    for (registro) in cursor:
        print(registro['cli_nome'] + " - "+ registro['cli_fone'])

    cursor.close()
    #con.commit()    #mesma coisa q editar e não salvar


def clienteInserir(con, codigo, nome, fone, email):
     cursor = con.cursor()
     sql = "INSERT INTO cliente (cli_codigo, cli_nome, cli_fone, cli_email) VALUES (%s, %s, %s, %s)"
     cursor.execute(sql, (codigo, nome, fone, email))
     con.commit() 
     cursor.close()
        

def main():
    con = conexao_abrir("localhost", "estudante1", "estudante1", "teste_python")
    #con = conexao_abrir("servidor", "bancodedados", "senha", "banco")
    
    # clienteInserir(con, 10, "evandro", "8876-2222","teste@teste")
    clienteListar(con)

    conexao_fechar(con)




if __name__ == "__main__":
	main()
   