import sys
import math


def solve(values: list, n: int) -> None:
    values = [float(x) for x in values]

    # Mean
    mean = sum(values) / n

    # Sample standard deviation
    variance = sum((x - mean) ** 2 for x in values) / (n - 1) if n > 1 else 0

    sd = math.sqrt(variance)

    print(f"{mean:.4f} {sd:.4f}")


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    values = [sys.stdin.readline().strip() for _ in range(n)]

    solve(values, n)