#Scenario: You have a dataset containing temperature readings for different cities over several days. You need to calculate the average temperature for each city.
#Task: Write a Python script using for loops to iterate through the dataset and calculate the average temperature for each city.

temperature_data = {
    "New York": [68, 72, 75, 70, 68],
    "Los Angeles": [82, 85, 88, 79, 81],
    "Chicago": [65, 68, 70, 64, 62]
}
# Dictionary to store the average temperature for each city
average_temperature={}
# Iterate through each city in the dataset
for city, temperatures in temperature_data.items():
    # Calculate the average temperature for the current city
    average = sum(temperatures)/len(temperatures)
    # Store the average temperature in the dictionary
    average_temperature[city] = average

# Print the average temperature for each city
for city, avg_temp in average_temperature.items():
    print(f"The avergae temperature in city {city} is {avg_temp}")
