import pandas as pd
import json
import matplotlib.pyplot as plt

df = pd.read_csv("random_walk.csv")

df['distant'] = (((df['x'])**2)+((df['y'])**2))**0.5
max_distant = df['distant'].max()
average_distant = df['distant'].mean()
print(max_distant)
print(average_distant)
# print(df['distant'])

new_distant = df[df['distant'] > average_distant]
# print(new_distant)
data_for_json = new_distant.to_dict(orient='records')

with open("filtered_walk.json", "w", encoding="utf-8") as f:
    json.dump(data_for_json, f, indent=4)


plt.figure(figsize=(7, 6))
plt.plot(df['x'], df['y'], label='trajectory', color="black")
plt.title("Залежність x y")
plt.xlabel("Вісь абсцис")
plt.ylabel("Віст ординат")
plt.scatter(0, 0, marker='o', color='red', label='start')
plt.scatter(df['x'].iloc[-1], df['y'].iloc[-1], marker='x', color='blue', label='end')
plt.show()

