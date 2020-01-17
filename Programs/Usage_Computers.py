# class created
class Computer:
    
    # Functon to find seconds per day
    def SecondPerDay(self):
        tot = 36 * 6 * 50
        print("The usage of computers in seconds per day is",tot,"seconds")

    # Functon to find minutes per week
    def MinutesPerWeek(self):
        tot = 360 * 7 * 50
        print("The usage of computers in minutes per week is", tot,"minutes")

    # Funtion to find hours per month
    def HoursPerMonth(self):
        tot = 6 * 30 * 50
        print("The usage of computers in hours per month is",tot,"hours")

    # Function to find hours per year
    def PerYear(self):
        tot = 6 * 30 * 50 * 12
        print("The usage of computers per year is",tot,"hours")

# instance of class created
obj = Computer()

# Function calls
obj.SecondPerDay()
obj.MinutesPerWeek()
obj.HoursPerMonth()
obj.PerYear()

