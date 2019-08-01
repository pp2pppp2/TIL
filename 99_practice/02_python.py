def calc(equation):
    temp = '0'
    result = 0
    a = 1
    for eq in equation:
        if eq == '+':
            a,temp,result = save(a,temp,result)
            a = 1
        elif eq == '-':
            a,temp,result = save(a,temp,result)
            a = 0
        else:
            temp += eq
    a,temp,result = save(a,temp,result)
    return result
def save(a,temp,result):
    if a:
        result += int(temp)
        temp=''
    if not a:
        result -= int(temp)
        temp=''
    return a,temp,result

print(calc('123+2-124'))
print(calc('-12+12-7979+9191')) 
print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))

def calc2(equation):
    tem = ''
    result = 0
    for i in equation[::-1]:
        if i == '-':
            result -= int(tem[::-1])
            tem = ''
        elif i == '+':
            result += int(tem[::-1])
            tem = ''
        else:
            tem += i
    if tem:
        result += int(tem[::-1])
    return result

print(calc2('123+2-124'))
print(calc2('-12+12-7979+9191')) 
print(calc2('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))

def calc3(equation):
    equation = equation.replace('+', '.+')
    equation = equation.replace('-', '.-')
    equation = equation.split('.')

    print(equation)

print(calc3('123+2-124'))
print(calc3('-12+12-7979+9191')) 
print(calc3('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))
