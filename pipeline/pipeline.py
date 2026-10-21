import sys
print("arguments", sys.argv)
import pandas as pd

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.head())

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")

day = int(sys.argv[1])
print(f"Running pipeline for day {day}")