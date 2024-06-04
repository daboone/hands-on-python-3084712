NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

print("-" * 50)

for name in NAMES:
    print(name)
print("-" * 50 )
for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")
print("-" * 50 + "\n")
for name in reversed(NAMES):
    print(name)
print("-" * 50 + "\n")
for i in range(5):
    print(i)
print("-" * 50 + "\n")
# enumerate
for i, name in enumerate(NAMES):
    print(f"{i} {name}")