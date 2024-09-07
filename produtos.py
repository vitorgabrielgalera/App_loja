import sqlite3

#crio a conexão com o banco de dados
conn = sqlite3.connect('produtos.db')

#cria um cursor
cursor = conn.cursor()

#checa se a tabela 'produtos' existe
cursor.execute('''SELECT count(name) FROM sqlite_master WHERE
               type="table" and name = "produtos"''')

#se a tabela não existir crie-a
if cursor.fetchone()[0] == 0:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque REAL NOT NULL 
        )
    ''')

    conn.commit()

while True:
    DROP TABLE cardapio
    resposta = input("O que deseja fazer? (1-cadastrar 2-atualizar)")
    if resposta == "1":
        nome = input("Nome do item (digite 'sair' para sair): ")
        if nome == 'sair':
            break
        preco = float(input("preco do item: "))
        estoque = float(input("estoque: "))
        cursor.execute(f'''
            INSERT INTO produtos (nome, preco, estoque)
            VALUES ('{nome}', {preco}, '{estoque}')
        ''')

    if resposta == "2":
        print("Qual o id do produto que deseja alterar?")
        cursor.execute("SELECT * FROM produtos")
        print(cursor.fetchall())
        resposta = input()
    
    conn.commit()

conn.close()