def do_twice(f,a):
    f(a)
    f(a)

def print_twice(a):
    print(a)
    print(a)




#def do_four(do_twice,a):
#    do_twice(f,a)
#    do_twice(f,a)

do_twice(print_twice,"Spam")   
#do_four(do_twice,"Spam")

