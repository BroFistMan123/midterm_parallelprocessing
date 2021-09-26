import time
import pandas as pd
import csv
import numpy as np
import os
import multiprocessing
import threading
import concurrent.futures
def computeCourseGrade(course_grade,units):

    #Multiply course grade to the units
    return int(course_grade)*int(units)


def computeStudent(student_data):
    grade_computation=0
    for i in range(10):
        courseComputation=computeCourseGrade(student_data[i+11],student_data[i+21])
        grade_computation+=courseComputation
    return grade_computation/10

    
def read_csv_file2(csv_path):
    data = list(csv.reader(open(csv_path)))
    return data
def computeProcess(data):
    for each_data in data:
        # np.append(data,computeStudent(each_data))
        each_data.append(computeStudent(each_data))
    
    write_csv_file("m3r.csv",data)
    return True
def write_csv_file(csv_path,array):
    answ=os.path.exists(csv_path)
    with open(csv_path, "a" if answ else "w", encoding='UTF8',newline='' ) as f:
        writer = csv.writer(f)
        if not answ:
            columns = ["Student", "SUB_1","SUB_2","SUB_3","SUB_4","SUB_5","SUB_6","SUB_7","SUB_8","SUB_9","SUB_10","USUB_1","USUB_2","USUB_3","USUB_4","USUB_5","USUB_6","USUB_7","USUB_8","USUB_9","USUB_10","SGD_1","SGD_2","SGD_3","SGD_4","SGD_5","SGD_6","SGD_7","SGD_8","SGD_9","SGD_10","Grades"]
            writer.writerow(columns)
        # write the header
        # write the data
        writer.writerows(array)

def import_csv_file(csv_path):
    data = pd.read_csv(csv_path).values
    return data


if __name__=="__main__":
    data=read_csv_file2("C:/Users/fr3d3/Documents/SchoolFiles/SecondSemester/MidtermExam/final_data.csv")
    start = time.perf_counter()

 
       # for _ in range(10): #JUST A THROWAWAY VARIABLE NAME (_). 
    #     p = multiprocessing.Process(target=do_something,args=[1.5])
    #     p.start()
    #     processes.append(p)
    # for each_process in processes:
    #     each_process.join()
    #data=[['1','Differential Calculus','Readings in Philippine History','Understanding the Self','Data Structures & Algorithms','Parallel & Distributed Computing','Living in the IT Era','Ethics','Discrete Structures','Art Appreciation','Computer Programming',3,1,1,3,3,2,2,3,1,3,72,76,91,100,71,96,75,100,82,95]]
    
    # SEQUENTIAL
    # if computeProcess(data[1:]):
    #     print("Successfully implemented.")

    # SEQUENTIAL END
    # #PARALLEL
    # processes=[]
    
    # p = multiprocessing.Process(target=computeProcess,args=[data[1:500]])
    # p.start()
    # p1 = multiprocessing.Process(target=computeProcess,args=[data[500:]])
    # p1.start()
    # processes.append(p)
    # processes.append(p1)
    # for each_process in processes:
    #     each_process.join()
    # #PARALLEL END
    # #PARALLEL 250
    # processes=[]
    # p = multiprocessing.Process(target=computeProcess,args=[data[1:250]])
    
    # p1 = multiprocessing.Process(target=computeProcess,args=[data[250:500]])
    
    # p2 = multiprocessing.Process(target=computeProcess,args=[data[500:750]])
    
    # p3 = multiprocessing.Process(target=computeProcess,args=[data[750:]])
    
    # processes.append(p)
    # processes.append(p1)
    # processes.append(p2)
    # processes.append(p3)
    # for each_process in processes:
    #     each_process.start()
    # for each_process in processes:
    #     each_process.join()
    # #PARALLEL END
    # #Threading 500
    # processes=[]
    # p1 = threading.Thread(target=computeProcess,args=([data[1:500]]),)
    # p2 = threading.Thread(target=computeProcess,args=([data[500:]]),)
    # processes.append(p1)
    # processes.append(p2)
    # for each_process in processes:
    #     each_process.start()
    # for each_process in processes:
    #     each_process.join()
    # #Threading end
    # #Threading 250
    # processes=[]
    # p1 = threading.Thread(target=computeProcess,args=([data[1:250]]),)
    # p2 = threading.Thread(target=computeProcess,args=([data[250:500]]),)
    # p3 = threading.Thread(target=computeProcess,args=([data[500:750]]),)
    # p4 = threading.Thread(target=computeProcess,args=([data[750:]]),)
    # processes.append(p1)
    # processes.append(p2)
    # processes.append(p3)
    # processes.append(p4)
    # for each_process in processes:
    #     each_process.start()
    # for each_process in processes:
    #     each_process.join()
    # #Threading end
    #Concurrent Futures
    with concurrent.futures.ProcessPoolExecutor() as executor:
        
        
        results=executor.submit(computeProcess,data[1:500])
        
        results1=executor.submit(computeProcess,data[500:])
        # x=results1.result()
        # y=results.result()
        
    #concurrent end
    finish=time.perf_counter()
    print(f'Finished in {round(finish-start,3)} second(s)')
    time.sleep(5)