def is_leap_year(year):
    
    # 4'e tam bölünen yıllar artık yıldır
    #100'e tam bölünenler artık yıl değildir
    #400'e tam bölünen yıllar tekrar artık yıldır.

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Kullanıcıdan yil al
try:
    year = int(input("Lutfen bir yil girin: "))
    if is_leap_year(year):
        print(f"{year} bir artik yildir.")
    else:
        print(f"{year} bir artik yil değildir.")
except ValueError:
    print("Lütfen geçerli bir yil girin!")
