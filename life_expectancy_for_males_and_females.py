import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('NCHS_-_Death_rates_and_life_expectancy_at_birth.csv')

male_timeline = dataset.iloc[234:348]
female_timeline = dataset.iloc[118:232]

male_year = male_timeline['Year']
male_life_expectancy = male_timeline['Average Life Expectancy (Years)']

female_year = female_timeline['Year']
female_life_expectancy = female_timeline['Average Life Expectancy (Years)']

plt.plot(male_year, male_life_expectancy, color = 'blue', label = "Males")
plt.plot(female_year, female_life_expectancy, color = 'pink', label = "Females")
plt.xlabel("Year")
plt.ylabel("Avg. Life Expectancy")
plt.title("Avg. Life Expectancy for Males and Females in the US (1900 - 2014)")
plt.legend()
plt.show()
