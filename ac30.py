maxlen = 9
minlen = 5

id = ""
length = 0

id = input ("enter an id: " )
length = len(id)

if (length < minlen):
    while (length < minlen):
        id = " - " +  id
        length = len(id)

elif ( length >maxlen):
    id = id [0: maxlen]

    print ( " the id is " + id)
    
