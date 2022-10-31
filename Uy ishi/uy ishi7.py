p = {
      'intiger': "Bututn sonlar",
      'float': "O'nlik sonlar",
      'boolean': 'Mantiqiy qiymat',
      'for': 'Biror amalni qayta-qayta bajarish tsikli',
      'if': 'Shartlarni tekshirish operatori',
      'string': 'Matnlar',
      'input': 'Foydalanuvchidan ma\'lumot qabul qilish',
      'print': 'Consolga yozilgan narsani chiqarish',
      'list': 'listga aylantirish',
      'del': 'O\'chirish'
          }

for key, value in sorted(p.items()):
    print(f"{key.title()} - {value.title()}.")



d = {
      "O'zbekiston": "toshkent",
    'aqsh': "washington",
    'rossiya': 'moskva',
    'tojikiston': 'dushanbe',
    'qirg\'iziston': 'bishkek',
    'qozog\'iston': "nursulton",
    'malayziya': "kuala-lumpur",
    'singapur': 'singapur',
    'italiya': 'rim',
      }
# for key, value in sorted(d.items()):
#     print(f"{key.title()} - {value.title()}.")
c = input("Qaysi davlatning poytaxtini bilishni istaysiz:\n>>>  ").lower()
p = d.get(c)
if p == None:
    print("Kechirasiz, bizda bu haqida ma'lumot yo'q.")
else:
    print(f"{c.title()}ning poytaxti {p.title()}.")







menu = {
      'osh': 20000,
      'lag\'mon': 22000,
      'non': 3000,
      'choy': 5000,
      'shashlik': 12000,
      'somsa': 6000,
      'tabaka': 15000,
      'sho\'va': 8000,
      'qozon kabob': 80000,
      'mastava': 8000
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





















