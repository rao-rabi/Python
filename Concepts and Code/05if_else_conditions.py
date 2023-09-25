# if else conditions
price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: ${down_payment}")

# if elif else condition

price = 20000

if price > 50000:
    taxes = .085*price
elif price > 100000:
    taxes= .076*price
else:
    taxes=.094*price
print(taxes)