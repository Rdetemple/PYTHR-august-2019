def race_results(person_nu):
    print(f'How far did person {person_nu} run (in feet)?')
    distance = float(input())
    print(f'How many minutes did person {person_nu} run take to run {distance} feet?')
    mins = float(input())
    return distance/(mins * 60)
# race_results = return distance/(mins * 60)
speed1 = race_results(1)
speed2 = race_results(2)
speed3 = race_results(3)
# print('How far did person 2 run (in feet)?')
# distance2 = float(input())
# print(f'How many minutes did person 2 run take to run {distance2} feet?')
# mins2 = float(input())
#
# print('How far did person 3 run (in feet)?')
# distance3 = float(input())
# print(f'How many minutes did person 3 run take to run {distance3} feet?')
# mins3 = float(input())

# secs2 = mins2 * 60
# speed2 = distance2/secs2
#
# secs3 = mins3 * 60
# speed3 = distance3/secs3
#
# Award Ceremonies
if speed3 > speed2 and speed3 > speed1:
    print(f'Person 3 was the fastest at {speed3} f/s')
elif speed2 > speed3 and speed2 > speed1:
    print(f'Person 2 was the fastest at {speed2} f/s')
elif speed1 > speed3 and speed1 > speed2:
    print(f'Person 1 was the fastest at {speed1} f/s')
elif speed1 == speed2 and speed2 == speed3:
    print(f'Everyone tied at {speed1} m/s')

print('Well done everyone!')
