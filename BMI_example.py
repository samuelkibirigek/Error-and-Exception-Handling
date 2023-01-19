"""
BODY MASS INDEX CALCULATOR. TRY RUNNING PROGRAM WITH HEIGHT IN EXCESS OF 3meters.
    Here I invite program user to enter a height and weight
    and in the case that they enter a height beyond 3 meters
    which is humanly unrealistic but mathematically acceptable
    we return a value error prompting them to enter a proper
    height rather than working with what is given.
"""

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)