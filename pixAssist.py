import sqlite3 
# import win32api



banco = sqlite3.connect('pixClientes.db')

cursor = banco.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS registros (
        data_pagamento_pix DATE,
        valor_pix NUMERIC (10,2) 
         );''')


#criando a função que insere um pix 
def inserirPix():
    cursor.execute(f''' INSERT INTO registros (data_pagamento_pix,  valor_pix)
    VALUES ('{data_pagamento_input}', '{valor_pix_input}')
    ''')

    banco.commit()
##############################################################################################



#seleciona o registro de acordo com a data
def selecionaRegistro():
    cursor.execute(f'''
        SELECT valor_pix FROM registros WHERE data_pagamento_pix = '{data_input}';
    ''')
    with open ('rel.txt', 'w') as arquivo:
        relatorio = arquivo.write(f' Novo relatorio ')
        print(relatorio)

    for data_pagamento_pix in cursor.fetchall():
        print ("Valor de pagamento pix: R$",data_pagamento_pix)


        with open ('rel.txt', 'a') as arquivo:
            relatorio = arquivo.write(f'\n Data selecionada: {data_input}, Valor do pagamento PIX:  R${data_pagamento_pix}')
            print(relatorio)       


#menu simples
print (" SELECIONE A OPÇÃO DESEJADA 1 PARA PAGAMENTO E 2 PARA RELATORIO")
op = int (input("O que deseja fazer: "))


if op == 1:
    data_pagamento_input = input ("Qual a data do recebimento? ")

    valor_pix_input = input ("Qual o valor do pagamento? ")    
    inserirPix()
    # win32api.MessageBox(0, 'Cadastrado com Sucesso', 'Sucesso')
if op == 2:
    print ('#####################################################################')
    print ('################### DIGITE COMO NO EXMPLO A BAIXO ###################')
    print ('################### EX: 30/09/2021 ##################################')
    print ('#####################################################################')
    data_input = input ("qual data deseja selecionar: ")
    selecionaRegistro()
    # win32api.MessageBox(0, 'O Relatorio Da Data Seleciona Foi Gerado Procure Pelo Arquivo "rel"', 'Relatorio Gerado Com Sucesso')


