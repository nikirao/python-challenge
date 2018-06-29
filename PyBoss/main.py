import os
import csv
from us_state_cd import us_state_abbrev

empfile=os.path.join(".","employee_data.csv")

#reading the employee file
with open(empfile, newline="") as empdata:
    empreader=csv.reader(empdata, delimiter=",")
    empheader=next(empreader)
    #writing formatted data to a new csv file
    with open('employee_output.csv','w') as outf:
        outf.write(','.join(['Emp ID','First Name', 'Last Name','DOB','SSN','State']))
        outf.write('\n')
        for row in empreader:
         outf.write(row[0])
         outf.write(',')

         #using the split function to split name column based on space into first and last name. Split function returns a list, join function is used to conver the list to a string.
         outf.write(','.join(row[1].split()))
         outf.write(',')
         outf.write(row[2])
         outf.write(',')

         # reading the last 4 digits of SSN and masking the first 5
         outf.write('***-**-'+row[3][-4:])
         outf.write(',')
         outf.write(us_state_abbrev.get(row[4],None))

         #newline is required for the cursor to move to next row item
         outf.write('\n')
