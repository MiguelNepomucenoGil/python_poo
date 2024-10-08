def operar_carro():
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

        if op == 1:
            carro1.ligar()
        elif op == 2:
            carro1.desligar()
        elif op == 3:
            v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro1.acelerar(v, t)


from frota import *

if __name__ == "__main__":
    print('Cadastre um carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')

    kms = float(input('Digite com quantos Kms: '))

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, kms, motor=False)

    print('Cadastre um carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')

    kms = float(input('Digite com quantos Kms: '))

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, kms, motor=False)

    '''
    Controlando o carro até ele atingir 600 Km
    '''
    while carro1.odometro < 600 and carro2.odometro < 600:
        try:

            op = 0
            while op not in (1, 2):
                op = int(input("Qual carro [1,2]? "))

            if op == 1:
                operar_carro(carro1)
            else:
                operar_carro(carro2)

            print('Infos atuais do carro')
            print(carro1)
        except Exception as e:
            print("Erro!")
            print(e)

    carro1.desligar()
    carro2.desligar()
    print(carro1)
    print(carro2)
    print('Parar para trocar óleo!!!')