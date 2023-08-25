"""
Download this file and write a program to read the file and store the
# users in the dictionary with the following structure:
# {'id' : {'name','score','birthday’,'sex'}}
# then write a program to answer the following questions :
# a. Do no store a user with no registered score ? # [ N/A ]
# b. What is the ID of the oldest user ?
# c. What is the average score ?
# d. What is the sex of the user with the highest score ?
"""

with open('dummy_grades.txt', 'rt') as db:
    for line in db:
        x = line.split()
        if x[2].isdigit():
            db_dict.update({x[0]: {'name':x[1] , 'score': x[2] , 'bd': x[4], 'sex': x[6]}})
        elif (x[2].replace('-', '')).isdigit():
            db_dict.update({x[0]: {'name': x[1] ,'score': x[2] ,'bd': x[4] ,'sex': x[6]}})
oldest = 9999
av = 0
highest = 0
print(db_dict)
for x in db_dict:
    av += int(db_dict[x]['score'])
    if int(db_dict[x]['score']) > highest:
        highest = int(db_dict[x]['score'])
    if int(db_dict[x]['bd']) < oldest:
        oldest = int(db_dict[x]['bd'])
old = [i for i in db_dict if db_dict[i]['bd'] == str(oldest)]
high = [i for i in db_dict if db_dict[i]['score'] == str(highest)]
print("the oldest id is: "+old[0])
print("average score"+str(av))
print("sex of the highest score user: " + db_dict[high[0]]['sex'])
