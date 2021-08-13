def anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)
    
    oneword=str(input("Enter the first word: "))
    twoword=str(input("Enter the second word: "))

print(anagram(oneword,twoword))
