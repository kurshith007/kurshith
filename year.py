yr = eval(int("enter the year"))
if (yr % 4) == 0:
   if (yr % 100) == 0:
       if (yr % 400) == 0:
           print("{0} is a leap year".format(yr))
       else:
           print("{0} is not a leap year".format(yr))
   else:
       print("{0} is a leap year".format(yr))
else:
   print("{0} is not a leap year".format(yr))
