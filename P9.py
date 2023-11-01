# Input
N = int(input())
country_stamps = set()

# Collect distinct country stamps
for _ in range(N):
    country_name = input()
    country_stamps.add(country_name)

# Output
print(len(country_stamps))
