import sys


def solve(s: str, t: str) -> None:
    distance = sum(a != b for a, b in zip(s, t))
    print(distance)


if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    solve(s, t)