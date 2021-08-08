'''
_____
|   |
|   O
|  /|\
|  / \
|____
'''
import random

def acak_kata ():
    mylist = [["K","U","D","A"], ["Z","E","B","R","A"], ["S","U","S","U"],['I','C','E','C','R','E','A','M']]
    rand_list = random.choice(mylist)
    if rand_list == ["K","U","D","A"] :
        print("\nClue : 4 Huruf, Temen-nya Pak Kusir\n")
    elif rand_list == ["Z","E","B","R","A"] :
        print("\nClue : 5 Huruf, yang suka bantuin kita nyebrang jalan raya\n")
    elif rand_list == ["S","U","S","U"] :
        print("\nClue : 4 Huruf, minuman hasil dari perasan mamalia\n")
    elif rand_list == ['I','C','E','C','R','E','A','M'] :
        print("\nClue : 8 Huruf, I scream You scream\n")

    return rand_list
    
def tebak():
    n = 1
    list1 = acak_kata()
    list2 = ["_" for i in range(len(list1))]
    salah = 0
    benar = False
    while salah !=6 or benar == True:
        huruf = input(f"Attempts {n} :").upper()
        n+=1
        if huruf in list1:
            for i in range(len(list1)):
                if huruf == list1[i]:
                    list2[i] = huruf
        else : 
            salah +=1
        for j in range(len(list2)):
            print(list2[j],end=" ")
        print()
        gambar(salah)
        print()
        if list1 == list2 :
            benar = True
            print("Selamat anda menang!\n")
            break      

def gambar (salah):
    if salah==1 :
        print("_____")
    if salah == 2:
        print("_____")
        print("|   |")
    if salah == 3 :
        print("_____")
        print("|   |")
        print("|   O")
    if salah == 4 :
        print("_____")
        print("|   |")
        print("|   O")
        print('|  /|\\')
    if salah == 5:
        print("_____")
        print("|   |")
        print("|   O")
        print("|  /|\\")   
        print("|  / \\")
    if salah == 6:
        print("_____")
        print("|   |")
        print("|   O")
        print("|  /|\\")
        print("|  / \\")
        print("|____")
        print("\nYou are dead!")   

print("***** HANGMAN *****")
pil = "y"
while pil != "n":
    tebak()
    pil = input("Do you want to play again? (y/n)").lower()
    