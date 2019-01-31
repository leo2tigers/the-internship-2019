import random
import time
import os

def main():
    print("Welcome\n")
    print("1. Play\n2. Exit\n")
    print("Please enter your selection : ", end='')

    selection = '0'

    while(selection != '1' and selection != '2'):
        selection = input().strip()
        if selection == '2':
            print("Good Bye.")
            return
        elif selection == '1':
            catselect()
        else:
            print("Invalid input!!!")
            print("Please enter your selection again : ", end='')

def catselect():
    print("Please select category from the following\n")
    print("1. Songs from maimai")
    print("2. National parks in Thailand")
    print("3. Return to main menu")
    print("Please enter your selection : ", end='')

    selectedCat = '0'

    while(selectedCat != '1' and selectedCat != '2' and selectedCat != '3'):
        selectedCat = input().strip()
        if(selectedCat == '1' or selectedCat == '2'):
            game(int(selectedCat))
        elif(selectedCat == '3'):
            main()
        else:
            print("Invalid input!!!")
            print("Please enter your selection again : ", end='')

def game(category):
    f = open("res/"+str(category)+".txt", 'r')
    wordSel = random.randint(1, 7)
    for i in range(wordSel):
        mString = f.readline()
    delimLoc = mString.find("|")
    word = mString[:delimLoc-1]
    hint = mString[delimLoc+2:]
    listOfLetter = list(word)
    checkerList = list(word.lower())
    correctLetter = list()
    wrongLetter = list()
    showCtrlList = list()
    for i in listOfLetter:
        if("A" <= i <= "Z" or "a" <= i <= "z"):
            showCtrlList.append(False)
        else:
            showCtrlList.append(True)

    life = 8
    score = 0
    startTime = time.time()
    finalCheck = False

    print("\nHint : "+hint)

    while(life > 0):
        for i in range(len(listOfLetter)):
            print(listOfLetter[i] if showCtrlList[i] else "_", end=' ')
        print("\n")
        print("Life : "+str(life)+" | Score : "+str(score)+ " | Incorrect letters used : ", end='')
        print(*wrongLetter)
        print("Enter your guess : ", end='')
        guess = input().strip().lower()
        print("\n")

        if((guess in wrongLetter) or (guess in correctLetter)):
            print("This letter was already used.\n")
            continue

        if(len(guess) > 1):
            print("Invalid input, please enter only single English alphabet.\n")
            continue

        if("a" <= guess <= "z"):
            if guess not in checkerList:
                print("Incorrect.\n")
                life -= 1
                wrongLetter.append(guess)
            else:
                for i in range(len(checkerList)):
                    if guess == checkerList[i]:
                        showCtrlList[i] = True
                        score += (15 + life)
                correctLetter.append(guess)
        else:
            print("Invalid input, please enter only single English alphabet.\n")
            continue

        for i in showCtrlList:
            if i == False: break
        else: finalCheck = True

        if(finalCheck): break 

        #life = -1

    if(finalCheck):
        timeFinished = time.time()
        timeUsed = timeFinished - startTime
        timeBonus = int(3000//timeUsed)

        print(*listOfLetter)
        print("\nCongratulations!!!\n")
        print("Base score : "+str(score)+" | Time bonus : "+str(timeBonus)+" | Final score : "+str(score+timeBonus))
    else:
        print("\nGame Over.\n")
        print("Final score : "+str(score))

    os.system("pause")
    print("\n")
    main()    

main()