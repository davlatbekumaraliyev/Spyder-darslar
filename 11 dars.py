# import math
# a = int(input("a ni kiriting:  "))
# b = int(input("b ni kiriting:  "))
# d = int(input("d ni kiriting:  "))
# c = math.sqrt((a * b) / (math.sqrt(b + (d**2))))
# print(c)


# car = {"model": "ferrari", "rang": "qizil"}
# print(car["model"])
# print(car["rang"])


# talaba = {
#     'ism': 'murod olimov',
#     'yosh': 22,
#     't_yil': 2000
# }

# # print(f"{talaba['ism'].title()},  \
# #       {talaba['t_yil']}-yilda tug'ilgan,  \
# #       {talaba['yosh']} yoshda")


# talaba['kurs'] = 4
# talaba['fakultet'] = 'informatika'
# talaba['ism'] = 'abdulloh'
# print(f"{talaba['ism'].title()},  \
#       {talaba['t_yil']}-yilda tug'igan,  \
#       {talaba['yosh']} yoshda,  \
#       {talaba['fakultet']} fakulteti,  \
#       {talaba['kurs']} kursda.")
      

# talaba = {}
# talaba['ism'] = 'qobil rasulov'
# talaba['kurs'] = 3
# talaba['yosh'] = 20
# print(talaba)
# print(f"Talaba {talaba['ism'].title()}, {talaba['kurs']}-kurs, {talaba['yosh']} yoshda.")



# #QIYMATNI YANGILASH
# talaba['kurs'] = 4
# print(talaba)
# print(f"Talaba {talaba['ism'].title()}, {talaba['kurs']}-kurs, {talaba['yosh']} yoshda.")


# talaba = {'ism': 'murod olimov', 'yosh': 22, 'yil': 2000}
# print(talaba)
# del talaba['yosh']
# print(talaba)



# telefonlar = {
#     'ali': 'iphone X',
#     'vali': 'galaxy s9',
#     'olim': 'mi 10 pro',
#     'orif': 'nokia 3310'
#     } 

# phone = telefonlar['ali']
# print(f"Alining telefoni {phone}")

# phone = telefonlar['vali']
# print(f"Valining telefoni {phone}")


# phone = telefonlar.get('hasan', 'None')
# print(phone)







# s = {}
# a = int(input("a>>>  "))
# b = int(input("b>>>  "))
# s["a"] = a
# s["b"] = b
# print(s)
# print(f"a = {s['a']}")













# talaba = {
#     'ism': 'valijon',
#     'familiya': 'shamshiyev', 
#     'yosh': 22,
#     'fakultet': 'matematika',
#     'kurs': 4
#     }

# # key = input("Kalit so'z kiriting:  ")
# # if key.lower() in talaba:
# #     print(talaba[key])
# # else:
# #     key = input("Bunday kalit so'z mavjud emas iltimos kalit so'z va qiymay kiriting:\nKey>>> ")
# #     value = input('Value>>>  ')
# #     talaba[key] = value
# #     print(f"{key} -- {talaba[key]}")

# # print(talaba.items())



# for kalit, qiymat in talaba.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat}\n")










# telefonlar = {
#     'ali': 'iphone X',
#     'vali': 'galaxy s9',
#     'olim': 'mi 10 pro',
#     'orif': 'nokia 3310'
#     } 

# for key, value in telefonlar.items():
#     print(f"{key.title()}ning telefoni {value}.")





# m = {
#       'olma': 10000,
#       'uzum': 12000,
#       'tuxum': 15000,
#       'anor': 18000,
#       'anjir': 20000
#       }


# print("Do'kondagi mahsulotlar: ")
# for mahsulot in m.keys():
#     print(mahsulot.title())


# b = ['anor', 'uzum', 'non', 'baliq']
# for mahsulot in m:
#     if mahsulot in b:
#         print(f"{mahsulot.title()} {m[mahsulot]} so'm")
        
# for bu in b:
#     if bu not in m:
#         print(f"Iltims, do'konimizga {bu} ham olib keling")



mahsulotlar = {
    'un': 10000,
    'olma': 7000,
    'pomidor': 12000,
    'bodring': 12000,
    'baliq': 45000,
    'tuxum': 1000,
    'banan': 17000,
    'kartoshka': 5000,
    'piyoz': 3000,
    'non': 3000,
    'sut': 5000,
    'ketchup': 7000,
    'qatiq': 6000,
    
    }

print("Assalomu alaykum")

e = int(input("Nechta mahsulot harid qilasiz?\n>>>  "))
q = 1
k = []
narh = 0
for r in range(1, e+1):
    k.append(input(f"{q} - harid qilmoqchi bo'lgan mahsulotingizni kiriting:\n>>>  "))
    q += 1
for a in mahsulotlar:
    if a.lower() in k:
        print(f"{a.capitalize()} {mahsulotlar[a]} so'm")
        if a == 'un':
            narh += 10000
        elif a == 'banan':
            narh += 17000
        elif a == 'olma':
            narh += 7000
        elif a == 'pomidor':
            narh += 12000
        elif a == 'banan':
            narh += 12000
        elif a == 'baliq':
            narh += 45000
        elif a == 'piyoz':
            narh += 3000
        elif a == 'kartoshka':
            narh += 5000
        elif a == 'tuxum':
            narh += 1000
        elif a == 'non':
            narh += 3000
        elif a == 'sut':
            narh += 5000
        elif a == 'ketchup':
            narh += 7000
        elif a == 'qatiq':
            narh += 6000
print(f"Jami {narh} so'm")
for j in k:
    if j not in mahsulotlar:
        print(f"Uzur, bizda xozircha {j} yo'q edi.")
print("Bizdagi mahsulotlar: ")
for a in mahsulotlar.keys():
    print(a.title())
y = input("Yana harid qilishni istaysizmi?(ha|yo'q)\n>>>  ")
narh2 = 0
if y.lower() == 'ha':
    e2 = int(input("Nechta mahsulot harid qilasiz?\n>>>  "))
    q2 = 1
    i = []
    for r in range(1, e2+1):
        i.append(input(f"{q2} - harid qilmoqchi bo'lgan mahsulotingizni kiriting:\n>>>  "))
        q2 += 1
    for z in i:
        if z.lower() in i:
            print(f"{z.capitalize()} {mahsulotlar[z]} so'm")
            if z == 'un':
                narh2 += 10000
            elif z == 'banan':
                narh2 += 17000
            elif z == 'olma':
                narh2 += 7000
            elif z == 'pomidor':
                narh2 += 12000
            elif z == 'banan':
                narh2 += 12000
            elif z == 'baliq':
                narh2 += 45000
            elif z == 'piyoz':
                narh2 += 3000
            elif z == 'kartoshka':
                narh2 += 5000
            elif z == 'tuxum':
                narh2 += 1000
            elif z == 'non':
                narh2 += 3000
            elif z == 'sut':
                narh2 += 5000
            elif z == 'ketchup':
                narh2 += 7000
            elif z == 'qatiq':
                narh2 += 6000
    print(f"Jami {narh2} so'm.")
    print("Haridingiz uchun rahmat!")
elif y.lower() == "yo'q":
    print("Haridingiz uchun rahmat!")
else:
    print("Haridingiz uchun rahmat!")












