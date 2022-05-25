input = "aish"
input = input.lower()
output = []
for character in input:
    number = ord(character) - 96
    output.append(number)
for i in range(50):
    if len(output) < 50:
        output.append(0)

print(output)