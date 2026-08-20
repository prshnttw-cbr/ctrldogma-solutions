import sys


def solve(s: str, t: str) -> None:
    positions = []

    for i in range(len(s) - len(t) + 1):
        if s[i:i + len(t)] == t:
            positions.append(i + 1)  # 1-based position

    print(*positions)


if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    solve(s, t)