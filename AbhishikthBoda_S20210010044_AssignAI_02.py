from typing import List

def encode(arr, s):
    alphabets = set(''.join(arr) + s)
    num_values = {}

    def check(i, var):
        if i == len(alphabets):
            return sum(map(lambda x: int(''.join([str(num_values[c]) for c in x])), arr)) == int(''.join([str(num_values[c]) for c in s]))

        for j in range(10):
            if j not in var:
                num_values[list(alphabets)[i]] = j
                if check(i+1, var.union({j})):
                    return True
                del num_values[list(alphabets)[i]]

        return False
    return check(0, set())

def solve_csp(arr: List[str], S: str) -> bool:
    # Step 1: Extract all unique letters from arr and S
    letters = set()
    for word in arr:
        letters.update(word)
    letters.update(S)
    
    # Remove duplicates from letters
    letters = list(letters)
    letters.sort()
    
    # Check if there are enough unique letters to map to all digits
    if len(letters) < 5:
        return False
    
    # Step 2: Generate all possible mappings from letters to digits
    mappings = []
    for i in range(10):
        for j in range(10):
            if j != i:
                for k in range(10):
                    if k != i and k != j:
                        for l in range(10):
                            if l != i and l != j and l != k:
                                for m in range(10):
                                    if m != i and m != j and m != k and m != l:
                                        mapping = {letters.pop(0): i,
                                                   letters.pop(0): j,
                                                   letters.pop(0): k,
                                                   letters.pop(0): l,
                                                   letters.pop(0): m}
                                        mappings.append(mapping)
    
    # Step 3: Check if any mapping satisfies the constraint
    for mapping in mappings:
        if sum_digits([encode(word, mapping) for word in arr]) == encode(S, mapping):
            return True
    return False

def sum_digits(numbers: List[int]) -> int:
    # Compute the sum of a list of numbers
    return sum(numbers)

# Example usage:
arr = ["SEND", "MORE"]
s = "MONEY"
print(encode(arr, s)) # Output: True

arr = ["LETS", "CUT", "TO", "THE"]
s = "CHASE"
print(encode(arr, s)) # Output: True
