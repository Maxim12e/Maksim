year = int(input("Введіть рік: "))

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return print(f"{year} - високосний рік")
    else:
        return print(f"{year} - не високосний рік")



