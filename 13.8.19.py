tickets_ = int(input("Введите количество билетов: "))
price_ = 0
for i in range(tickets_):
    age = int(input("Введите ваш возраст: "))
    i += 1
    if age < 18:
        print("Бесплатно!")
    elif 18 <= age <= 25:
        price_ += 990
        print('Стоимость билета 990 рублей')
    else:
        price_ += 1390
        print("Стоимость билета 1390 рублей")
if tickets_ > 3:
    price_ = price_*0.9
    print("Стоимость билетов со скидкой: ", price_)
else:
    print("Сумма к оплате", price_)
