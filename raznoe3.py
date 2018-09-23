# for j in "Hi! I'm mister Robert":
# 	if j == "\":
# 	  print ("Найдено")
# 	  break
# else:
# 	print ("Готово")

# print("Hi! I\'m mister Robert")

inp_list=map(int, input().split())
print(type(inp_list))


new_list=map(bin,list(inp_list))
print(list(new_list))