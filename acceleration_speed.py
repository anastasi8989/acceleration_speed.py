initial_velocity = float(input("Введите начальную скорость (в м/с): "))
acceleration = float(input("Введите ускорение (в м/c^2): "))
time = float(input("Введите время движения (в секундах): "))

final_velocity = initial_velocity + (acceleration * time)

print("Скорость объекта в конечный момент времени:", final_velocity, "м/с")
