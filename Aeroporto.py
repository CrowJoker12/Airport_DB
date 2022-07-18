import Aeroporto_Defs as ad

dados = ad.Aviao()
print('=-=' * 10)

while True:
    def escolher():
        print('''\033[96mBem Vindo! Selecione as opções que desejar!\033[0m
            [1] \033[32mCadastrar Aeronave\033[0m    [2] \033[35mEditar Aeronave\033[0m    [3] \033[31mDeletar Aeronave\033[0m
            [4] \033[32mCadastrar Empresa\033[0m     [5] \033[35mEditar Empresa\033[0m     [6] \033[31mDeletar Empresa\033[0m
            [7] \033[32mCadastrar Aeroporto\033[0m   [8] \033[35mEditar Aeroporto\033[0m   [9] \033[31mDeletar Aeroporto\033[0m
            [10] \033[32mCadastrar Vôo\033[0m        [11] \033[35mEditar Vôo\033[0m        [12] \033[31mDeletar Vôo\033[0m
            [13] \033[96mRelatório Período\033[0m    [14] \033[96mRelatório Empresa\033[0m [15] \033[96mRelatório Aeroporto\033[0m
            [16] Terminar Algoritmo''')
        opcao = int(input('Opção: '))
        return opcao


    def op1():
        try:
            dados.cadastrar_aeronave()
        except:
            print('\033[31mAeronave já Cadastrada\033[0m')
        print('=-=' * 10)


    def op2():
        try:
            dados.editar_aeronave()
        except:
            print('\033[31mAeronave já Cadastrada\033[0m')
        print('=-=' * 10)


    def op3():
        dados.deletar_aeronave()
        print('=-=' * 10)


    def op4():
        try:
            dados.cadastrar_empresa()
        except:
            print('\033[31mEmpresa já Cadastrada\033[0m')
        print('=-=' * 10)


    def op5():
        try:
            dados.editar_empresa()
        except:
            print('\033[31mEmpresa já Cadastrada\033[0m')
        print('=-=' * 10)


    def op6():
        dados.deletar_empresa()
        print('=-=' * 10)


    def op7():
        try:
            dados.cadastrar_aeroporto()
        except:
            print('\033[31mAeroporto já Cadastrado\033[0m')
        print('=-=' * 10)


    def op8():
        try:
            dados.editar_aeroporto()
        except:
            print('\033[31mAeroporto já Cadastrado\033[0m')
        print('=-=' * 10)


    def op9():
        dados.deletar_aeroporto()
        print('=-=' * 10)


    def op10():
        try:
            dados.cadastrar_voo()
        except:
            print('\033[31mVôo já Cadastrado\033[0m')
        print('=-=' * 10)


    def op11():
        try:
            dados.editar_voo()
        except:
            print('\033[31mVôo já Cadastrado\033[0m')
        print('=-=' * 10)


    def op12():
        dados.deletar_voo()
        print('=-=' * 10)


    def op13():
        dados.relatorio_periodo()
        print('=-=' * 10)


    def op14():
        dados.relatorio_empresa()
        print('=-=' * 10)


    def op15():
        dados.relatorio_aeroporto()
        print('=-=' * 10)


    def op16():
        print('=-=' * 10)
        print('\033[37mTerminando...\033[0m')


    dic = {1: op1, 2: op2, 3: op3, 4: op4,
           5: op5, 6: op6, 7: op7, 8: op8,
           9: op9, 10: op10, 11: op11, 12: op12,
           13: op13, 14: op14, 15: op15, 16: op16}

    opcao_escolhida = escolher()
    dic[opcao_escolhida]()
    if opcao_escolhida == 16:
        break
