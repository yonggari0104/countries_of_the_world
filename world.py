import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')



world = pd.read_csv('C:\\Users\\user\\.spyder-py3\\world\\world.csv')

#SEE IF NaN VALUES EXISTS
print(world.isna().any())

print(world.info())
print(world.head())
print(world.dtypes)
print(world.describe())


world["Literacy (%)"] = world["Literacy (%)"].str.replace("," , ".").astype("float64")
world["Net migration"] = world["Net migration"].str.replace("," , ".").astype("float64")
world["Birthrate"] = world["Birthrate"].str.replace("," , ".").astype("float64")
world["Deathrate"] = world["Deathrate"].str.replace("," , ".").astype("float64")
world["Agriculture"] = world["Agriculture"].str.replace("," , ".").astype("float64")
world["Industry"] = world["Industry"].str.replace("," , ".").astype("float64")
world["Service"] = world["Service"].str.replace("," , ".").astype("float64")



world.fillna(0, inplace=True)



#BAR GRAPH OF TOP 30 COUNTRIES WITH HIGHEST POPULATIONS
mostPop30Data = world.sort_values("Population", ascending = False).head(30)

plt.figure(figsize = (10, 5))
sns.barplot(x = mostPop30Data["Country"], y = mostPop30Data["Population"])
plt.xticks(rotation = 90)
plt.title("Top 30 Countries with the Highest Populations")
plt.xlabel("Countries")
plt.ylabel("Population (in billion)")
plt.show()




#SIDE BAR GRAPH OF TOP 30 COUNTRIES WITH LARGEST AREA
largeArea30Data = world.sort_values("Area (sq. mi.)", ascending = False).head(30)

plt.figure(figsize = (5, 10))
sns.barplot(x = largeArea30Data["Area (sq. mi.)"], y = largeArea30Data["Country"])
plt.title("Top 30 Countries with the Largest Area")
plt.xlabel("Area")
plt.ylabel("Countries")
plt.show()





#POINT GRAPH OF B/D RATIO FOR TOP 50 COUNTRIES WITH HIGH LITERACY
highLitData = world.sort_values("Literacy (%)", ascending = False).head(50)

plt.figure(figsize = (10, 5))
sns.pointplot(x = highLitData["Country"], y = highLitData["Birthrate"], color = "green", alpha = 0.8)
sns.pointplot(x = highLitData["Country"], y = highLitData["Deathrate"], color = "red", alpha = 0.6)
plt.text(1, 32, "Birthrate", color = "green", fontsize = 14)
plt.text(1, 29, "Deathrate", color = "red", fontsize = 14)
plt.xticks(rotation = 90)
plt.title("Birth and Death Ratios of 50 Countries of Highest Literacy")
plt.xlabel("Countries")
plt.ylabel("Ratios (%)")
plt.grid()
plt.show()



#POINT GRAPH OF B/D RATIO FOR TOP 50 COUNTRIES WITH LOW LITERACY
lowLitData = world[world["Literacy (%)"] != 0].sort_values("Literacy (%)", ascending = True).head(50)

plt.figure(figsize = (10, 5))
sns.pointplot(x = lowLitData["Country"], y = lowLitData["Birthrate"], color = "green", alpha = 0.8)
sns.pointplot(x = lowLitData["Country"], y = lowLitData["Deathrate"], color = "red", alpha = 0.6)
plt.text(1, 5, "Birthrate", color = "green", fontsize = 14)
plt.text(1, 1, "Deathrate", color = "red", fontsize = 14)
plt.xticks(rotation = 90)
plt.title("Birth and Death Ratios of 50 Countries of Lowest Literacy")
plt.xlabel("Countries")
plt.ylabel("Ratios (%)")
plt.grid()
plt.show()




#DOT PLOT OF GDP VS BIRTHRATE
plt.figure(figsize = (10, 5))
sns.lmplot(x = "GDP ($ per capita)", y = "Birthrate", data = world)
plt.xlabel("GDP")
plt.ylabel("Birthrate")
plt.title("GDP vs Birthrate")
plt.show()


#%%



#LINE PLOT OF BIRTHRATE VS RATE
plt.plot(world["Birthrate"])
plt.xlabel('Rate')
plt.ylabel('Birthrate')
plt.title('Line Plot')
plt.grid(True)
plt.show()




explode = (0, 0.1, 0, 0,0,0,0)
sizes=[15,10,25,5,30,5,10]
labels="ASIA","EASTERN EUROPE","NORTHERN AFRICA","OCEANIA","WESTERN EUROPE","SUB-SAHARAN AFRICA","NORTHERN AMERICA"
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels,explode=explode, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.show()