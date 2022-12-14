import numpy as np

triangles = []
with open('p102_triangles.txt') as f:
    for x in f:
        x = x.rstrip()
        x = x.split(",")
        read_triangle = [(int(x[0]), int(x[1])), (int(x[2]), int(x[3])), (int(x[4]), int(5))]
        triangles.append(read_triangle)


# def calculate_equation(point_1: tuple, point_2: tuple) -> tuple:
#     if point_1[0] != point_2[0]:
#         m = (point_2[1] - point_1[1]) / (point_2[0] - point_1[0])
#     else:
#         m = (point_2[1] - point_1[1]) * float('inf')
#     c = point_1[1] - m * point_1[0]
#     return (m, c)
#
#
# def crosses_origin(m: float, c: float) -> tuple:
#     if m != 0:
#         x_coordinate = -c / m
#     else:
#         x_coordinate = float('inf')
#     y_coordinate = c
#     return (x_coordinate, y_coordinate)
#
#
# def contains_origin(triangle: list) -> bool:
#     coordinates = {"++": 0, "--": 0}
#     for i in range(len(triangle) - 1):
#         for j in range(i + 1, len(triangle)):
#             m, c = calculate_equation(triangle[i], triangle[j])
#             x_variable, y = crosses_origin(m, c)
#             if x_variable != float('inf'):
#                 if x_variable == 0 and y == 0:
#                     return True
#                 if x_variable < 0 and y < 0:
#                     coordinates["--"] += 1
#                 elif x_variable > 0 and y > 0:
#                     coordinates["++"] += 1
#     for value in coordinates.values():
#         if value == 0:
#             return False
#     return True

def triangle_equation(triangle: list[tuple]) -> bool:
    first_point = np.array([triangle[0][0], triangle[0][1], 0])
    second_point = np.array([triangle[1][0], triangle[1][1], 0])
    third_point = np.array([triangle[2][0], triangle[2][1], 0])
    first_line = second_point - first_point
    second_line = third_point - second_point
    normal = np.cross(first_line,second_line)



count = 0

for triangle in triangles:
    if contains_origin(triangle):
        count+=1
print(count)