====exercise 2 answer . function to calculate average mark of students score=======

def getData():
    Data ={}
    while True:
        studentId = input('Enter student ID first: ')
        studentMark = input('Enter marks with coma separated values: ')
        moreMarks = input('Enter "no" to quit and "yes" to continue: ')
        if studentId in Data:
            print('Two students can not have the same ID: ')
            return Data
        else: 
            Data[studentId] = studentMark.split(",")

        if moreMarks.lower() == "yes":
            continue

        elif moreMarks.lower() == "no":
            return Data
            
            
=====calling sub funtion =====
            
    def getAvg(Data):
    aveData={}
    for x in Data:
        L = Data[x]
        s = 0  # itretor
        for marks in L:
            s+=int(marks)
        aveData[x] = s/len(L)
    return aveData
        

==== getting data =====
    getSumAve = getAvg(accessData)
  
===== looping through to display the data===== 

for i in getSumAve:
    print('Average score of student with the ID :',i, 'is :', round(getSumAve[i]))
    
    
    
======exercise 1 answer ========
    
    def xmasTree():
    Data ={}
    while True:
        star_Icon = input()
        
        if star_Icon == "*":
            continue
        elif star_Icon == "|":
            return Data
            


====NOTE ! I AM RUNING THIS ON JUPITER NOTEBOOK(ANACONDA)=====






