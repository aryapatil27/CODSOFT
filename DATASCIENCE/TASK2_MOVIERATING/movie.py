import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import LabelEncoder

# ------------------------------------
# 1. LOAD DATASET
# ------------------------------------
data = pd.read_csv("movie.csv", encoding="latin1")

# ------------------------------------
# 2. DROP NAME
# ------------------------------------
data.drop('Name', axis=1, inplace=True)

# ------------------------------------
# 3. CLEAN NUMERIC COLUMNS
# ------------------------------------
data['Year'] = pd.to_numeric(data['Year'], errors='coerce')

data['Duration'] = data['Duration'].astype(str).str.replace(' min', '', regex=False)
data['Duration'] = pd.to_numeric(data['Duration'], errors='coerce')

data['Votes'] = data['Votes'].astype(str).str.replace(',', '', regex=False)
data['Votes'] = pd.to_numeric(data['Votes'], errors='coerce')

# ------------------------------------
# 4. REMOVE ROWS WITHOUT RATING
# ------------------------------------
data = data.dropna(subset=['Rating'])

# ------------------------------------
# 5. HANDLE MISSING VALUES
# ------------------------------------

# Numeric → mean
data['Year'].fillna(data['Year'].mean(), inplace=True)
data['Duration'].fillna(data['Duration'].mean(), inplace=True)
data['Votes'].fillna(data['Votes'].mean(), inplace=True)

# Categorical → "Unknown"
for col in ['Genre', 'Director', 'Actor 1', 'Actor 2', 'Actor 3']:
    data[col] = data[col].fillna('Unknown')
    data[col] = data[col].replace('', 'Unknown')

# ------------------------------------
# 6. ENCODE CATEGORICAL DATA
# ------------------------------------
encoder = LabelEncoder()

for col in ['Genre', 'Director', 'Actor 1', 'Actor 2', 'Actor 3']:
    data[col] = encoder.fit_transform(data[col])

# ------------------------------------
# 7. FINAL SAFETY CHECK (MOST IMPORTANT)
# ------------------------------------
data = data.dropna()   # 🔥 THIS LINE FIXES YOUR ERROR

# ------------------------------------
# 8. SPLIT FEATURES & TARGET
# ------------------------------------
X = data.drop('Rating', axis=1)
y = data['Rating']

# ------------------------------------
# 9. TRAIN-TEST SPLIT
# ------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ------------------------------------
# 10. TRAIN MODEL
# ------------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# ------------------------------------
# 11. PREDICT
# ------------------------------------
y_pred = model.predict(X_test)

# ------------------------------------
# 12. EVALUATE
# ------------------------------------
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# ------------------------------------
# 13. NEW MOVIE PREDICTION
# ------------------------------------
new_movie = pd.DataFrame({
    'Year': [2023],
    'Duration': [120],
    'Genre': [data['Genre'].mean()],
    'Votes': [500],
    'Director': [data['Director'].mean()],
    'Actor 1': [data['Actor 1'].mean()],
    'Actor 2': [data['Actor 2'].mean()],
    'Actor 3': [data['Actor 3'].mean()]
})

predicted_rating = model.predict(new_movie)
print("Predicted Movie Rating:", predicted_rating[0])
