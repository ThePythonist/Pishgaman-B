import datetime
import jdatetime

shamsi = jdatetime.date.fromgregorian(day=9,month=12,year=2021)
print(shamsi)
print("Rooz :",str(shamsi)[-2:])
print("Mah :",str(shamsi)[-5:-3])
print("Sal :",str(shamsi)[:4])
