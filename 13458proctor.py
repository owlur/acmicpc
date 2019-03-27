N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

print(sum((1 + (a-B)//C + int(bool((a-B) % C)) if a > B else 1 for a in A)))