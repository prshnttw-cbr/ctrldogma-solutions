import sys


def solve(s: str) -> None:
    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    reverse_complement = "".join(complement[base] for base in reversed(s))

    if s == reverse_complement:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    solve(s)