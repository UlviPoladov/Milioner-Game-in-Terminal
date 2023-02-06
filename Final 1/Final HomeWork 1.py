import random
import os
import time
from Joker import *
from questionsdb import *
from rich.console import Console
loading = ['Suallar Yükləndi', 'Oyun Yaradıldı', 'Jokerlər Yükləndi']
console = Console()
tasks = [f"{n}" for n in loading]

# with console.status("[bold green]Yüklənir...") as status:
#     while tasks:
#         task = tasks.pop(0)
#         time.sleep(2)
#         console.log(f"{task}")
#     time.sleep(2)   
#     os.system('cls')

counttt=0
balance = 0
balanceList = [100, 500, 1000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]

def jokers(): # Jokerleri Göstermek Üçün
    if joker == []:
        print("\t\t\t\tHeç Bir Joker Hakkın Yoxdu!")
    else:
        print("\t\t\t\t\tJoker Hakkların: ", end=' ')
        for i in range(len(joker)):
            print(f'{i+1}) {joker[i]} ', end=' ')
        print()

def money(raund): # Mükafat
    global balance
    balance = balanceList[raund-1]
    return balance

def baraj(): # Baraj
    global balance
    global counttt
    def winMessage(balance):
        global counttt
        print(f"Baraj sualına cavab verdiniz və {balance}$ qazandınız mükafatı götürüb çəkilə bilərsiniz və ya risk edib davam edə bilərsiniz (Not: əgər səhv suala cavab versəniz hər hansısa mükafata sahib OLMAYCAQSINIZ!)")
        op = input("Seçiminiz (Tamam(t) ya Davam(d)): ")
        counttt+=1
        if op.lower() == "t":
            print(f"Təbriklər!!! Kim Milyoner Olmaq İstəyər Yarışından {balance}$ Qazandınız!!!")
            quit()
        else:
            pass
    
           
    if balance == 1000:
        
        winMessage(balance)
    elif balance == 8000:
        
        winMessage(balance) 
    elif balance == 32000:
        
        winMessage(balance)
    elif balance == 1000000:
        
        print(f"\U0001F389 Təbriklər Siz Kim Milyoner Olmaq İstəyər yarışının verilmiş 12 sualına səhv olmadan cavab verdiniz və {balance}$ olan böyük mükafatı əldə ettiniz!!!")
        quit()

def Game(): # Oyun
    global counttt
    a = questions[0].split(":")
    b = a[1].split()
    randomquestions = random.sample(range(12), 12) # Təkrarlanmayacaq random rəqəmlər (list)
    randomanswers = random.sample(range(4), 4) # Təkrarlanmayacaq random rəqəmlər (list)
    counter = 1
    for i in randomquestions:
        a = questions[i].split(":")
        b = a[1].split(",")
        while True:
            print(f'\t\t\t\t\t--------------------- Sual {counter} ---------------------\n')
            print(f'\t\t\t\t\t{a[0]}') 
            print(f'\t\t\t\t\t    A: {b[randomanswers[0]]}       B: {b[randomanswers[1]]}\n\t\t\t\t\t    C: {b[randomanswers[2]]}       D: {b[randomanswers[3]]}')
            jokers()
            op = input("\t\t\t\t\tSeçim Edin: ")
            if op.lower() == 'a':
                if b[randomanswers[0]] in correctanswers:
                    print(f"Doğru Cavab! {money(counter)}$ Qazandın!")
                    baraj()
                    counter += 1
                    time.sleep(2)
                    os.system("cls")
                    break
                else:
                    if counttt==1:
                        print("Yanlış Cavab! Təəsüflər Olsunki Siz Sadece 1000$ Qazandiniz")
                    elif counttt==2:
                        print("Yanlış Cavab! Təəsüflər Olsunki Siz Sadece 8000$ Qazandiniz")
                    elif counttt==3:
                        print("Yanlış Cavab! Təəsüflər Olsunki Siz Sadece 32000$ Qazandiniz")
                    else:
                        print("Yanlış Cavab! Təəsüflər Olsunki Siz Hecne Qazana Bilmediniz")
                    counter += 1
                    quit()
            elif op.lower() == 'b':
                if b[randomanswers[1]] in correctanswers:
                    print(f"Doğru Cavab! {money(counter)}$ Qazandın!")
                    baraj()
                    counter += 1
                    time.sleep(2)
                    os.system("cls")
                    break
                else:
                    if counttt==1:
                        print("Yanlış Cavab! Təəsüflər Olsunki Siz Sadece 1000$ Qazandiniz")
                    elif counttt==2:
                        print("Yanlış Cavab! Təəsüflər Olsunki Siz Sadece 8000$ Qazandiniz")
                    elif counttt==3:
                        print("Yanlış Cavab! Təəsüflər Olsunki Siz Sadece 32000$ Qazandiniz")
                    else:
                        print("Yanlış Cavab! Təəsüflər Olsunki Siz Hecne Qazana Bilmediniz")
                    counter += 1
                    quit()
            elif op.lower() == 'c':
                if b[randomanswers[2]] in correctanswers:
                    print(f"Doğru Cavab! {money(counter)}$ Qazandın!")
                    baraj()
                    counter += 1
                    time.sleep(2)
                    os.system("cls")
                    break
                else:
                    if counttt==1:
                        print("Yanlış Cavab! Təəsüflər Olsunki Siz Sadece 1000$ Qazandiniz")
                    elif counttt==2:
                        print("Yanlış Cavab! Təəsüflər Olsunki Siz Sadece 8000$ Qazandiniz")
                    elif counttt==3:
                        print("Yanlış Cavab! Təəsüflər Olsunki Siz Sadece 32000$ Qazandiniz")
                    else:
                        print("Yanlış Cavab! Təəsüflər Olsunki Siz Hecne Qazana Bilmediniz")
                    counter += 1
                    quit()
            elif op.lower() == 'd':
                if b[randomanswers[3]] in correctanswers:
                    print(f"Doğru Cavab! {money(counter)}$ Qazandın!")
                    baraj()
                    counter += 1
                    time.sleep(2)
                    os.system("cls")
                    break
                else:
                    if counttt==1:
                        print("Yanlış Cavab! Təəsüflər Olsunki Siz Sadece 1000$ Qazandiniz")
                    elif counttt==2:
                        print("Yanlış Cavab! Təəsüflər Olsunki Siz Sadece 8000$ Qazandiniz")
                    elif counttt==3:
                        print("Yanlış Cavab! Təəsüflər Olsunki Siz Sadece 32000$ Qazandiniz")
                    else:
                        print("Yanlış Cavab! Təəsüflər Olsunki Siz Hecne Qazana Bilmediniz")
                    counter += 1
                    quit()
            elif op.lower() == '1':
                if 0 < int(op.lower()) < len(joker)+1:
                    jokerss(int(op.lower()), a[0], b[randomanswers[0]], b[randomanswers[1]], b[randomanswers[2]], b[randomanswers[3]])
                else:
                    print("Unexpected Error!")
            elif op.lower() == '2':
                if 0 < int(op.lower()) < len(joker)+1:
                    jokerss(int(op.lower()), a[0], b[randomanswers[0]], b[randomanswers[1]], b[randomanswers[2]], b[randomanswers[3]])
                else:
                    print("Unexpected Error!")
            elif op.lower() == '3':
                if 0 < int(op.lower()) < len(joker)+1:
                    jokerss(int(op.lower()), a[0], b[randomanswers[0]], b[randomanswers[1]], b[randomanswers[2]], b[randomanswers[3]])
                else:
                    print("Unexpected Error!")
            else:
                print("Wrong Choice!")

print("\t\t\t\t\tKim milyoner olmaq isdəyər oyununa xoş gəldiniz!")
print("\t\t\t\t\t\t\t1) Oyuna Başla\n\t\t\t\t\t\t\t2) Qaydalar\n\t\t\t\t\t\t\t3) Çıxış")
while True:
    operator = input("\n\t\t\t\t\tSeçim Edin: ")
    if operator == "1":
        Game()
    elif operator == "2":
        print("Qaydalar -> https://bul.tc/PFWG")
    elif operator == "3":
        print("Çıxış Edildi.")
        quit()
    else:
        print("\t\t\t\t\t\t\t1) Oyuna Başla\n\t\t\t\t\t\t\t2) Qaydalar\n\t\t\t\t\t\t\t3) Çıxış")