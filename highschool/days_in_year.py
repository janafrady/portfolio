from calendar import Calendar


class MyCalendar(Calendar):
  def __init__(self,year,weekday):
    self.year = year
    self.weekday = weekday
    self.cal = Calendar(self.weekday)
    self.counter = 0

  
  def count_weekday_in_year(self):
    for x in range(1,13):
      for date in self.cal.monthdays2calendar(self.year,x):
        for z in range(7):
          if date[z][1] == self.weekday and date[z][0] != 0:
            self.counter += 1
    return self.counter


test = MyCalendar(2019, 0)
another = MyCalendar(2000, 6)

print(test.count_weekday_in_year())

print(another.count_weekday_in_year())
