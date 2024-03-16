def calculate_membership_fee(initial_fee, annual_increase_rate, years):
    fees = []
    current_fee = initial_fee

    for year in range(1, years + 1):
        current_fee *= (1 + annual_increase_rate / 100)
        fees.append((year, round(current_fee, 2)))

    return fees

def display_projected_rates(fees):
    print("Year\tProjected Fee")
    print("---------------------")
    for year, fee in fees:
        print(f"{year}\t${fee}")

# Initial membership fee
initial_fee = 2500

# Annual increase rate
annual_increase_rate = 4

# Number of years
years = 6

# Calculate projected membership fees
projected_fees = calculate_membership_fee(initial_fee, annual_increase_rate, years)

# Display projected rates
display_projected_rates(projected_fees)
