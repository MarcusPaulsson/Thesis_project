def count_common_terms(a1, b1, a2, b2, L, R):
    def find_terms(a, b, limit):
        terms = set()
        k = 0
        while True:
            term = a * k + b
            if term > limit:
                break
            terms.add(term)
            k += 1
        return terms

    terms1 = find_terms(a1, b1, R)
    terms2 = find_terms(a2, b2, R)

    common_terms = terms1.intersection(terms2)
    count = sum(1 for x in common_terms if L <= x <= R)
    
    return count

# Input reading
a1, b1, a2, b2, L, R = map(int, input().split())
result = count_common_terms(a1, b1, a2, b2, L, R)
print(result)