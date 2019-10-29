# Wow! It's 90 degrees Fahrenheit and you are sweating buckets! Luckily you have air conditioning,
# but it's really old and kind of finicky. It cools the room by three degrees and shuts off,
# so you have to keep turning it back on until the temperature gets to where you want it to be.
# Seventy five sounds much more pleasant than 90, so that's what you're shooting for.
#
# While the temperature is greater than 75 degrees Fahrenheit, print 'The temperature is XX — crank the AC!',
# and subtract 3 degrees from the temperature.
#
# Once the temperature is cool enough and the loop is done, print '75. Ahh, that's better.'


temperature = 90

#Check if temperature is greater then 75
while temperature > 75:
    temperature -= 3
    print(f"The temperature is {temperature} - crank the AC!")

print(f"Ahh, that's better. {temperature}")

# OUTPUTThe temperature is 87 - crank the AC!
# The temperature is 84 - crank the AC!
# The temperature is 81 - crank the AC!
# The temperature is 78 - crank the AC!
# The temperature is 75 - crank the AC!
# Ahh, that's better. 75
# I am stuck of th loop ignorning 75. I tried >= 75 which made a small improvment. 
