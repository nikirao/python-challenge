import os
import csv

#Initializing variables
electdate=[]
max_revenue=-99999
min_revenue=99999
accessed=True
changes=[]
revenue=0
budgetcsv=os.path.join('.','budget_data.csv')
with open(budgetcsv, newline="") as budgetdata:
    budgetreader=csv.reader(budgetdata,delimiter=',')
    budgetheader=next(budgetreader)

    #looping through every row of budget_data.csv

    for row in budgetreader:
        electdate.append(row[0])

        #calculating sum of revenue
        revenue=revenue+int(row[1])

     
        if (accessed==True):

            #calculating revenue changes between months, first month is set to 0 
            changes.append(0)
            prev_revenue=row[1]
            accessed=False

        #calculating max and min revenue and revenue changes
        else:
            revenue_change=(int(row[1])-int(prev_revenue))
            changes.append(revenue_change)
            prev_revenue=row[1]
            if(revenue_change>max_revenue):
                max_revenue=revenue_change
                max_date=row[0]
            if revenue_change<min_revenue:
                min_revenue=revenue_change
                min_date=row[0]
            



    avg_change=sum(changes)/(len(changes)-1)
    max_date2=max_date.replace("-","-20")
    min_date2=min_date.replace("-","-20")
            
        
     #printing all the values   
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: "+str(len(electdate)))
    print("Total net amount over the entire period: $"+str(revenue))
    print("Total average change between months over the entire period: $"+"%.2f" % avg_change)
    print("Greatest Increase in Profits: "+max_date2+" ($"+str(max_revenue)+")")
    print("Greatest Decrease in Profits: "+min_date2+" ($"+str(min_revenue)+")")
