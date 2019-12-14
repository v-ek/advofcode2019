def calc_fuel(mass):
    fuel = mass // 3 - 2  # Calc fuel for mass
    if fuel <= 0:
        return 0
    return fuel + calc_fuel(fuel)

fname = './input_d1.txt'
with open(fname) as f:
    content = f.readlines()

masses = [int(item.strip()) for item in content]

# Part 1
sum_fuel = sum([mass // 3 - 2 for mass in masses])
print(sum_fuel)

# Part 2
# Test cases
assert calc_fuel(14) == 2
assert calc_fuel(1969) == 966
assert calc_fuel(100756) == 50346

sum_fuel_p2 = sum([calc_fuel(mass) for mass in masses])
print(sum_fuel_p2)
