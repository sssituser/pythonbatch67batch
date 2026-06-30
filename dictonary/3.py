courses ={1:"Python",1:"Angular",2:"Java",3:".NET",4:"React"
          ,5:"Java",6:"DataScience",7:"C",8:"UI"}
#Reading values
print(courses[1])
print(courses)
for key in courses.keys():
    print(f'{key}===>{courses.get(key)}')
    
print(courses.get(6))
print(courses.__getitem__(7))
