import os
import csv

#Initializing variables
electdate=[]
revenue=0
max_revenue=0
min_revenue=0
accessed=True
changes=[]
sum_change=0
change_accessed=True
budgetcsv=os.path.join('.','budget_data.csv')
with open(budgetcsv, newline="") as budgetdata:
    budgetreader=csv.reader(budgetdata,delimiter=',')
    budgetheader=next(budgetreader)

    #looping through every row of budget_data.csv

    for row in budgetreader:
        electdate.append(row[0])

        #calculating sum of revenue
        revenue=revenue+int(row[1])

        #assigning max and min values to the first row elements
        if (accessed==True):
            max_revenue=int(row[1])
            min_revenue=int(row[1])
            min_date=row[0]
            max_date=row[0]
            accessed=False

        #calculating max and min revenue
        else:
            if(int(row[1])>max_revenue):
                max_revenue=int(row[1])
                max_date=row[0]
            if int(row[1])<min_revenue:
                min_revenue=int(row[1])
                min_date=row[0]

        #assigning revenue changes between months to list variable changes, first months change is set to 0
        if change_accessed==True:
            changes.append(0)
            change_accessed=False
            prev_revenue=row[1]
        else:
            changes.append(int(row[1])-int(prev_revenue))
            prev_revenue=row[1]

    #calculating average of revenue changes between months
    for change in changes:
         sum_change=sum_change+int(change)

    avg_change=sum_change/(len(changes)-1)
    max_date2=max_date.replace("-","-20")
    min_date2=min_date.replace("-","-20")
            
        
     #printing all the values   
        
    print("Total Months: "+str(len(electdate)))
    print("Total net amount over the entire period: $"+str(revenue))
    print("Total average change between months over the entire period: $"+"%.2f" % avg_change)
    print("Greatest Increase in Profits: "+max_date2+" ($"+str(max_revenue)+")")
    print("Greatest Decrease in Profits: "+min_date2+" ($"+str(min_revenue)+")")
