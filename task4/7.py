
from collections import defaultdict
def Anagrams(words):
    groupedWords = defaultdict(list)

    for word in words:
        groupedWords["".join(sorted(word))].append(word)

    for group in groupedWords.values():
        print(" ".join(group))

n=int(input("enter the number of words:"))
arr=[]
for i in range (0,n):
  w=str(input())
  arr.append(w)
Anagrams(arr)

