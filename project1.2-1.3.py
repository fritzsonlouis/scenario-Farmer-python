
# Step 1: Check if it's cloudy
is_cloudy = True

# Step 2: Check if it's raining
is_raining = True

# Step 3: Get current moisture level
moisture = 35

# Step 4: Get current temperature
temperature = 85

# Step 5: Check if it's cloudy and raining
if is_cloudy and is_raining:
    # Step 6: Do not turn on the sprinklers
    print("It's cloudy and raining, do not turn on the sprinklers.")

# Step 7: Check if it's not raining and moisture is less than 40 or temperature is higher than 90
elif not is_raining and (moisture < 40 or temperature > 90):
    # Step 8: Turn on the sprinklers
    print("Turn on the sprinklers, its not raining and the moisture is less than 40 or temperature is higher than 90.")

else:
    # Step 9: Print message that the crops are doing good and healthy
    print("The crops are doing good and healthy.")
