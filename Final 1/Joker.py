import random

correctanswers = ["Beş", "Hündürlük", "Yuri_Qaqarin", "Avrora", "19-cu_əsr", "Personaj", "Napoli", "Kotan", "Aksiz_markası", "Kobalt", "Dama", "Merkuri", "Hippokrat", "Qaş", "Əsgərlər"]
joker = ["Dosta Zəng", "Yarı Yarıya", "İzləyicilərdən Soruş"]
adlar = ["Cavid", "Rəsul", "Sukur", "Ulvi", "Yusif", "Nihat"]
dialoqlar = ["Hmm Maraqlı Sualdı. Məncə Cavab", "Çətin Yerdən Gəldi Ama Məncə Cavab", "Cavab Çox Sadədir Məncə Cavab"]
tempList = []

def randomDialog(): # Balaca bir detay
    num = random.randint(0, 2)
    return dialoqlar[num]

def checkJoker(type, cavabA, cavabB, cavabC, cavabD): # Joker hakkların funksiyaları
    cavablar = []
    correctAns = []
    cavablar.append(cavabA)
    cavablar.append(cavabB)
    cavablar.append(cavabC)
    cavablar.append(cavabD)  
    if cavabA in correctanswers:
        correctAns.append(cavabA)
    elif cavabB in correctanswers:
        correctAns.append(cavabB)
    elif cavabC in correctanswers:
        correctAns.append(cavabC)
    elif cavabD in correctanswers:
        correctAns.append(cavabD)

    cavablar.remove(correctAns[0])
    randnum = random.randint(0, 2)
    correctAns.append(cavablar[randnum])
    faiz = random.randint(1, 100)
    
    if type == 'Dosta Zəng':
        if tempList:
            if faiz < 10:
                return correctAns[1]
            else:
                return correctAns[0] # Düzgün Cavab
        else:
            if faiz < 10:
                return correctAns[1]
            else:
                return correctAns[0] # Düzgün Cavab
    elif type == 'Yarı Yarıya':
        a = f'{correctAns[0]} ya da {correctAns[1]}'
        tempList.append(correctAns[0])
        tempList.append(correctAns[1])
        return a
    elif type == 'İzləyicilərdən Soruş':
        list = []
        one = two = three = four = 0
        one1 = two1 = 0
        for i in range(10):
            num = random.randint(1, 100)
            list.append(num)
        for i in list:
            if i < 26:
                one += 1
            elif 25 < i < 51:
                two += 1
            elif 50 < i < 76:
                three += 1
            elif 75 < i < 101:
                four += 1
            elif i < 51:
                one1 += i
            elif 50 < i < 101:
                two1 += 1
        if tempList:
            if one1 < two1:
                a = f'A: {cavablar[2]} {four*10}% B: {tempList[1]} {(two*10)-10}% C: {cavablar[1]} {three*10}% D: {tempList[0]} {(one*10)+30}%'
                return a
            elif two1 < one1:
                a = f'A: {tempList[0]} {(one*10)+30}% B: {tempList[1]} {(two*10)-10}% C: {cavablar[0]} {(three*10)-10}% D: {cavablar[2]} {(four*10)-10}%'
                return a
            else:
                a = f'A: {tempList[1]} {(two*10)-10}% B: {tempList[0]} {(one*10)+30}% C: {cavablar[0]} {(three*10)-10}% D: {cavablar[2]} {(four*10)-10}%'
                return a
        else:
            if one < two and one < three and one < four:
                a = f'A: {correctAns[0]} {(one*10)+10}% B: {cavablar[0]} {(two*10)-10}% C: {cavablar[1]} {three*10}% D: {cavablar[2]} {four*10}%'
                return a
            elif two < one and two < three and two < four:
                a = f'A: {cavablar[1]} {(one*10)+10}% B: {cavablar[0]} {(two*10)-10}% C: {correctAns[0]} {three*10}% D: {cavablar[2]} {four*10}%'
                return a
            elif three < one and three < two and three < four:
                a = f'A: {cavablar[1]} {one*10}% B: {cavablar[0]} {two*10}% C: {correctAns[0]} {(three*10)+10}% D: {cavablar[2]} {(four*10)-10}%'
                return a
            elif four < one and four < two and two < three:
                a = f'A: {cavablar[1]} {(one*10)+10}% B: {cavablar[0]} {(two*10)-10}% C: {correctAns[0]} {three*10}% D: {cavablar[2]} {four*10}%'
                return a
            else:
                a = f'A: {correctAns[0]} {one*10}% B: {cavablar[0]} {two*10}% C: {cavablar[1]} {three*10}% D: {cavablar[2]} {four*10}%'
                return a

def jokerss(num, sual, cavabA, cavabB, cavabC, cavabD):
    if joker[num-1] == "Dosta Zəng":
        randnum = random.randint(0, 5)
        print(f"Dosta Zəng Edilir...\n- ...\n-Sən: Salam  {adlar[randnum]} Kim Milyonr Olmaq istəyər yarışına qatılmışam və bir sualda çətinlik çəkirəm sənin köməyin lazımdı. Sual belədi: {sual} və Variantlar isə belədir: A:{cavabA} B:{cavabB} C:{cavabC} D:{cavabD}\n-{adlar[randnum]}: {randomDialog()} {checkJoker('Dosta Zəng', cavabA, cavabB, cavabC, cavabD)}")
        joker.remove("Dosta Zəng")
    elif joker[num-1] == "Yarı Yarıya":
        print(f"Yarı Yarıya Joker Hakkından İstifadə Etdin. Doğru Cavab Verilenlerden Biridir: {checkJoker('Yarı Yarıya', cavabA, cavabB, cavabC, cavabD)}")
        joker.remove("Yarı Yarıya")
    elif joker[num-1] == "İzləyicilərdən Soruş":
        print(f"İzləyicilərdən Soruş Joker Hakkından İstifadə Etdin. İzləyicilər öz cavalarını verdilər və nəticə belədir: {checkJoker('İzləyicilərdən Soruş', cavabA, cavabB, cavabC, cavabD)}")
        joker.remove("İzləyicilərdən Soruş")