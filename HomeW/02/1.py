## Умова:
## 1. Відомий РІК. Визначити, чи буде цей рік високосним,
##  і до якого століття цей рік відноситься.
year = int(input("Enter the year: "))
century = year // 100 + 1
print(year, " is leap." if year % 4 == 0 else " is not leap.")
print(century, " century.")
