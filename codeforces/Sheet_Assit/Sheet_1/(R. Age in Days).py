N = int(input())

days_Year = 365
days_Month = 30

year = N // days_Year
remain_days_Year = N % days_Year
month = remain_days_Year // days_Month
days = remain_days_Year % days_Month

print(f"{year} years")
print(f"{month} months")
print(f"{days} days")
