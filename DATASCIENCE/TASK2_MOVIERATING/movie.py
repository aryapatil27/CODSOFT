import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("movie.csv", encoding="latin1")

data.drop('Name', axis=1, inplace=True)

data['Year'] = pd.to_numeric(data['Year'], errors='coerce')

data['Duration'] = data['Duration'].astype(str).str.replace(' min', '')
data['Duration'] = pd.to_numeric(data['Duration'], errors='coerce')

data['Votes'] = data['Votes'].astype(str).str.replace(',', '')
data['Votes'] = pd.to_numeric(data['Votes'], errors='coerce')

data = data.dropna(subset=['Rating'])

data['Year'] = data['Year'].fillna(data['Year'].mean())
data['Duration'] = data['Duration'].fillna(data['Duration'].mean())
data['Votes'] = data['Votes'].fillna(data['Votes'].mean())

for col in ['Genre', 'Director', 'Actor 1', 'Actor 2', 'Actor 3']:
    data[col] = data[col].fillna('Unknown')
    data[col] = data[col].replace('', 'Unknown')

encoder = LabelEncoder()
for col in ['Genre', 'Director', 'Actor 1', 'Actor 2', 'Actor 3']:
    data[col] = encoder.fit_transform(data[col])

X = data.drop('Rating', axis=1)
X = X.fillna(0)
y = data['Rating']

print("Total samples:", len(data))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

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
