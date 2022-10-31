# isdigit   string
# isalnumin   str yoki nit ligini tekshiradi

# yosh = '18'
# print(yosh.isdigit())



# a = input("Yoshingiz nechida? ")
# if a.isdigit():
#     a = float(yosh)
# else:
#     print("Matnli raqam. ")



# from random import randint

# a = randint(1, 500)
# b = randint(1, 500)

# c = int(input('{} + {} = '.format(a, b)))

# if c == (a + b):
#     print("To'g'ri :)")
# else:
#     print("Xato :(")


import math
from random import randint
print("Matematikada o'zingizni sinab ko'ring!")
print("Hohlagan amalingizni tanlang: ")
masalalar = ["Ko'paytirish", "bo'lish", "ayirish", "qo'shish", "daraja"]
son = 1
for a in masalalar:
    print(son, "-", a, end= ("\n"))
    son += 1
amal = input("Tanlagan amalingizni raqamini yozing: ")
if amal.lower() == "1":
    q = 0
    for n in range(1, 6):
          a = randint(1, 20)
          b = randint(1, 20)
          c = int(input("{} x {} = ".format(a, b)))
          if c == float(a * b):
              print("To'g'ri :)")
              q = q + 1
          else:
              print("Xato :(")
    foiz = 20 * q
    print(f"Siz {foiz}% ishladingiz.")
elif amal.lower() == "2":
    q = 0
    for n in range(1, 6):
        a = randint(100, 1000)
        b = randint(1, 20)
        c = int(input("{} : {} = ".format(a, b)))
        if c == float(math.ceil(a / b)):
            print("To'g'ri :)")
            q = q + 1
        else:
              print("Xato :(")
    foiz = 20 * q
    print(f"Siz {foiz}% ishladingiz.")
elif amal.lower() == "3":
    q = 0
    for n in range(1, 6):
        a = randint(1, 100)
        b = randint(1, 100)
        c = int(input("{} - {} = ".format(a, b)))
        if c == float(a - b):
            print("To'g'ri :)")
            q = q + 1
        else:
            print("Xato :(")
    foiz = 20 * q
    print(f"Siz {foiz}% ishladingiz.")
elif amal.lower() == "4":
    q = 0
    for n in range(1, 6):
        a = randint(1, 100)
        b = randint(1, 100)
        c = int(input("{} + {} = ".format(a, b)))
        if c == float(a + b):
            print("To'g'ri :)")
            q = q + 1
        else:
            print("Xato :(")
    foiz = 20 * q
    print(f"Siz {foiz}% ishladingiz.")
elif amal.lower() == "5":
    q = 0
    for n in range(1, 6):
        a = randint(1, 10)
        b = randint(1, 5)
        c = int(input("{} soni {} darajada = ".format(a, b)))
        if c == float(a ** b):
            print("To'g'ri :)")
            q = q + 1
        else:
            print("Xato :(")
    foiz = 20 * q
    print(f"Siz {foiz}% ishladingiz.")
else:
    print("Siz noto'g'ri tanladingiz! ")
     

















































