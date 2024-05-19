def make_car(manufacturer, model, **car_info):
    """Prints information about cars"""
    car_info['brand'] = manufacturer
    car_info['model_name'] = model

    return car_info


car = make_car('suzuki', 'breeza', colour='white', air_bags=4, tow_package=True)
print(car)