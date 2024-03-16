# Initial membership fee
membership_fee = 2500

# Percentage increase each year
increase_percent = 4

# Calculate and display the projected rates for the next six years
for year in range(1, 7):
    membership_fee *= 1 + increase_percent / 100
    print(f"The projected membership fee for year {year} is: ${round(membership_fee, 2)}")
