hrs = input("Введіть кількість робочих годин: ")
rate = input("Введіть ставку на годину: ")

h = float(hrs)
r = float(rate)


if h <= 40:
        z = h * r
else:
       z = (40 * r) + ((h - 40) * r * 1.5)

print(z)
