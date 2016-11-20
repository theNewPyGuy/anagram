from random import choice
from datetime import datetime
from dependencies import *

english = englishWords()

def anagram(word):
    if len(word) == 3:
        to_array = SplitA(word)
        universal = []
        for i in range(0, len(to_array)):
            mirror_to_array = Mirror(to_array)
            current_char = mirror_to_array[i]
            mirror_to_array.remove(current_char)
            two_anagram = []
            mirror_mirror_to_array = Mirror(mirror_to_array)
            for t in range(0, len(mirror_to_array)):
                mirror_mirror_to_array = reverse(mirror_mirror_to_array)
                two_anagram.append(toString(mirror_mirror_to_array))
            for item in two_anagram:
                word = current_char + item
                if word not in universal:
                    universal.append(word)
        return universal
    else:
        UNIVERSAL = []
        TO_ARRAY = SplitA(word)
        for q in range(0, len(word)):
            MIRROR_TO_ARRAY = Mirror(TO_ARRAY)
            CURRENT_CHAR= MIRROR_TO_ARRAY[q]
            MIRROR_TO_ARRAY.remove(CURRENT_CHAR)
            WORD_LESS_ONE = anagram(toString(MIRROR_TO_ARRAY))
            for ITEMS in WORD_LESS_ONE:
                WORD = CURRENT_CHAR + ITEMS
                if WORD not in UNIVERSAL:
                    UNIVERSAL.append(CURRENT_CHAR + ITEMS)
        return UNIVERSAL    

INPUT = str(raw_input("Enter word: "))
print "Please wait..."
Anagrams = anagram(INPUT)

print "There are", len(Anagrams),"possible anagrams for", INPUT
print "How do you want to view them?"
View = str(raw_input("Filtered For english words(F), Unfiltered(U)? :  "))
if View == 'U':
    data = Mirror(Anagrams)
    TYPE = "Unfiltered"
else:
    data = []
    jargon = []
    if " " in INPUT:
        for I in Anagrams:
            Split = I.split(' ')
            W = 0
            for U in Split:
                try:
                    if english[U] == "english":  
                        W += 1
                except KeyError as E:
                    break
            if W == len(Split) and I[0] != " " and I[-1] != " ":
                print I," is english"
                data.append(I)
    else:
        for i in Anagrams:
            try:
                if english[i] == "english":
                    data.append(i)
            except KeyError as e:
                jargon.append(e)

    if len(data) == 0:
        data.append("No anagram")

    TYPE = "Filtered"


print "Please wait..."
date = "="*70+ "  " +str(datetime.now().date())+"  " + "="*70 + "\n"
title = "Anagram for: '"+str(INPUT) + "';    --- Type: "+TYPE+"\n"
w2F('anagrams.txt', date+title)
for i in data:
    writeThis = i + "\n"
    w2F('anagrams.txt', writeThis)
    
print "Your anagram is ready. just check anagrams.txt"
