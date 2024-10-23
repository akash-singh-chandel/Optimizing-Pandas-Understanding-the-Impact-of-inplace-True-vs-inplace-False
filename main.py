import pandas as pd
import numpy as np
import timeit

# Create a large DataFrame for testing
df_original = pd.DataFrame({
    'A': np.random.randint(0, 100, 100000),
    'B': np.random.randn(100000),
    'C': np.random.choice([np.nan, 1, 2, 3], size=100000)
})

# 1. drop()
print("\n1. Timing for `drop()`:")

# Drop a column without inplace
time_no_inplace = timeit.timeit("df_original.drop('B', axis=1)", globals=globals(), number=100)

# Drop a column with inplace (we need to copy the original df for each operation)
time_inplace = timeit.timeit("df = df_original.copy(); df.drop('B', axis=1, inplace=True)", globals=globals(), number=100)

print(f"drop() without inplace: {time_no_inplace:.6f} seconds")
print(f"drop() with inplace: {time_inplace:.6f} seconds")

# 2. fillna()
print("\n2. Timing for `fillna()`:")

# Fill NaN values without inplace
time_no_inplace = timeit.timeit("df_original.fillna(0)", globals=globals(), number=100)

# Fill NaN values with inplace
time_inplace = timeit.timeit("df = df_original.copy(); df.fillna(0, inplace=True)", globals=globals(), number=100)

print(f"fillna() without inplace: {time_no_inplace:.6f} seconds")
print(f"fillna() with inplace: {time_inplace:.6f} seconds")

# 3. sort_values()
print("\n3. Timing for `sort_values()`:")

# Sort values without inplace
time_no_inplace = timeit.timeit("df_original.sort_values(by='A')", globals=globals(), number=100)

# Sort values with inplace
time_inplace = timeit.timeit("df = df_original.copy(); df.sort_values(by='A', inplace=True)", globals=globals(), number=100)

print(f"sort_values() without inplace: {time_no_inplace:.6f} seconds")
print(f"sort_values() with inplace: {time_inplace:.6f} seconds")

# 4. replace()
print("\n4. Timing for `replace()`:")

# Replace values without inplace
time_no_inplace = timeit.timeit("df_original.replace(1, 100)", globals=globals(), number=100)

# Replace values with inplace
time_inplace = timeit.timeit("df = df_original.copy(); df.replace(1, 100, inplace=True)", globals=globals(), number=100)

print(f"replace() without inplace: {time_no_inplace:.6f} seconds")
print(f"replace() with inplace: {time_inplace:.6f} seconds")

# 5. drop_duplicates()
print("\n5. Timing for `drop_duplicates()`:")

# Drop duplicates without inplace
time_no_inplace = timeit.timeit("df_original.drop_duplicates()", globals=globals(), number=100)

# Drop duplicates with inplace
time_inplace = timeit.timeit("df = df_original.copy(); df.drop_duplicates(inplace=True)", globals=globals(), number=100)

print(f"drop_duplicates() without inplace: {time_no_inplace:.6f} seconds")
print(f"drop_duplicates() with inplace: {time_inplace:.6f} seconds")
