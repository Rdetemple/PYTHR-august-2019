
romantic_movie1 = ('The Princess Bride', 1987, 98, 'The story of a man and a woman who lived happily ever after.', ['Buttercup', 'Westley', 'Fezzik', 'Inigo Montoya', 'Vizzini'])
romantic_movie2 = ('Groundhog Day', 1993, 101, "He's having the day of his life… over and over again.", ['Phil Connors'])
romantic_movie3 = ('Amélie', 2001, 122, 'One person can change your life forever.', ['Amélie Poulain', 'Nino Quincampoix', 'The Garden Gnome'])


# Here are my favorite romance movies:

print(romantic_movie1[0:4])
# -  This did not output as expected :(
print(romantic_movie1[0],(romantic_movie1[3]))
# this is closer but not exact

# The Princess Bride ( 1987 ): The story of a man and a woman who lived happily ever after.
print(romantic_movie1[0],'(', romantic_movie1[1],')', ':', romantic_movie1[3])

# Groundhog Day ( 1993 ): He's having the day of his life...over and over again.
print(romantic_movie2[0],'(', romantic_movie2[1],')', ':', romantic_movie2[3])

# Amélie ( 2001 ): One person can change your life forever.

print(romantic_movie3[0],'(', romantic_movie3[1],')', ':', romantic_movie3[3])
