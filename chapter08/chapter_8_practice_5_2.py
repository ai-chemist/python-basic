def make_car(brand, wheel, **kwargs):
    kwargs['brand'] = brand
    kwargs['wheel'] = wheel
    return kwargs

car_0 = make_car('subaru', 'outback', color='blue', tow_package=False)
car_1 = make_car('porsche', 'no wheel', size='400*200')
car_2 = make_car('honda', '4')

car_list = [car_0, car_1, car_2]
for car in car_list:
    print(car)