import pandas as pd
import random
import csv
array = [] 
columns = ["Student", "SUB_1","SUB_2","SUB_3","SUB_4","SUB_5","SUB_6","SUB_7","SUB_8","SUB_9","SUB_10","USUB_1","USUB_2","USUB_3","USUB_4","USUB_5","USUB_6","USUB_7","USUB_8","USUB_9","USUB_10","SGD_1","SGD_2","SGD_3","SGD_4","SGD_5","SGD_6","SGD_7","SGD_8","SGD_9","SGD_10"]
courses=[('Parallel & Distributed Computing',3),('Differential Calculus',3),('Computer Programming',3),('Discrete Structures',3),('Data Structures & Algorithms',3),('Physical Education 3',2),('Life & Works of Rizal',2),('Basic Grammar & Writing Composition (Nihongo)',2),('Technopreneurship',2),('Living in the IT Era',2),('Life & Works of Rizal',1),('Readings in Philippine History',1),('Art Appreciation',1),('Essentials of Catholic Faith & Life',1),('Understanding the Self',1)]
for each_student in range(1000):
    data_to_send=[0]*31
    subjects_toAdd=[]
    courses=[('Parallel & Distributed Computing',3),('Differential Calculus',3),('Computer Programming',3),('Discrete Structures',3),('Data Structures & Algorithms',3),('Physical Education 3',2),('Ethics',2),('Basic Grammar & Writing Composition (Nihongo)',2),('Technopreneurship',2),('Living in the IT Era',2),('Life & Works of Rizal',1),('Readings in Philippine History',1),('Art Appreciation',1),('Essentials of Catholic Faith & Life',1),('Understanding the Self',1)]
    for each_random_subject in range(10):
        
        chosen_subject=random.choice(courses)
        random_grade=random.randint(70,100)
        data_to_send[each_random_subject+1]=chosen_subject[0]
        data_to_send[each_random_subject+11]=chosen_subject[1]
        courses.remove(chosen_subject)
        data_to_send[each_random_subject+21]=random_grade
        
    print(data_to_send)
    data_to_send[0]=each_student+1

    array.append(data_to_send)

with open('final_data.csv', 'w', encoding='UTF8',newline='' ) as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(columns)

    # write the data
    writer.writerows(array)