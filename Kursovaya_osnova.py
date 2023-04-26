from datetime import datetime

class NumberConverter:
    
    def __init__(self):
        self.current_datetime = datetime.now()
        

    def input_number(self):
        while True:
            try:
                self.x = int(input("Введіть x >>> "))
                self.n = int(input("Введіть n >>> "))
                return self
            except ValueError:
                print("Please reinsert")

    def eight_to_ten(self):
        y = ''
        a = self.x
        while self.x > 0:
            y = str(self.x % 8) + y
            self.x = self.x // 8
        file = open('OneFile.txt', 'a+', encoding='utf-8')
        file.write(str(self.current_datetime) + '  ' + str(a) + ' = ' + str(y) + '\n' )
        file.close()
        print('Переклад з 10 системи в 8-ну >>> ' + y)

    def ten_to_eight(self):
        pow = 1
        otv = 0
        a = self.x
        for i in str(self.x)[::-1]:
            otv += int(i) * pow
            pow *= 8
            b = str(otv)
        file = open('OneFile.txt', 'a+', encoding='utf-8')
        file.write(str(self.current_datetime) + '  ' + str(a) + ' = ' + str(otv) + '\n' )
        file.close()
        print('Переклад з 8 системи в 10-ну >>> ' + str(otv))  
    
    def main(self):
        if self.n == 8 :
            self.eight_to_ten()
            print('Дякую що скористувались переводом чисел') 
        elif self.n == 10 :
            self.ten_to_eight()
            print('Дякую що скористувались переводом чисел') 
        else : 
            print('Переклад тільки у вісімкову та десяткову системи')

converter = NumberConverter()
converter.input_number().main()