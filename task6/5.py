s=int(input())
for _ in range(s):
    count=0
    for c in input():
        if c == "hackerrank"[count]:
            count += 1
            if count==len("hackerrank"):
                print("YES")
                break
    else:
        print("NO")