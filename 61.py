theprice =23.567
myname="frankie"
score =10876
layout=""


layout ="the score is []"
print (layout.format(score))

layout = "my name is [] and my score is[]"
print(layout.format(myname, score))

layout = "all data [2], [1], [0]"
print (layout.format (theprice, myname, score))
