import sys


def solve(t: str) -> None:
    rna = t.replace("T", "U")
    print(rna)


if __name__ == "__main__":
    t = sys.stdin.readline().strip()
    solve(t)