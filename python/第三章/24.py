import pprint

with open("/Users/mengxp/Desktop/newStart/code/pythonAndGo/python/第三章/24.txt") as f:
    file_data=f.readlines()
    print(type(file_data))
    pprint.pprint(file_data)
    print(len(file_data))

print(len(file_data))
print(file_data.count("\n"))
print(str(file_data).split(" ").count("I"))
print(str(file_data).split(" ").count("You"))
print(str(file_data).split(" ").count("you"))




