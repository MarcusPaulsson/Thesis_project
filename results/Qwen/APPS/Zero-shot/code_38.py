def check_tracks(n, L, Kefa, Sasha):
    Kefa = Kefa + [L + x for x in Kefa]
    Sasha = Sasha + [L + x for x in Sasha]
    for i in range(n):
        if all(Kefa[j] - Kefa[i] == Sasha[j] - Sasha[i] for j in range(n)):
            return "YES"
    return "NO"

n, L = map(int, input().split())
Kefa = list(map(int, input().split()))
Sasha = list(map(int, input().split()))

print(check_tracks(n, L, Kefa, Sasha))