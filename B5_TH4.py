ds=input(' Danh sách: ').split()
#in cả dãy vừa nhập
print(ds)
# in dãy vừa nhập, mỗi phần tử trên một dòng và đảo ngược lí thuyết
for so in ds.__reversed__():
    print(so)
