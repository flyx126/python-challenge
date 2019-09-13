import os
import csv

emp_id = []
full_name = []
first_name = []
last_name=[]
dob_date=[]
dob = []
ssn = []
ssn_formated = []
state=[]
new_csv=[]

state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

pyboss_csv = os.path.join(".","02-Homework_03-Python_ExtraContent_Instructions_PyBoss_employee_data.csv")


with open(pyboss_csv,"r",encoding = "UTF-8") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        emp_id.append(row[0])
        full_name = row[1].split(" ")
        first_name.append(full_name[0])
        last_name.append(full_name[1])
        
        dob_date=row[2].split("-")
        dob.append(dob_date[1] + "/" + dob_date[2] + "/" + dob_date[0])

        ssn=row[3].split("-")
        ssn_formated.append("***-**-"+ssn[2])
        
        state.append(state_abbrev[row[4]])

new_csv =zip(emp_id,first_name,last_name,dob,ssn_formated,state)

outputFile = os.path.join(".","PyBoss.csv")               #direction to the folder we want to store the new file
with open(outputFile,"w",encoding="UTF-8",newline='') as output:
    writer = csv.writer(output, delimiter = ",")
    writer.writerow(["Employe Number","First Name","Last Name","DOB","SSN","State"])
    writer.writerows(new_csv)