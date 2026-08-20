import sys


def solve(s: str) -> None:
    # Mapping for complement
    complement = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    
    # Reverse the string and compute complement
    reverse_complement = ''.join(complement[base] for base in reversed(s))
    
    print(reverse_complement)


if __name__ == "__main__":
    s = sys.stdin.readline().strip()  # The DNA sequence to reverse-complement
    solve(s)