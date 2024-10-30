from circle_radius import radius_circumscribed_square, radius_inscribed_square

side_length = float(input("Введіть довжину сторони квадрата: "))

radius_circumscribed = radius_circumscribed_square(side_length)
print(f"Радіус кола, описаного навколо квадрата: {radius_circumscribed:.2f}")

radius_inscribed = radius_inscribed_square(side_length)
print(f"Радіус кола, вписаного в квадрат: {radius_inscribed:.2f}")