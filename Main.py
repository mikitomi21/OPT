tab = [1,2,3,3,4,5,6,7,9,2,42,443,56,87,4,2]

map1 = map(lambda x:x*2, tab)
print(list(map1))

fil = filter(lambda x:x%3==0, tab)
print(list(fil))