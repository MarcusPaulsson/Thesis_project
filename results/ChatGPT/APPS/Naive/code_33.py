def count_common_terms(a1, b1, a2, b2, L, R):
    def get_terms(a, b, start, end):
        terms = set()
        k = 0
        while True:
            term = a * k + b
            if term > end:
                break
            if term >= start:
                terms.add(term)
            k += 1
        return terms

    terms1 = get_terms(a1, b1, L, R)
    terms2 = get_terms(a2, b2, L, R)

    common_terms = terms1.intersection(terms2)
    return len(common_terms)

# Read input
a1, b1, a2, b2, L, R = map(int, input().split())
# Calculate and print the result
print(count_common_terms(a1, b1, a2, b2, L, R))