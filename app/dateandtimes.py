# import datetime

# first_day = datetime.datetime.now()
# second_day = datetime.datetime.now() + datetime.timedelta(days = 1) 
# third_day = datetime.datetime.now() + datetime.timedelta(days = 2)
# fourth_day = datetime.datetime.now() + datetime.timedelta(days = 3)
# fifth_day = datetime.datetime.now() + datetime.timedelta(days = 4)
# sixth_day = datetime.datetime.now() + datetime.timedelta(days = 5)
# seventh_day = datetime.datetime.now() + datetime.timedelta(days = 6)

from datetime import datetime, timedelta

now = datetime.now()
second_day = now + timedelta(days=1)
third_day = now + timedelta(days=2)
fourth_day = now + timedelta(days=3)
fifth_day = now + timedelta(days=4)
six_day = now + timedelta(days=5)
