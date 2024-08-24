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
    while carro1.odometro < 600 and carro2.odometro < 600 and (carro1.tanque > 0  or carro2.tanque > 0):
        escolha = input('Escolha: carro1 ou carro2')
        try:
          op = carro1


    

              


        except Exception as e:
                print("Erro!")
                print(e)







