
# 自动化生成1-10000的key的字典,值是 字母

dictKeys=list(range(1,100))
#print(dictKeys)

dictValue=[]

for keyK in dictKeys: 
    print(keyK)
    valueKey=f"a{keyK}"   
    dictValue.append(valueKey)


#print(dictValue)
##print(len(dictValue)) 

map=dict()

for keyK in dictKeys: 
    map.setdefault(keyK,f"a{keyK}")


print(map)   


map2=zip(dictKeys,dictValue)
print(type(map2))


for item in map2:
 print(item)