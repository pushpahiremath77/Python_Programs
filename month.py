month=input("Enter month:")
if month in ('January','March','May','July','August','October','December'):
    print("Number of days:31 days")

elif month in ('April','June','September','November'):
    print("Number of days:30 days")

elif month=='February':
    print("Number of days:28/29 days")

else:
    print("Invalid month!!!")
      








