# nums = [3, 11, 6, 32, 15, 22, 4, 10, 5]

# m = []

# teste = 0

# for i in range(len(nums)):
#     linha = []
#     for j in range(3):
#         nums.sort()
#         linha.append(nums[i])
#         nums.pop()
#     m.append(linha)

nums = [3, 11, 6, 32, 15, 22, 4, 10, 5]
linha1 = []
linha3 = []

matriz = []

for _ in range(3):
    linha1.append(nums.pop(nums.index(max(nums))))
    linha1.sort()
for _ in range(3):
    linha3.append(nums.pop(nums.index(min(nums))))
    linha3.sort()
nums.sort()
matriz.append(linha1)
matriz.append(nums)
matriz.append(linha3)
print(matriz)
