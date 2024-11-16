word =input ("enter word")

print("Originalstring:", word)

size = len(word)

print("printing only even index chars")
for i in range (0, size-1,2):
    print("index[", i , "] ", word[i])
