# Part A
yearly_salary = float(input('The starting yearly salary:'))
portion_saved = float(input('The portion of your salary:'))
cost_of_dream_home = float(input('Cost of dream home:'))
portion_down_payment = 0.25
amount_saved = 0
r = 0.05
month = 0
monthly_salary = yearly_salary / 12
monthly_savings = monthly_salary * portion_saved
Down_payment = cost_of_dream_home * portion_down_payment
while amount_saved < Down_payment:
    amount_saved += amount_saved * r/12 + monthly_savings
    month += 1
print('Number of months:', month)

# Part B
yearly_salary = float(input('The starting yearly salary:'))
portion_saved = float(input('The portion of your salary:'))
cost_of_dream_home = float(input('Cost of dream home:'))
semi_annual_raise = float(input('Semi-annual raise:'))
portion_down_payment = 0.25
amount_saved = 0
r = 0.05
month = 0
monthly_salary = yearly_salary / 12
monthly_savings = monthly_salary * portion_saved
Down_payment = cost_of_dream_home * portion_down_payment
while amount_saved < Down_payment:
    if month % 6 == 0 and month != 0:
        monthly_savings += monthly_savings * semi_annual_raise
    amount_saved += amount_saved * r/12 + monthly_savings
    month += 1
print('Number of months:', month)

# Part C
initial_deposit = float(input("initial deposit: "))
cost_of_house = 800000
portion_down_payment = 0.25
Down_Payment = cost_of_house * portion_down_payment
epsilon = 100
month = 36
low = 0
high = 1
r = (low + high) / 2
amount_saved = initial_deposit * (1 + r/12) ** month
steps = 1
amount_at_max = initial_deposit * (1 + 1/12) ** 36
if initial_deposit >= Down_Payment - epsilon:
    r = 0
elif amount_at_max < Down_Payment - epsilon:
    r = None
else:
    while abs(amount_saved - Down_Payment) >= epsilon:

    if amount_saved > Down_Payment:
        high = r
    else:
        low = r
    r = (low + high) / 2
    amount_saved = initial_deposit * (1 + r / 12) ** month
    steps += 1
print(steps)
print(r)
