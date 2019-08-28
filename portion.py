'''
This code calculates how many tons of food each person in a group should take based on how many total tons of food the group has and how many people are in the group. 
Then, it prompts the user with how much food they took. It will output "Good job, you took the right amount of food!" if you took the right amount, and "You took the wrong amount of food" if you took the wrong amount.
Fixed by Ben
'''

# Amount of food and number of people
tons_of_food = 0.07
num_people = 25

# Determine how much food each person gets
tons_of_food_per_person = tons_of_food / num_people
print tons_of_food_per_person

# Ask the user how much food they took
tons_taken = float(input("How many tons of food did you take? "))
if round(tons_taken, 5) == round(tons_of_food_per_person, 5):
    print "Good job, you took the right amount of food!"
else:
    print "You took the wrong amount of food!"
