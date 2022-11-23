#- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
coordinate_x= float(input("Введите x:\n"))
coordinate_y= float(input("Введите y:\n"))
if coordinate_x> 0 and coordinate_y > 0:
    print("Первая четверть")
elif coordinate_x< 0 and coordinate_y > 0:
    print("Вторая четверть")
elif coordinate_x< 0 and coordinate_y < 0:
    print("Третья четверть")
elif coordinate_x>0 and coordinate_y<0:
    print("Четвертая четверть")
    