# Climate-change-and-impacts-in-Africa

![](climatechangeimage.jpg)

For this project, I analyzed the state of climate change in Africa. This project highlights the growing concern of climate change in Africa and emphasizes the need for regional and international efforts to reduce CO2 emissions and mitigate its impact on temperature and other environmental factors.

***_Project description and dataset information can be seen on the main project page._***

**Project steps:**
1. Data cleaning and validation
2. Used a line plot to show the trend of CO2 levels across the African regions.
3. Conducted a Spearman's correlation to determine the relationship between time (Year) and CO2 levels across the African regions.
4. Conducted an ANOVA test using pingouin.anova() on CO2 by Region, I also conducted a posthoc test (with Bonferroni correction) using pingouin.pairwise_tests() to check if there is a significant difference in the CO2 levels among the African Regions.
5. Determined the most common (top 5) industries in each African region.
6. Determined the industry responsible for the most amount of CO2 (on average) in each African Region.
7. Created an instance of LinearRegression() and used reg.predict() to predict the CO2 levels (at each African region) in the year 2025.
8. Using a linear model I was able to assess the impact of CO2 levels on annual temperature in the selected African countries.

**Findings:**
1. CO2 levels have increased significantly across all African regions since 1970.
2. There is a positive correlation between time and CO2 levels in all regions.
3. Significant differences in CO2 levels exist between some regions, but not all.
4. The "Residential and Other Sectors" and "Main Activity Electricity and Heat Production" industries are major contributors to CO2 emissions in most regions.
5. Predicted CO2 levels are expected to continue rising in all regions by 2025.
6. There is a statistically significant positive relationship between CO2 levels and annual temperature in the selected African countries. A one-unit increase in log10 CO2 is associated with a small but statistically significant increase in temperature.

Dive into the project [here](https://github.com/JachimmaChristian/Climate-change-and-impacts-in-Africa/blob/main/workspace/workspace/notebook.ipynb)
