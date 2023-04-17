import calculation as c
import unittest

d_1 = float(input(" Введите кратчайшее расстояние от спасателя до кромки воды, d1 (ярды) => "))
d_2 = float(input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы) => "))
hhh = float(input("Боковое смещение между спасателем и утопающим, h (ярды) => "))
v_sand = float(input("Скорость движения спасателя по песку, Vsand (мили в час) => "))
nnn = float(input("Введите коэффициент замедление спасателя при движении в воде, n => "))
theta1 = float(input("Введите направление движения спасателя по песку, Θ1 (градусы) => "))

xxx = c.get_xxx(theta1, d_1)
l_1 = c.get_l_1(xxx, d_1)
l_2 = c.get_l_2(hhh, xxx, d_2)
time = c.get_time(l_1, nnn, l_2, v_sand)
print("Если спасатель начнет движение под углом theta1, равным ", round(theta1),
      " градусам, он достигнет утопающего через ", round(time, 1), " секунды")

optimal_theta1 = c.get_optimal_theta1(d_1, d_2, hhh, v_sand, nnn)
print("Оптимальное значение угла, под которым необходимо начать движение спасателю = ", optimal_theta1)
