# m = {
#       'olma': 10000,
#       'anor': 20000,
#       'uzum': 40000,
#       'un': 14000,
#       'sut': 7000,
#       'pomidor': 12000,
#       'bodring': 12000,
#       }

# print("Do'konimizdagi mahsulotlar: ")
# for j in sorted(m):
#     print(j.title())

# tel = {
#         'ali': 'iphone X',
#         'vali': 'galaxy s9',
#         'olim': 'mi 10 pro',
#         'orif': 'nokia 3310'
#         } 

# print(tel.values())
# print("Foydalanuvchilar qaytdagi telefonlarni ishlatishadi:  ")
# for w in tel.values():
#     print(w)




# tellar = {
#     'ali': 'iphone X',
#     'vali': 'galaxy s9',
#     'olim': 'mi 10 pro',
#     'orif': 'nokia 3310',
#     'aziz': 'hawei p30',
#     'sobir': 'iphone x',
#     'salim': 'iphone x',
#     'asil': 'mi 10 pro'
#       }

# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:  ')
# for e in set(tellar.values()):
#     print(e)



# p = {
#       'intiger': "Bututn sonlar",
#       'float': "O'nlik sonlar",
#       'boolean': 'Mantiqiy qiymat',
#       'for': 'Biror amalni qayta-qayta bajarish tsikli',
#       'if': 'Shartlarni tekshirish operatori'
     
#           }

# for key, value in sorted(p.items()):
#     print(f"{key.title()} - {value.title()}.")







# d = {
#      "O'zbekiston": "toshkent",
#     'aqsh': "washington",
#     'rossiya': 'moskva',
#     'tojikiston': 'dushanbe',
#     'qirg\'iziston': 'bishkek',
#     'qozog\'iston': "nursulton",
#     'malayziya': "kuala-lumpur",
#     'singapur': 'singapur',
#     'italiya': 'rim',
#      }

# c = input("Qaysi davlatning poytaxtini bilishni istaysiz:\n>>>  ").lower()
# p = d.get(c)
# if p == None:
#     print("Kechirasiz, bizda bu haqida ma'lumot yo'q.")
# else:
#     print(f"{c.title()}ning poytaxti {p.title()}.")




menu = {
     'osh': 20000,
     'lag\'mon': 22000,
     'non': 3000,
     'choy': 5000,
     'shashlik': 12000,
     'somsa': 6000,
     'tabaka': 15000
     }

narh = 0
print('3ta taom buyurtma bering:  ')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:  ").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm.")
        narh = narh + menu[buyurtma]
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")
print(f"Jami {narh} so'm")













