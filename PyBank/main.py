# import library to work with csv files
import csv
import os
# Create a dictionary for the final output
financial_analysis = {}
# find total of all entries in the csv
count = 0
sum_total = 0
# need a variable for recording the changes in profit/loss for every month
dict_changes={}
lst_change = []
last_rec_change = 0
last_change = 0
financial_analysis.update({'summary_text': 'Financial Analysis'})
financial_analysis.update({'line_format': '----------------------------'})
# for formatting
translationtable = str.maketrans({'[': '', ']': '',"'":""})
# open the csv file in the resource folder
# Create an object that operates like a regular reader but maps the information in each row to a dict whose keys are given by the optional fieldnames parameter(Dictionary Reader)
budget_reader = csv.DictReader(open('Resources/budget_data.csv', mode='r', newline='\n'))
for row in budget_reader:
    # if this is the first iteration then you need to initialize last_change
    if count==0:
        last_change = float(row['Profit/Losses'])

    else:
        last_change = float(row['Profit/Losses']) - last_change
        dict_changes.update({row['Date']:last_change})

        sum_total = sum_total + float(row['Profit/Losses'])
        # for the next time the current value of profit/ loss needs to be assigned to last change
        last_change = float(row['Profit/Losses'])
    count = count + 1
# The total number of months included in the dataset. This should be the count of entries in the dictionary
financial_analysis.update({'Total Months': count})
# format the total amount in dollars
financial_analysis.update({'Total: ': "${:,.0f}".format(sum_total)})
# to get average change , extract all the values from dictionary into a list
lst_change = list(dict_changes.values())
#print(lst_change)
financial_analysis.update({'Average Change: ': "${:,.2f}".format(sum(lst_change)/len(lst_change))})
month_greatest = str([k for k,v in dict_changes.items() if v == max(lst_change)]).translate(translationtable)
month_lowest = str([k for k,v in dict_changes.items() if v == min(lst_change)]).translate(translationtable)

month_greatest_text = "Greatest Increase in Profits: " + month_greatest + ": "
month_lowest_text = "Greatest Decrease in Profits: " + month_lowest + ": "
financial_analysis.update({month_greatest_text : "${:,.0f}".format(max(lst_change))})
financial_analysis.update({month_lowest_text : "${:,.0f}".format(min(lst_change))})
if(os.path.exists('Output/output.txt')):
    # for now just delete if exists
    os.remove('Output/output.txt')
f = open('Output/output.txt','w')
for k, v in financial_analysis.items():
    if(str(k)=="summary_text"):
        print(v)
        f.write(str(v))
        f.write("\n")
    elif(str(k)=="line_format"):
        print(v)
        f.write(str(v))
        f.write("\n")
    else:
        print(k, v)
        f.write(str(k) + str(v))
        f.write("\n")
f.close()






