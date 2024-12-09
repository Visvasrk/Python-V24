#here is an example of try expect block in python.
#the try block tries the given statement
#if exception arises, the expect block tells what to do.else,the part continues.
print('Press q to quit any time')
while True:
    divident=input('Enter number one the divident : ')
    if divident.lstrip().rstrip().lower() == 'q':
        break
        exit()
    divisor=input('Enter number two the divisor : ')
    if divisor.lstrip().rstrip().lower() == 'q':
        break
        exit()
    try:
        quotient=eval(divident)/eval(divisor)
    except ZeroDivisionError:
        print('Sorry you can not divide a number by zero !')
        print('Answer is indefinite or infinite...')
    else:
        print(quotient)
        
        
          
