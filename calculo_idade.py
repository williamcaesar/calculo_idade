#! /usr/bin/env python3
x = 0
meses_31 = [1,3,5,7,8,10,12]
meses_30 = [4,6,9,11]
meses_28 = [2]

nome = input("Qual o seu nome? ")
ano = input("Que ano você nasceu? ")
mes = input("Que mês? ")
dia = input("Que dia? ")
idade = 2017-int(ano)
mes_nome = {1:"Janeiro",
            2:"Fevereiro",
            3:"Março",
            4:"Abril",
            5:"Maio",
            6:"Junho",
            7:"Julho",
            8:"Agosto",
            9:"Setembro",
            10:"Outubro",
            11:"Novembro",
            12:"Dezembro"}
try:
    print("Olá",nome,"você nasceu em",dia,"de",mes_nome[int(mes)],"de",ano,"então você tem",idade,"anos")
except Exception as e:
    print ("Dados invalidos!")
