import sys


def solve(s: str) -> None:
    # Write your solution here.
    # Print the counts of A, C, G, T in that order.
    print(s.count("A"), s.count("C"), s.count("G"), s.count("T"))


if __name__ == "__main__":
    s = sys.stdin.readline().strip()  # The DNA sequence
    solve(s)