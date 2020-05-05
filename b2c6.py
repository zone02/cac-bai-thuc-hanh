class hinhchunhat(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def dien_tich(self):
        return self.a*self.b
a=int(input("nhap vao cd:"))
b=int(input("nhap vao cr:"))
c=hinhchunhat(a,b)
print("dien tich hinh chu nhat la",c.dien_tich())
