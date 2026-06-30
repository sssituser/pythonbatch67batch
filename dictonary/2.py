courses ={1:"Python",1:"Angular",2:"Java",3:".NET",4:"React"
          ,5:"Java",6:"DataScience",7:"C",8:"UI"}
print(courses)
print(courses[1])
print(courses[2])
print(courses[3])
print(courses.keys())
print(courses.values())
courses[7]="SAP" # adding the elements to the dictonary
courses[10]="PowerBI"
print(courses)
courses.setdefault(11,"ABC")#adding element
print(courses)