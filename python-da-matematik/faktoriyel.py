def faktoriyel(n):
  if(n==1):
    return n
  else:
    return n*(faktoriyel(n-1))

sayi = int(input("Faktoriyel Hesabı Yapılacak Sayı : "))

if sayi < 0:
  print("Negagif Sayı girişi yaptınız")
elif sayi == 0:
  print("Faktoriyel : 1")
else:
  print("Faktoriyel : ",faktoriyel(sayi ))
