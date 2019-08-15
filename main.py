import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('NCHS_-_Death_rates_and_life_expectancy_at_birth.csv')

# print(dataset)

timeline = dataset.iloc[1:116]

year = timeline['Year']
life_expectancy = timeline['Average Life Expectancy (Years)']

plt.plot(year, life_expectancy)
plt.xlabel("Year")
plt.ylabel("Avg. Life Expectancy")
plt.title("Avg. Life Expectancy in the US from 1900 to 2014")
plt.show()

# print(timeline.tail(5))