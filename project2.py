indoor_points = 0
outdoor_points = 0
social_points = 0
print ()
answer1 = input("Do you prefer A sports, B video games, or C talking to friends? ")
if answer1 == "A":
    outdoor_points += 1
elif answer1 == "B":
    indoor_points += 1
elif answer1 == "C":
    social_points += 1
print ()
answer2 = input("Would you rather A play with a friend online, B hangout with them in person, or C hangout with a large group of friends?" )
if answer2 == "A":
    indoor_points += 1
elif answer2 == "B":
    outdoor_points += 1
elif answer2 == "C":
    social_points += 1
print ()
answer3 = input("Would you rather A go to the beach with a friend, B go to the movie theatre with a friend, or C go to a big party?  ")
if answer3 == "A":
    outdoor_points += 1
elif answer3 == "B":
    indoor_points += 1
elif answer3 == "C":
    social_points += 1
print ()
answer4 = input("Would you rather A go on a walk, B watch youtube videos, or C call a friend?  ")
if answer4 == "A":
    outdoor_points += 1
elif answer4 == "B":
    indoor_points += 1
elif answer4 == "C":
    social_points += 1
print ()
answer5 = input("Would you rather A go to a summer camp, B stay at home all summer, or C hangout with lots of friends?  ")
if answer5 == "A":
    outdoor_points += 1
elif answer5 == "B":
    indoor_points += 1
elif answer5 == "C":
    social_points += 1
print ()
if indoor_points > outdoor_points and indoor_points > social_points:
    print("You are an indoor person! You probably like being comfortable!")
elif outdoor_points > indoor_points and outdoor_points > social_points:
    print("You are an outdoor person! You probably enjoy lots of movement and activities!")
elif social_points > indoor_points and social_points > outdoor_points:
    print("You are a social person! You probably enjoy lots of attention and people around you!")