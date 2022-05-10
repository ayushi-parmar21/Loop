# Lst = [50, 70, 30, 20, 90, 10, 50]
# print(Lst[1:4])

# Lst = [50, 70, 30, 20, 90, 10, 50]
# print(Lst[-7::1])

# Lst = [50, 70, 30, 20, 90, 10, 50]
# print(Lst[1:5])



# List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print("\nOriginal List:\n", List)
# print("\nSliced Lists: ")
# print(List[3:9:2])
# print(List[::2])
# print(List[::])


# List = ['Geeks', 4, 'geeks !']
# print("\nOriginal List:\n", List)

# print("\nSliced Lists: ")
# print(List[::-1])
# print(List[::-3])
# print(List[:1:-2])



# List = [-999, 'G4G', 1706256, '^_^', 3.1496]
# print("\nOriginal List:\n", List)
# print("\nSliced Lists: ")
# print(List[10::2])
# print(List[1:1:1])
# print(List[-1:-1:-1])
# print(List[:0:])



List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\nOriginal List:\n", List)
print("\nSliced Lists: ")
newList = List[:3]+List[7:]
print(newList)
List = List[::2]+List[1::2]
print(List)
