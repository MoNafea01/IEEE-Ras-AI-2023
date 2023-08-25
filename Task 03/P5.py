"""
In a different file, import the dictionary you just created and write a
function to create a file named “busted.txt”. Save the data of dictionary
in this file without sex and score.
lines in the file should be like this 1 Atef - 1970
"""
from P4 import db_dict
db_dict_formatted = ''
for x in db_dict:
    m = db_dict[x]
    db_dict_formatted = db_dict_formatted + x +' '+m['name']+' - '+m['bd'] + '\n'
with open('busted.txt', 'wt') as f:
    f.write(db_dict_formatted)
print(db_dict_formatted)
