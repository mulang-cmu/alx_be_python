"""
A Python script that calculates the simple interest earned on an investment over a period of time.
The formula for simple interest is (I = P * R * T), where:
    ( I ) is the interest earned,
    ( P ) is the principal amount (initial investment),
    ( R ) is the annual interest rate (as a decimal),
    ( T ) is the time the money is invested for in years.
"""
# principal: in dollars, rate: in percentage, time: in years.
principal = 1000
rate = 0.05 
time = 3

#claculating interest
interest = principal * rate * time

if __name__ == "__main__":
    print(f"The simple interest is: {interest}")