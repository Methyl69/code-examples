print ("printing current and previous noin range of (10)")
previous_num = 0

for i in range (1,11):
    x_sum = previous_num + i
    print("current number", i ,"previous no", previous_num, "sum: ", x_sum)
    previous_num = i
