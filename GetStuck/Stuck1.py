#Function which adds "." between letters
#Example: word => w.o.r.d (last "." isn't added)

def spell():
    word=input("What do you want?")
    print(word[0]+".")
    for i in range(len(word)):
        print(word[i] + ".")
        i = i+1

spell()
    

