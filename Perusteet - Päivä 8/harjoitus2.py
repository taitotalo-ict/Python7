file = open('harjoitus2.txt')

# content_str = file.read()         # -> str (koko sisältö)
# content = content_str.split('\n')


# file.seek(0)
# content = []
# while row_str := file.readline():     # -> str (1 rivi)
#     content.append(row_str)

file.seek(0)
content = file.readlines()    # -> list(str, str, ...)
file.close()

#print(content)
result = []
for row in content:
    result.append(row[4])
print(''.join(result))

result = []
for index, row in enumerate(content):
    print(index, row)
    result.append(row[index])
print(result)
print(''.join(result))
