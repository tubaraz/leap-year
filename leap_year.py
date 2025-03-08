def is_leap_year(year):

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Kullanıcıdan yıl al
try:
    year = int(input("Lutfen bir yil girin: "))
    if is_leap_year(year):
        print(f"{year} bir artık yildır.")
    else:
        print(f"{year} bir artık yil değildir.")
except ValueError:
    print("Lütfen geçerli bir yil girin!")
