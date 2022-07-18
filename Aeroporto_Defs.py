import sqlite3

conexao = sqlite3.connect('Banco de Dados Aeroporto.db')
cursor = conexao.cursor()


# ----------------------------------------------------------------------------------------------------------------------
class Aviao:
    def cadastrar_aeronave(self):
        codigo = input('Código da Aeronave: ')
        modelo = input('Modelo da Aeronave: ')
        assentos = input('Assentos Disponíveis da Aeronave: ')
        bagagem = input('Limite de Bagagem(kg) da Aeronave: ')
        cursor.execute(
            f'INSERT INTO Aeronaves (Código_Aeronave, Modelo_Aeronave, Assentos_Disponíveis, Limite_de_Bagagem_kg)'
            f'VALUES("{codigo}", "{modelo}", "{assentos}", "{bagagem}")'
        )
        conexao.commit()
        print('\033[35mAeronave Cadastrada!\033[0m')

    # ------------------------------------------------------------------------------------------------------------------
    def editar_aeronave(self):
        codigo = input('Código da Aeronave que deseja editar: ')
        cursor.execute(f'SELECT * FROM Aeronaves WHERE Código_Aeronave="{codigo}"')
        linha = cursor.fetchone()
        if linha is None:
            print('\033[31mAeronave não encontrada!\033[0m')
        else:
            print(f'{linha}')
            print('=-=' * 10)
            print('Qual campo que deseja alterar?')
            print('[1] Código_Aeronave   [2] Modelo_Aeronave   [3] Assentos_Disponíveis   [4] Limite_de_Bagagem_kg')
            op = int(input('Digite a opção desejada: '))
            lista = ['', 'Código_Aeronave', 'Modelo_Aeronave', 'Assentos_Disponíveis', 'Limite_de_Bagagem_kg']
            x = input('Nova Informação: ')
            cursor.execute(f'UPDATE Aeronaves SET {lista[op]}="{x}" WHERE Código_Aeronave="{codigo}"')
            conexao.commit()
            print('\033[35mAeronave Atualizada!\033[0m')

    # ------------------------------------------------------------------------------------------------------------------
    def deletar_aeronave(self):
        codigo = input('Código da Aeronave que deseja deletar: ')
        cursor.execute(f'SELECT * FROM Aeronaves WHERE Código_Aeronave="{codigo}"')
        linha = cursor.fetchone()
        if linha is None:
            print('\033[31mAeronave não encontrada!\033[0m')
        else:
            cursor.execute(f'DELETE FROM Aeronaves WHERE Código_Aeronave="{codigo}"')
            conexao.commit()
            print('\033[35mAeronave Deletada!\033[0m')

    # ------------------------------------------------------------------------------------------------------------------
    def cadastrar_empresa(self):
        codigo = input('Código da Empresa: ')
        nome = input('Nome da Empresa: ')
        nacionalidade = input('Nacionalidade da Empresa: ')
        sigla = input('Sigla da Empresa: ')
        cursor.execute(
            f'INSERT INTO Empresas (Código_Empresa, Nome_Empresa, Nacionalidade_Empresa, Sigla_Empresa)'
            f'VALUES("{codigo}", "{nome}", "{nacionalidade}", "{sigla}")'
        )
        conexao.commit()
        print('\033[35mEmpresa Cadastrada!\033[0m')

    # ------------------------------------------------------------------------------------------------------------------
    def editar_empresa(self):
        codigo = input('Código da Empresa que deseja editar: ')
        cursor.execute(f'SELECT * FROM Empresas WHERE Código_Empresa="{codigo}"')
        linha = cursor.fetchone()
        if linha is None:
            print('\033[31mEmpresa não encontrada!\033[0m')
        else:
            print(f'{linha}')
            print('=-=' * 10)
            print('Qual campo que deseja alterar?')
            print('[1] Código_Empresa   [2] Nome_Empresa   [3] Nacionalidade_Empresa   [4] Sigla_Empresa')
            op = int(input('Digite a opção desejada: '))
            lista = ['', 'Código_Empresa', 'Nome_Empresa', 'Nacionalidade_Empresa', 'Sigla_Empresa']
            x = input('Nova Informação: ')
            cursor.execute(f'UPDATE Empresas SET {lista[op]}="{x}" WHERE Código_Empresa="{codigo}"')
            conexao.commit()
            print('\033[35mEmpresa Atualizada!\033[0m')

    # ------------------------------------------------------------------------------------------------------------------
    def deletar_empresa(self):
        codigo = input('Código da Empresa que deseja deletar: ')
        cursor.execute(f'SELECT * FROM Empresas WHERE Código_Empresa="{codigo}"')
        linha = cursor.fetchone()
        if linha is None:
            print('\033[31mEmpresa não encontrada!\033[0m')
        else:
            cursor.execute(f'DELETE FROM Empresas WHERE Código_Empresa="{codigo}"')
            conexao.commit()
            print('\033[35mEmpresa Deletada!\033[0m')

    # ------------------------------------------------------------------------------------------------------------------
    def cadastrar_aeroporto(self):
        codigo = input('Código do Aeroporto: ')
        nome = input('Nome do Aeroporto: ')
        sigla = input('Sigla do Aeroporto: ')
        cidade = input('Cidade do Aeroporto: ')
        estado = input('Estado do Aeroporto: ')
        pais = input('País do Aeroporto: ')
        continente = input('Continente do Aeroporto: ')
        cursor.execute(
            f'INSERT INTO Aeroportos (Código_Aeroporto, Nome_Aeroporto, Sigla_Aeroporto, Cidade, Estado, País, Continente)'
            f'VALUES("{codigo}", "{nome}", "{sigla}", "{cidade}", "{estado}", "{pais}", "{continente}")'
        )
        conexao.commit()
        print('\033[35mAeroporto Cadastrado!\033[0m')

    # ------------------------------------------------------------------------------------------------------------------
    def editar_aeroporto(self):
        codigo = input('Código do Aeroporto que deseja editar: ')
        cursor.execute(f'SELECT * FROM Aeroportos WHERE Código_Aeroporto="{codigo}"')
        linha = cursor.fetchone()
        if linha is None:
            print('\033[31mAeroporto não encontrado!\033[0m')
        else:
            print(f'{linha}')
            print('=-=' * 10)
            print('Qual campo que deseja alterar?')
            print('[1] Código_Aeroporto   [2] Nome_Aeroporto   [3] Sigla_Aeroporto\n'
                  '[4] Cidade   [5] Estado   [6] País   [7] Continente')
            op = int(input('Digite a opção desejada: '))
            lista = ['', 'Código_Aeroporto', 'Nome_Aeroporto', 'Sigla_Aeroporto', 'Cidade', 'Estado', 'País', 'Continente']
            x = input('Nova Informação: ')
            cursor.execute(f'UPDATE Aeroportos SET {lista[op]}="{x}" WHERE Código_Aeroporto="{codigo}"')
            conexao.commit()
            print('\033[35mAeroporto Atualizado!\033[0m')

    # ------------------------------------------------------------------------------------------------------------------
    def deletar_aeroporto(self):
        codigo = input('Código do Aeroporto que deseja deletar: ')
        cursor.execute(f'SELECT * FROM Aeroportos WHERE Código_Aeroporto="{codigo}"')
        linha = cursor.fetchone()
        if linha is None:
            print('\033[31mAeroporto não encontrado!\033[0m')
        else:
            cursor.execute(f'DELETE FROM Aeroportos WHERE Código_Aeroporto="{codigo}"')
            conexao.commit()
            print('\033[35mAeroporto Deletado!\033[0m')

    # ------------------------------------------------------------------------------------------------------------------
    def cadastrar_voo(self):
        codigo_voo = input('Código do Vôo: ')
        data_s = input('Data da Saída: ')
        hora_s = input('Hora da Saída: ')
        codigo_dec = input('Código do Aeroporto de Decolagem: ')
        cursor.execute(f'SELECT Código_Aeroporto FROM Aeroportos WHERE Código_Aeroporto="{codigo_dec}"')
        linha = cursor.fetchone()
        if linha is None:
            print('\033[31mAeroporto Não Cadastrado!\033[0m')
        else:
            codigo_des = input('Código do Aeroporto de Destino: ')
            cursor.execute(f'SELECT Código_Aeroporto FROM Aeroportos WHERE Código_Aeroporto="{codigo_des}"')
            linha = cursor.fetchone()
            if linha is None:
                print('\033[31mAeroporto Não Cadastrado!\033[0m')
            else:
                codigo_emp = input('Código da Empresa: ')
                cursor.execute(f'SELECT Código_Empresa FROM Empresas WHERE Código_Empresa="{codigo_emp}"')
                linha = cursor.fetchone()
                if linha is None:
                    print('\033[31mEmpresa Não Cadastrada!\033[0m')
                else:
                    passageiros = input('N° de Passageiros: ')
                    assentos = input('Assentos Disponíveis da Aeronave: ')
                    carga = input('Carga Carregada(kg) na Aeronave: ')
                    codigo_aer = input('Código da Aeronave: ')
                    cursor.execute(f'SELECT Código_Aeronave FROM Aeronaves WHERE Código_Aeronave="{codigo_aer}"')
                    linha = cursor.fetchone()
                    if linha is None:
                        print('\033[31mAeronave Não Cadastrada!\033[0m')
                    else:
                        data_c = input('Data da Chegada: ')
                        hora_c = input('Hora da Chegada: ')
                        natureza = input('Natureza do Vôo: ')
                        cursor.execute(
                            f'INSERT INTO Voos (Código_Voo, Data_Saída, Hora_Saída, Código_Aeroporto_Decolagem, Código_Aeroporto_Destino, '
                            f'Código_Empresa, N°Passageiros, Assentos_Disponíveis, Carga_Carregada_kg, Código_Aeronave, Data_Chegada, '
                            f'Hora_Chegada, Natureza_do_Voo)'
                            f'VALUES("{codigo_voo}", "{data_s}", "{hora_s}", "{codigo_dec}", "{codigo_des}", "{codigo_emp}", "{passageiros}", '
                            f'"{assentos}", "{carga}", "{codigo_aer}", "{data_c}", "{hora_c}", "{natureza}")'
                        )
                        conexao.commit()
                        print('\033[35mVôo Cadastrado!\033[0m')

    # ------------------------------------------------------------------------------------------------------------------
    def editar_voo(self):
        codigo = input('Código do Voo que deseja editar: ')
        cursor.execute(f'SELECT * FROM Voos WHERE Código_Voo="{codigo}"')
        linha = cursor.fetchone()
        if linha is None:
            print('\033[31mVôo não encontrado!\033[0m')
        else:
            print(f'{linha}')
            print('=-=' * 10)
            print('Qual campo que deseja alterar?')
            print('[1] Código_Voo   [2] Data_Saída   [3] Hora_Saída   [4] Código_Aeroporto_Decolagem\n'
                  '[5] Código_Aeroporto_Destino   [6] Código_Empresa   [7] N°Passageiros   [8] Assentos_Disponíveis\n'
                  '[9] Carga_Carregada_kg   [10] Código_Aeronave [11] Data_Chegada   [12] Hora_Chegada   [13] Natureza_do_Voo')
            op = int(input('Digite a opção desejada: '))
            lista = ['', 'Código_Voo', 'Data_Saída', 'Hora_Saída', 'Código_Aeroporto_Decolagem', 'Código_Aeroporto_Destino',
                     'Código_Empresa', 'N°Passageiros', 'Assentos_Disponíveis', 'Carga_Carregada_kg', 'Código_Aeronave',
                     'Data_Chegada', 'Hora_Chegada', 'Natureza_do_Voo']
            if op == 4:
                x = input('Nova Informação: ')
                cursor.execute(f'SELECT Código_Aeroporto FROM Aeroportos WHERE Código_Aeroporto="{x}"')
                linha = cursor.fetchone()
                if linha is None:
                    print('\033[31mAeroporto Não Cadastrado!\033[0m')
                else:
                    cursor.execute(f'UPDATE Voos SET Código_Aeroporto_Decolagem="{linha[0]}" WHERE Código_Voo="{codigo}"')
                    conexao.commit()
                    print('\033[35mVoo Atualizado!\033[0m')
            elif op == 5:
                x = input('Nova Informação: ')
                cursor.execute(f'SELECT Código_Aeroporto FROM Aeroportos WHERE Código_Aeroporto="{x}"')
                linha = cursor.fetchone()
                if linha is None:
                    print('\033[31mAeroporto Não Cadastrado!\033[0m')
                else:
                    cursor.execute(f'UPDATE Voos SET Código_Aeroporto_Destino="{linha[0]}" WHERE Código_Voo="{codigo}"')
                    conexao.commit()
                    print('\033[35mVoo Atualizado!\033[0m')
            elif op == 6:
                x = input('Nova Informação: ')
                cursor.execute(f'SELECT Código_Empresa FROM Empresas WHERE Código_Empresa="{x}"')
                linha = cursor.fetchone()
                if linha is None:
                    print('\033[31mEmpresa Não Cadastrada!\033[0m')
                else:
                    cursor.execute(f'UPDATE Voos SET Código_Empresa="{linha[0]}" WHERE Código_Voo="{codigo}"')
                    conexao.commit()
                    print('\033[35mVoo Atualizado!\033[0m')
            elif op == 10:
                x = input('Nova Informação: ')
                cursor.execute(f'SELECT Código_Aeronave FROM Aeronaves WHERE Código_Aeronave="{x}"')
                linha = cursor.fetchone()
                if linha is None:
                    print('\033[31mAeronave Não Cadastrada!\033[0m')
                else:
                    cursor.execute(f'UPDATE Voos SET Código_Aeronave="{linha[0]}" WHERE Código_Voo="{codigo}"')
                    conexao.commit()
                    print('\033[35mVoo Atualizado!\033[0m')
            else:
                x = input('Nova Informação: ')
                cursor.execute(f'UPDATE Voos SET {lista[op]}="{x}" WHERE Código_Voo="{codigo}"')
                conexao.commit()
                print('\033[35mVôo Atualizado!\033[0m')

    # ------------------------------------------------------------------------------------------------------------------
    def deletar_voo(self):
        codigo = input('Código do Vôo que deseja deletar: ')
        cursor.execute(f'SELECT * FROM Voos WHERE Código_Voo="{codigo}"')
        linha = cursor.fetchone()
        if linha is None:
            print('\033[31mVôo não encontrado!\033[0m')
        else:
            cursor.execute(f'DELETE FROM Voos WHERE Código_Voo="{codigo}"')
            conexao.commit()
            print('\033[35mVôo Deletado!\033[0m')

    # ------------------------------------------------------------------------------------------------------------------
    def relatorio_periodo(self):
        data = input('Data da Saída: ')
        cursor.execute(f'SELECT * FROM Voos WHERE Data_Saída="{data}"')
        linha = cursor.fetchone()
        if linha is None:
            print('\033[31mVôo não encontrado!\033[0m')
        else:
            cursor.execute(f'SELECT * FROM Voos WHERE Data_Saída="{data}"')
            linha = cursor.fetchall()
            print('=-=' * 10)
            print(f'\033[33mVôos que Decolaram {data}\033[0m')
            print('----' * 5)
            for i in range(0, len(linha)):
                print(f'No Vôo {linha[i][1]}, tiveram \033[96m{linha[i][7]}\033[0m passageiros,\n'
                      f'em \033[96m{linha[i][8]}\033[0m assentos disponíveis, sendo ocupados\n'
                      f'\033[96m{round((linha[i][7] / linha[i][8]) * 100, 2)}%\033[0m dos assentos, e carregando \033[96m{linha[i][9]}kg\033[0m')
                print('----' * 5)

    # ------------------------------------------------------------------------------------------------------------------
    def relatorio_empresa(self):
        empresa = input('Empresa: ')
        cursor.execute(f'SELECT * FROM Voos WHERE Código_Empresa="{empresa}"')
        linha = cursor.fetchone()
        if linha is None:
            print('\033[31mVôo não encontrado!\033[0m')
        else:
            cursor.execute(f'SELECT * FROM Voos WHERE Código_Empresa="{empresa}"')
            linha = cursor.fetchall()
            print('=-=' * 10)
            print(f'\033[33mVôos com a Empresa {empresa}\033[0m')
            print('----' * 5)
            for i in range(0, len(linha)):
                print(f'No Vôo {linha[i][1]}, tiveram \033[96m{linha[i][7]}\033[0m passageiros,\n'
                      f'em \033[96m{linha[i][8]}\033[0m assentos disponíveis, sendo ocupados\n'
                      f'\033[96m{round((linha[i][7] / linha[i][8]) * 100, 2)}%\033[0m dos assentos, e carregando \033[96m{linha[i][9]}kg\033[0m')
                print('----' * 5)

    # ------------------------------------------------------------------------------------------------------------------
    def relatorio_aeroporto(self):
        aeroporto = input('Aeroporto de Decolagem: ')
        cursor.execute(f'SELECT * FROM Voos WHERE Código_Aeroporto_Decolagem="{aeroporto}"')
        linha = cursor.fetchone()
        if linha is None:
            print('\033[31mVôo não encontrado!\033[0m')
        else:
            cursor.execute(f'SELECT * FROM Voos WHERE Código_Aeroporto_Decolagem="{aeroporto}"')
            linha = cursor.fetchall()
            print('=-=' * 10)
            print(f'\033[33mVôos com a Decolagem no Aeroporto {aeroporto}\033[0m')
            print('----' * 5)
            for i in range(0, len(linha)):
                print(f'No Vôo {linha[i][1]}, tiveram \033[96m{linha[i][7]}\033[0m passageiros,\n'
                      f'em \033[96m{linha[i][8]}\033[0m assentos disponíveis, sendo ocupados\n'
                      f'\033[96m{round((linha[i][7] / linha[i][8]) * 100, 2)}%\033[0m dos assentos, e carregando \033[96m{linha[i][9]}kg\033[0m')
                print('----' * 5)
