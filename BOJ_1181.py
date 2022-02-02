import sys
n=int(sys.stdin.readline())
word=[str(sys.stdin.readline()) for _ in range(n)]
s=set(word)
word=list(s)
word.sort()
word=sorted(word, key=lambda x: len(x))
for w in word:
    print(w, end='')