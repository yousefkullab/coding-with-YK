class Solution:
    
    # Format: YYYY-MM-DD
    #
    # Clarification:
    # The dates can be in any order.
    # So we use abs() to get the positive difference.
    #
    # Approach 1:
    # Brute force → date → next day → next day → ...
    #
    # Approach 2:
    # Convert each date into total number of days,
    # then calculate the difference.
    #
    # year = 365 days
    # leap year = 366 days
    #
    # total =
    # previous years' days
    # + previous months' days
    # + current day

    # Time Complexity = O(Y + M)
    # Space Complexity = O(1)

    days_in_month = [
        31, 28, 31, 30,
        31, 30, 31, 31,
        30, 31, 30, 31
    ]

    @staticmethod
    def is_leap_year(year):
        return (
            year % 400 == 0
            or (year % 4 == 0 and year % 100 != 0)
        )

    def date_to_days(self, year, month, day):

        # Days from previous years
        days = (year - 1) * 365

        for y in range(1, year):
            if self.is_leap_year(y):
                days += 1

        # Days from previous months
        for m in range(1, month):
            days += self.days_in_month[m - 1]

            if m == 2 and self.is_leap_year(year):
                days += 1

        # Current day
        days += day

        return days

    def daysBetweenDates(self, date1: str, date2: str) -> int:

        year1, month1, day1 = map(int, date1.split("-"))
        year2, month2, day2 = map(int, date2.split("-"))

        days1 = self.date_to_days(year1, month1, day1)
        days2 = self.date_to_days(year2, month2, day2)

        return abs(days1 - days2)

s = Solution()
date1 = "2019-06-29"
date2 = "2019-06-30"
print(s.daysBetweenDates(date1, date2))  # Output: 1
