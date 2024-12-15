tuple = ('p', 'u', 's', 'h', 'p', 'a')
str = ''.join(tuple)
print(str)

#4th element from starting
item1=tuple[3]
print(item1)

#4th element from end
item2=tuple[-4]
print(item2)

index=tuple.index("p",2)
print(f"Index:{index}")

print(f"Length: {len(tuple)}")
