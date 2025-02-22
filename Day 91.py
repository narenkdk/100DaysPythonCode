#Day 91: Data science


#Use Python for data science projects (e.g., data cleaning, feature engineering).

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Load Data
df = sns.load_dataset("titanic")

# 2. Data Cleaning
df["age"].fillna(df["age"].median(), inplace=True)
df["embark_town"].fillna(df["embark_town"].mode()[0], inplace=True)
df.drop(columns=["deck"], inplace=True)  # Too many missing values
df.drop_duplicates(inplace=True)

# Convert categorical to numerical
df["sex"] = df["sex"].map({"male": 0, "female": 1})
df["embarked"] = df["embarked"].map({"C": 0, "Q": 1, "S": 2})

# 3. Feature Engineering
df["family_size"] = df["sibsp"] + df["parch"] + 1
df["age_group"] = pd.cut(df["age"], bins=[0, 12, 18, 30, 50, 80], labels=["child", "teen", "young_adult", "adult", "senior"])
df["age_group"] = df["age_group"].cat.codes  # Convert to numerical

# 4. Exploratory Data Analysis (EDA)
sns.barplot(x="sex", y="survived", data=df)
plt.title("Survival Rate by Gender")
plt.show()

sns.histplot(df["age"], bins=30, kde=True)
plt.title("Age Distribution")
plt.show()

# 5. Machine Learning Model
features = ["sex", "age", "fare", "family_size", "age_group"]
X = df[features]
y = df["survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# 6. Model Evaluation
print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
