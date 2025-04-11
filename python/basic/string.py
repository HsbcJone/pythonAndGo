content="""
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
"""

var="123456"
print(content[0:5])
print(var[0:-1:2])
print(var[-3::2])

print(content.isalnum())
print(content.isalpha())

var1=content.count("better")
print(f"内容中包含better的个数是 {var1}")