file_path_one = input()
file_path_two = input()

with open(file_path_one, "r") as file:
    circle_data = [i.rstrip() for i in file]
    center_x = int(circle_data[0][0])
    center_y = int(circle_data[0][2])
    circle_radius = int(circle_data[1])

with open(file_path_two, "r") as f:
    for line in f:
        dot = line.split()
        dot_x = int(dot[0])
        dot_y = int(dot[1])
        result = (dot_x - center_x)**2 + (dot_y - center_y)**2
        if result < circle_radius ** 2:
            print(1)
        elif result == circle_radius ** 2:
            print(0)
        else:
            print(2)
