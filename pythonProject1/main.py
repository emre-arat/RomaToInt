

roma_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
sum_number = int()
userinput = input("Enter roma numbers: ")
char_list = []
for x in userinput:
    char_list.append(x)
for c in char_list:
    if c not in roma_dict.keys():
        print("False data")
        exit()


def sum_func(liste):
    toplam = 0
    for y in range(0,len(liste)):
        if y +1 < len(liste) and roma_dict[liste[y]] < roma_dict[liste[y+1]]:
            toplam -= roma_dict[liste[y]]
        else:
            toplam += roma_dict[liste[y]]
    if toplam > 4999:
        print("Result is > 4999")
    else:
        print(toplam)

#index_control(char_list)
hata = False
def control_func(liste): # 4 karakterli liste alması gerekiyor
    global hata
    count_list = []
    for x in liste:
        if hata == True:
            break
        else:
            if x == "I":
                number = liste.count(x)
                count_list.append(number)
        if 4 in count_list:
            hata = True


def dortlu_list(liste):
    selected_list = []
    for x in range(0, len(liste)+1):
        selected_list.append(liste[0+x:5+x])
    return selected_list # 4 lü liste döndürür

selected_list = dortlu_list(char_list)

for l in selected_list:
    if hata == False:
        control_func(l)
        selected_list.remove(l)
    else:
        break

if hata == False:
    sum_func(char_list)
else:
    print("False data")

