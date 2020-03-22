# import library to work with csv files
import csv
import os

# Create a dictionary for the final output
poll_analysis = {}
poll_analysis.update({'summary_text': 'Election Results'})
poll_analysis.update({'line_format': '----------------------------'})
# create a dictionary for keeping log of election results
poll_candidates = {}
# variable for total votes
total_votes = 0
count = 0
# for formatting
translationtable = str.maketrans({'[': '', ']': '',"'":""})
# open the csv file in the resource folder
# Create an object that operates like a regular reader but maps the information in each row to a dict whose keys are given by the optional fieldnames parameter(Dictionary Reader)
poll_reader = csv.DictReader(open('Resources/election_data.csv', mode='r', newline='\n'))
for row in poll_reader:
    # you need to read each entry and add it against a unique candidate
    if ([k for k, v in poll_candidates.items() if k == row['Candidate']]):
        total_votes = poll_candidates[row['Candidate']]
        total_votes = total_votes + 1
        poll_candidates[row['Candidate']] = total_votes
    else:
        # this is a new key in the dictionary with count set to 1
        total_votes = 1
        poll_candidates.update({row['Candidate']: total_votes})

    count = count + 1
# The total number of months included in the dataset. This should be the count of entries in the dictionary
poll_analysis.update({'Total Votes: ': count})
poll_analysis.update({'line_format1': '----------------------------'})
for k, v in poll_candidates.items():
    temp_key = str(k) + ": " + "{:.3%}".format(v/count)
    poll_analysis.update({temp_key: v})
    temp_key=""
poll_analysis.update({'line_format2': '----------------------------'})
# to print the winner
lst_votesplit = list(poll_candidates.values())
winner_name = str([k for k,v in poll_candidates.items() if v == max(lst_votesplit)]).translate(translationtable)
#winner_key = "Winner: " + winner_name
poll_analysis.update({'Winner: ': winner_name})
poll_analysis.update({'line_format3': '----------------------------'})

if (os.path.exists('Output/output.txt')):
    # for now just delete if exists
    os.remove('Output/output.txt')
f = open('Output/output.txt', 'w')
for k, v in poll_analysis.items():
    if (str(k) == "summary_text"):
        print(v)
        f.write(str(v))
        f.write("\n")
    elif (str(k) == "line_format"):
        print(v)
        f.write(str(v))
        f.write("\n")
    elif (str(k) == "line_format1"):
        print(v)
        f.write(str(v))
        f.write("\n")
    elif (str(k) == "line_format2"):
        print(v)
        f.write(str(v))
        f.write("\n")
    elif (str(k) == "line_format3"):
        print(v)
        f.write(str(v))
        f.write("\n")
    elif (str(k) == "Winner: "):
        print(str(k) + "  " + str(v) )
        f.write(str(k) + "  " + str(v) )
        f.write("\n")
    else:
        print(str(k) + "  (" + str(v) + ")")
        f.write(str(k) + "  ("+ str(v)+")")
        f.write("\n")
f.close()
