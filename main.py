#  try catch block

class NegativeError(Exception):
    pass

try:
    n = int(input("enetr numerator:"))
    d = int(input("enetr denomenator:"))
    
    
    if  n < 0 or d < 0:
        raise NegativeError
    
    q = n /d
    
    print(q)
        
except ZeroDivisionError:
    print("numbers can't be zero")
    
except ValueError:
    print("please enetr an integer")

except NegativeError:
    print("No negative number please")
    
except Exception as e:
    print(e)
    print("Something went wrong end it")

else:
    #  runs whenever no error
    print('I am else block')
    
finally:
    #  run regardless
    print("I am finally block")
    
print("end of program")