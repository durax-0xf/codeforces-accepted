def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for x in a:
        ans += x in b
    print(ans)
 
t = int(input())
for _ in range(t):
    solve()