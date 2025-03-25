num1= float(input("Informe o primeiro número: "))
num2= float(input("Informe o segundo número: "))

oper=(input("Informe a operação: "))

if oper == '+':
    print(num1+num2)
elif oper == '-':
    print(num1-num2)
elif oper == '*':
    print(num1*num2)
elif oper == '/':
    print(num1/num2)
else:
    print("Erro")