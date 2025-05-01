
# 涉及列表定义
list1=[1,2,3]
list2=[1,2,3,"mengxp"]
list3=[1,2,3,4,["mengxp","songqian"]]
list4=list("mexp")

print(list1)
print(list2)
print(type(list2))
print(list3)
print(list4)


# 列表增删改查
list3.append("mengzs")
print(list3)

list3.insert(0,"start")
print(list3)

index1=list3.index("start")
print(index1)

list3.extend(list("red"))
print(f"====={list3}")

list3.remove("mengzs")
print(list3)

print(list3.pop(-1))

list3.clear

#del list3[4][1]
#print(list3)

#var2=list3[4][1]
#print(var2)

# 列表常见函数

newList=sorted(["b","a","c"])

print(newList)

## 注意调用函数的时候记得加上()
newList.reverse()

print(newList)