print('hello world')
print("hello world")

# 注释
print(120)

#
print(1/2)
print("1/2")

#
fp = open('D:/test.txt', 'a+')
# +a 无文件创建，在文件中追加内容
#
print('helloworld', file=fp)
fp.close()
