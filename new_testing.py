# def water_state(temperature):
#     if temperature <= 0:
#         return "Solid"
#     elif temperature > 0 & temperature < 100:
#         return "Liquid"
#     else:
#         return "Gas"
#


# def calculate_time(h,g=9.80665):
#     t = (2 * h / g) ** 0.5
#     return t
#
#
# time = calculate_time(h=100)
# print(time)
#
# # def get_nr_items(name):
#     count = name.split(",")
#     print(count)
#     return len(count)


# print(get_nr_items('john, lisa, teresa'))
# def convert(feet, inches):
#     meters = feet * 0.3048 + inches * 0.0254
#     return f"{feet} ft and {inches} inches is equal to approximately {round(meters)} meters"
#
#
# def user_input():
#     feet_inches = input("Enter feet and inches: ")
#     part = feet_inches.split(" ")
#     foot = int(part[0])  # Convert to integer
#     inch = int(part[1])  # Convert to integer
#     return foot, inch
#
#
# feet, inches = user_input()
#
# answer = convert(feet=feet, inches=inches)
#
# print(answer)
