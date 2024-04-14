import sys
from collections import UserDict

input = sys.stdin.readline
word_dict = UserDict()

N,M = map(int,input().split())
for _ in range(N):
    word = str(input().rstrip())
    len_word = len(word)
    if len_word<M:
        continue
    if word in word_dict:
        word_dict[word][0]+=1
    else:
        word_dict[word]=[1,len_word]

for w,v in sorted(word_dict.items(), key=lambda x: (-x[1][0],-x[1][1],x[0])):
    print(w)
    