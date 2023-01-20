
import datetime

current_time = datetime.datetime.now().timestamp()
last_fed = 15
temperature = 85
humidity = 75
is_raining = False
bring_water_and_snacks = False

if (temperature > 85 and humidity > 75) or is_raining:
    if (last_fed + 4*60*60 < current_time) and not owner_specified:
        bring_water_and_snacks = True

if bring_water_and_snacks:
    print("Bring water and snacks for the dogs during the walk.")
else:
    print("No need to bring water and snacks for the dogs.")
