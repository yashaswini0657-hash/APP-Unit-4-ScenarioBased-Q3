
import numpy as np
import pandas as pd

# Create NumPy array of mobile prices
prices = np.array([18000, 25000, 32000, 45000, 28000, 55000])

print("Mobile Prices:")
print(prices)

# Price statistics
print("\nMean Price:", np.mean(prices))
print("Median Price:", np.median(prices))
print("Maximum Price:", np.max(prices))
print("Minimum Price:", np.min(prices))

# Pandas DataFrame
mobiles = pd.DataFrame({
    "Mobile": ["Samsung", "OnePlus", "Vivo", "iPhone", "Realme", "Redmi"],
    "Price": prices
})

print("\nMobile Details:")
print(mobiles)

print("\nMobiles costing more than Rs. 30,000:")
print(mobiles[mobiles["Price"] > 30000])

# Mobile Prices:
# [18000 25000 32000 45000 28000 55000]

# Mean Price: 33833.333333333336
# Median Price: 30000.0
# Maximum Price: 55000
# Minimum Price: 18000

# Mobile Details:
#     Mobile  Price
# 0  Samsung  18000
# 1  OnePlus  25000
# 2     Vivo  32000
# 3   iPhone  45000
# 4   Realme  28000
# 5    Redmi  55000

# Mobiles costing more than Rs. 30,000:
#    Mobile  Price
# 2    Vivo  32000
# 3  iPhone  45000
# 5   Redmi  55000