nums = [1, 4, 7, 2, 4, 9]
vogais = ['a', 'e', 'i', 'o', 'u']
booleanos = [True, True, False, True, False]
vazio = []

for i in range(len(nums)):
    print(nums[i])

for i, elemento in enumerate(nums):
    print(f"Indice: {i}: {elemento}")

nums.append(10)

print(nums)