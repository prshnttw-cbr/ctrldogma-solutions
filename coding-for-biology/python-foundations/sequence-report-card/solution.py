import sys


def solve(identifier: str, seq: str) -> None:
    print(f"ID: {identifier}")
    print(f"Length: {len(seq)}")
    print(f"First base: {seq[0]}")


if __name__ == "__main__":
    identifier = sys.stdin.readline().strip()
    seq = sys.stdin.readline().strip()
    solve(identifier, seq)