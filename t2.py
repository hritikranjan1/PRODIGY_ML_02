import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

# Load customer data from the CSV file
customer_data = pd.read_csv("/home/luvranjan/Desktop/PRODIGY_ML_02-master/hritik.csv")

# Drop the "CustomerID" column
customer_data.drop(["CustomerID"], axis=1, inplace=True)

# Visualize Age distribution
plt.figure(figsize=(10, 6))
plt.title("Ages Frequency")
sns.axes_style("dark")
sns.violinplot(y=customer_data["Age"])
plt.show()

# Visualize Spending Score and Annual Income using boxplots
plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.boxplot(y=customer_data["Spending Score (1-100)"], color="red")
plt.subplot(1, 2, 2)
sns.boxplot(y=customer_data["Annual Income (k$)"])
plt.show()

# Visualize gender distribution
gender = customer_data.Gender.value_counts()
sns.set_style("darkgrid")
plt.figure(figsize=(10, 4))
sns.barplot(x=gender.index, y=gender.values)
plt.show()

# Create age groups
age18_25 = customer_data.Age[(customer_data.Age <= 25) & (customer_data.Age >= 18)]
age26_35 = customer_data.Age[(customer_data.Age <= 35) & (customer_data.Age >= 26)]
age36_45 = customer_data.Age[(customer_data.Age <= 45) & (customer_data.Age >= 36)]
age46_55 = customer_data.Age[(customer_data.Age <= 55) & (customer_data.Age >= 46)]
age55above = customer_data.Age[customer_data.Age >= 56]

x = ["18-25", "26-35", "36-45", "46-55", "55+"]
y = [len(age18_25), len(age26_35), len(age36_45), len(age46_55), len(age55above)]

plt.figure(figsize=(15, 6))
sns.barplot(x=x, y=y, palette="rocket")
plt.title("Number of Customers and Ages")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.show()

# Create spending score groups
ss1_20 = customer_data["Spending Score (1-100)"][(customer_data["Spending Score (1-100)"] >= 1) & (customer_data["Spending Score (1-100)"] <= 20)]
ss21_40 = customer_data["Spending Score (1-100)"][(customer_data["Spending Score (1-100)"] >= 21) & (customer_data["Spending Score (1-100)"] <= 40)]
ss41_60 = customer_data["Spending Score (1-100)"][(customer_data["Spending Score (1-100)"] >= 41) & (customer_data["Spending Score (1-100)"] <= 60)]
ss61_80 = customer_data["Spending Score (1-100)"][(customer_data["Spending Score (1-100)"] >= 61) & (customer_data["Spending Score (1-100)"] <= 80)]
ss81_100 = customer_data["Spending Score (1-100)"][(customer_data["Spending Score (1-100)"] >= 81) & (customer_data["Spending Score (1-100)"] <= 100)]

ssx = ["1-20", "21-40", "41-60", "61-80", "81-100"]
ssy = [len(ss1_20), len(ss21_40), len(ss41_60), len(ss61_80), len(ss81_100)]

plt.figure(figsize=(15, 6))
sns.barplot(x=ssx, y=ssy, palette="nipy_spectral_r")
plt.title("Spending Scores")
plt.xlabel("Score")
plt.ylabel("Number of Customers Having the Score")
plt.show()

# Create annual income groups
ai0_30 = customer_data["Annual Income (k$)"][(customer_data["Annual Income (k$)"] >= 0) & (customer_data["Annual Income (k$)"] <= 30)]
ai31_60 = customer_data["Annual Income (k$)"][(customer_data["Annual Income (k$)"] >= 31) & (customer_data["Annual Income (k$)"] <= 60)]
ai61_90 = customer_data["Annual Income (k$)"][(customer_data["Annual Income (k$)"] >= 61) & (customer_data["Annual Income (k$)"] <= 90)]
ai91_120 = customer_data["Annual Income (k$)"][(customer_data["Annual Income (k$)"] >= 91) & (customer_data["Annual Income (k$)"] <= 120)]
ai121_150 = customer_data["Annual Income (k$)"][(customer_data["Annual Income (k$)"] >= 121) & (customer_data["Annual Income (k$)"] <= 150)]

aix = ["$ 0 - 30,000", "$ 30,001 - 60,000", "$ 60,001 - 90,000", "$ 90,001 - 120,000", "$ 120,001 - 150,000"]
aiy = [len(ai0_30), len(ai31_60), len(ai61_90), len(ai91_120), len(ai121_150)]

plt.figure(figsize=(15, 6))
sns.barplot(x=aix, y=aiy, palette="Set2")
plt.title("Annual Incomes")
plt.xlabel("Income")
plt.ylabel("Number of Customers")
plt.show()

# 3D Scatter Plot
sns.set_style("white")
fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(customer_data.Age, customer_data["Annual Income (k$)"], customer_data["Spending Score (1-100)"], c='blue', s=60)
ax.view_init(30, 185)
plt.xlabel("Age")
plt.ylabel("Annual Income (k$)")
ax.set_zlabel('Spending Score (1-100)')
plt.show()

# K-Means Clustering
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, init="k-means++")
    kmeans.fit(customer_data.iloc[:, 1:])
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(12, 6))
plt.grid()
plt.plot(range(1, 11), wcss, linewidth=2, color="red", marker="8")
plt.xlabel("K Value")
plt.xticks(np.arange(1, 11, 1))
plt.ylabel("WCSS")
plt.show()

# Fit K-Means with chosen number of clusters (5 in this case)
km = KMeans(n_clusters=5, init="k-means++")
clusters = km.fit_predict(customer_data.iloc[:, 1:])
customer_data["label"] = clusters

# Visualize clusters in 3D
fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111, projection='3d')
colors = ['blue', 'red', 'green', 'orange', 'purple']
for i in range(5):
    ax.scatter(customer_data.Age[customer_data.label == i], customer_data["Annual Income (k$)"][customer_data.label == i], customer_data["Spending Score (1-100)"][customer_data.label == i], c=colors[i], s=60, label=f'Cluster {i}')

ax.view_init(30, 185)
plt.xlabel("Age")
plt.ylabel("Annual Income (k$)")
ax.set_zlabel('Spending Score (1-100)')
plt.legend()
plt.show()

your_name = "Hritik ranjan"
github_link = "https://github.com/hritikranjan1"
linkedin_link = "https://www.linkedin.com/in/hritikranjan"

print(f"Name: {Hritik_ranjan}")
print(f"GitHub: {https://github.com/hritikranjan1}")
print(f"LinkedIn: {https://www.linkedin.com/in/hritik-ranjan-05a835230}")

