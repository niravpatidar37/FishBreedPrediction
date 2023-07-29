import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv("https://raw.githubusercontent.com/niravpatidar37/Data/main/Fish.csv")

df.info()
df.head()

X = df.drop(columns = ["Species"])
y = df.Species

# Create and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the trained model to a file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)