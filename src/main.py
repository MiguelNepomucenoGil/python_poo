from frota import *

if __name__ == "__main__":
    print('Cadastre um carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    kms = float(input('Digite com quantos Kms: '))
    litros = float(input("Informe o nivel do tanque: "))
    cm = float(input("COnsumo medio: "))

    print('Cadastre outro carro')
    nm_modelo2 = input('Digite o modelo: ')
    nm_marca2 = input('Digite a marca: ')
    nm_cor2 = input('Digite a cor: ')
    kms2= float(input('Digite com quantos Kms: '))
    litros2 = float(input("Informe o nivel do tanque: "))
    cm2 = float(input("COnsumo medio: "))

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, kms, True, litros, cm)
    carro2 = Carro(nm_modelo2, nm_marca2, nm_cor2, kms2, True, litros2, cm2)



    '''
    Controlando o carro até ele atingir 10000km ou 600km

    '''
    while carro1.odometro < 600 and carro2.odometro < 600:
        escolha = input('Escolha: carro1 ou carro2')
        try:
          
            
            if escolha == "carro1": 
                print('1- Ligar motor')
                print('2- Desligar motor')
                print('3- Acelerar')

                op = 0
                while op not in (1,2,3):
                    op = int(input("Digite as opcoes[1-3]: "))

                if op == 1:
                    carro1.ligar()
                elif op == 2:
                    carro1.desligar()
                elif op == 3:
                    v = float(input("Informe a velocidade: "))
                    t = float(input("Informe o tempo: "))
                    carro1.acelerar(v, t)
                
                if carro1 == 600:
                    print("carro1 ganhou!")
                elif carro2 == 600:
                    print("carro2 ganhou!")

            elif escolha == "carro2": 
                print('1- Ligar motor')
                print('2- Desligar motor')
                print('3- Acelerar')

                op = 0
                while op not in (1,2,3):
                    op = int(input("Digite as opcoes[1-3]: "))

                if op == 1:
                    carro2.ligar()
                elif op == 2:
                    carro2.desligar()
                elif op == 3:
                    v = float(input("Informe a velocidade: "))
                    t = float(input("Informe o tempo: "))
                    carro2.acelerar(v, t)

    

              


        except Exception as e:
                print("Erro!")
                print(e)







