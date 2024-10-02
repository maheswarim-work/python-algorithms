def lovefunc( flower1, flower2 ):
    # ...
    if (flower1 % 2 == 0 and flower2 % 2 !=0) | (flower1 % 2 != 0 and flower2 % 2 ==0):
        return True
    else:
        return False

flower1 = 6
flower2 = 5
print(lovefunc( flower1, flower2 ))
