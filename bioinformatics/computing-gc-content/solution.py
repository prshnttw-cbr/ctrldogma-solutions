def solve(s):
    gc = s.count('G') + s.count('C')
    print(f"{gc * 100 / len(s):.2f}")

s = input().strip()
solve(s)
