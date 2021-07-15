from math import pi

remainder = 4
convert_sigma_value = 10
convert_force_value = 9806.65
possible_value = [round(2 + .1 * i, 1) for i in range(0, 11)]

force = 201.72 * convert_force_value
amount_lug = 2
sigma = 170 * convert_sigma_value  # [(Н)/(мм^2)]
tau = 0.6 * sigma
mu = [1, 1.1, 1.2, 1.3]
val = 1
sep = ","

data_file = open('data.csv', 'w')


def bolt_section():
    """
    Площадь сечения болта

    Returns: площадь сечения болта
    """
    return force / (tau * amount_lug)


def bolt_diameter():
    """
    Диаметр болта

    Returns: диаметр болта
    """
    return ((4 * force) / (pi * amount_lug * tau)) ** .5


def a(value):
    """
    Толщина проушины

    Returns: толщина проушины
    """
    return force / (bolt_diameter() * value * sigma)


def b(value):
    return value * bolt_diameter()


def x(value):
    return (b(value) - bolt_diameter()) / 2


def k(value):
    # return force / (2 * a() * x(value) * sigma)
    return 0.565 + 0.48 * (y(value) / x(value)) - 0.1 * value


def y(value):
    return x(value) * (0.208 * value - 1.177) + force / (0.96 * a(mu[val]) * sigma)


print("P", "m", "sigma", "tau", "F", "d", "mu", "a", "b/d", "x", "k", "y", sep=sep, file=data_file)

h = 1
for i in possible_value:
    if k(i) >= 1:
        print(*(("Error: k>1",) * 12), sep=sep, file=data_file)
        h += 1

    else:
        print(round(force, remainder), round(amount_lug, remainder),
              round(sigma, remainder), round(tau, remainder), round(bolt_section(), remainder),
              round(bolt_diameter(), remainder), round(mu[val], remainder), round(a(mu[val]), remainder),
              round(i, remainder), round(x(i), remainder), k(i), round(y(i), remainder),
              sep=sep, file=data_file)
        h += 1

data_file.close()
