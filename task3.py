# numbers = (1,2,3,4,5,6,7,8,9)
# count = 0
# count_tek = 0
# for i in numbers:
#     if i % 2 == 0 :
#        count = count+1
#     else:
#         count_tek = count_tek+1
# print(f'cut ededlerin sayi:{count}')
# print(f'tek ededlerin sayi:{count_tek}')

# text = input("metni daxil edin!!")
# for i in text:
#     if i.isdigit():
#         print("eded var")
#         break
 
# day =  input("tarixi daxil edin")
# ay = input("ayi daxil edin:  ")
# fesil= {"qish":["yanvar","fevral","decabr"],
#         "yaz":["mart","aprel"],
#         "yay":["may","iyun","iyul"],
#         "payiz":["avqust","sentyabr","oktyabr"]}
# for m in ay:
#     for i in fesil.keys():
#      print(i)
#     # for j in fesil[i]:
#         # print(j)
#     if m == fesil[i]:
#         print(i)
        


datas = {
    "winter": ["January", "December", "February"],
    "spring": ["March", "April", "May"],
    "summer": ["June", "July", "August"],
    "autumn": ["Octember", "November", "September"]
}

month = input("Enter the month: ")  # December


found_season = None

for season, months in datas.items():
    if month.capitalize() in months:
        found_season = season
        break

print(found_season)