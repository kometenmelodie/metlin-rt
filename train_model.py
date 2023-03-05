import pandas as pd
import tensorflow as tf
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# Morgan fingerprints are predictors
x = pd.read_csv("data/morgan_fp.csv")

# load retention time
y = pd.read_csv("data/data.csv")
y = y["RT"]

# 75/25 split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=3515
)

# reconstruction of the METLIN model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=1000, activation="relu"))
model.add(tf.keras.layers.Dense(units=500, activation="relu"))
model.add(tf.keras.layers.Dense(units=200, activation="relu"))
model.add(tf.keras.layers.Dense(units=100, activation="relu"))
model.add(tf.keras.layers.Dense(units=1))

model.compile(optimizer="adam", loss="mean_squared_error")

# same batch size and number of epochs as in paper
model.fit(x_train, y_train, batch_size=35, epochs=20, shuffle=True)

# make predictions
y_pred = model.predict(x_test)

# calculate R²
print(r2_score(y_true=y_test, y_pred=y_pred))

model.save("model/metlin_model.h5")
