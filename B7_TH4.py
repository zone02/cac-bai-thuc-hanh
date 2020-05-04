s=input(' Nhap chuoi: ')
chuoi_moi = ''.join(i for i in s if not i.isdigit())
print('Chuoi moi se la: ',chuoi_moi)
