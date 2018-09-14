# temp_mass=[]
# count_1=7

# for i in range(count_1):
#     zzz=int(input("Enter number: "))
#     temp_mass.append(zzz)
#     print(temp_mass)

# max = temp_mass[0]
# min = temp_mass[0]

# for i in range(count_1):
#     if temp_mass[i] > max:
#         max = temp_mass[i]
#     if temp_mass[i] < min:
#         min = temp_mass[i]
# print("Maximum number = %d. Mininmum number = %d." %(max, min))

def get_min_max (list):
    if list==[]:
        return False

    result={}

    result['min']=list[0]
    result['max']=list[0]

    for i in range(len(list)):
        if list[i] > result['max']:
            result['max'] = list[i]
        if list[i] < result['min']:
            result['min'] = list[i]
    return result

# list_temp=[-2,23,1,77,0,45,3]
# list_temp=[]
# print(get_min_max(list_temp))
