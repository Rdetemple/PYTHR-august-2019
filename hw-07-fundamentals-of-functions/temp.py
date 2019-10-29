print('How far did person 1 run (in feet)?')
distance1 = float(input())
print(f'How many minutes did person 1 run take to run {distance1} feet?')
mins1 = float(input())

print('How far did person 2 run (in feet)?')
distance2 = float(input())
print(f'How many minutes did person 2 run take to run {distance2} feet?')
mins2 = float(input())

print('How far did person 3 run (in feet)?')
distance3 = float(input())
print(f'How many minutes did person 3 run take to run {distance3} feet?')
mins3 = float(input())

secs1 = mins1 * 60
speed1 = distance1/secs1

secs2 = mins2 * 60
speed2 = distance2/secs2

secs3 = mins3 * 60
speed3 = distance3/secs3

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
