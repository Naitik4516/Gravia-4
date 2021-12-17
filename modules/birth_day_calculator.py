import datetime

# # driver code to check the above function
# def main(birth_date, birth_month, birth_year):
#     # current dd// mm/yyyy
#     today_date = datetime.datetime.now().strftime("%x/%G").split("/")
#     print(today_date)
#     current_date = int(today_date[1])
#     current_month = int(today_date[0])
#     current_year = int(today_date[3])

#     # function call to print age
#     findAge(current_date, current_month, current_year, birth_date, birth_month, birth_year)

class findAge(object):
    def __init__(self, birth_date, birth_month, birth_year):
        today_date = datetime.datetime.now().strftime("%x/%G").split("/")
        print(today_date)
        current_date = int(today_date[1])
        current_month = int(today_date[0])
        current_year = int(today_date[3])
        # days of every month
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # if birth date is greater then current birth
        # month then do not count this month and add 30
        # to the date so as to subtract the date and
        # get the remaining days
        if birth_date > current_date:
            current_date = current_date + month[birth_month - 1]
            current_month = current_month - 1

        # if birth month exceeds current month, then do
        # not count this year and add 12 to the month so
        # that we can subtract and find out the difference
        if birth_month > current_month:
            current_year = current_year - 1
            current_month = current_month + 12

        # calculate date, month, year
        self.calculated_date = current_date - birth_date
        self.calculated_month = current_month - birth_month
        self.calculated_year = current_year - birth_year

        # print the present age
        print(f"Present Age\nYears: {self.calculated_year} Months: {self.calculated_month} Days: {self.calculated_date}\n", end = '')
    
    def get(self) -> tuple:
        return (self.calculated_year, self.calculated_month,  self.calculated_date)

if __name__ == '__main__':
    print(findAge(2,2,2009).get()[0])
