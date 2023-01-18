

def number(x):
    while True:
        try:
            text = '{} {} {} '.format("Введіть ",x, '>>>')
            x = int(input(text))
            return x
        except ValueError:
            print("Некоректне введення даних")
 
x = number('x')
y = ''

while x > 0:
    y = str(x % 8) + y
    x = x // 8
print(y)

