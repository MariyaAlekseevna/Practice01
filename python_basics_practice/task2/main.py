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
print(l_1)
l_2 = c.get_l_2(hhh, xxx, d_2)
print(l_2)
time = c.get_time(l_1, nnn, l_2, v_sand)
print("Если спасатель начнет движение под углом theta1, равным ", round(theta1),
      " градусам, он достигнет утопающего через ", round(time, 1), " секунды")
print(c.get_l_1(c.get_xxx(39.413, 8), 8.0))
print(c.get_l_2(50, c.get_xxx(39.413, 8), 10.0))
print(c.get_time(c.get_l_1(c.get_xxx(8, 39.413), 8.0), 2, c.get_l_2(50, c.get_xxx(8, 39.413), 10.0), 5))


class testCase(unittest.TestCase):
    def test_get_l_1(self):
        xxx=c.get_xxx(39.413, 8)
        result = c.get_l_1(xxx, 8.0)
        self.assertEqual(round(result, 2), 31.06)

    def test_get_l_2(self):
        result = c.get_l_2(50, c.get_xxx(39.413, 8), 10.0)
        self.assertEqual(round(result, 2), 130.66)

    def test_get_time(self):
        result = c.get_time(c.get_l_1(c.get_xxx(39.413, 8), 8.0), 2, c.get_l_2(50, c.get_xxx(39.413, 8), 10.0), 5)
        self.assertEqual(round(result, 1), 39.9)
