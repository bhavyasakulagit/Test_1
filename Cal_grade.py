A = float(input("Marks obtained in A:"))
B = float(input("MArks obtained in B:"))
C = float(input("MArks obtained in C:"))

total = A+B+C
Percentage = (total/300)*100
Avg = (total)/300

'''if(Percentage>=90):
    print("Grade A total = {total} , Percentage = ")
elif(Percentage>=70 and Percentage<60):
    print("Grade B total = {total} , Percentage = ")'''

if(Percentage>=90):
    grade = 'A'
elif(Percentage>=80):
    grade = 'B'
elif(Percentage>=40 and Percentage<80):
    grade = 'C'
else:
    grade = 'Next year'
print(f"Grade = {grade}, Total = {total}, Average = {Avg}",end =(" Great Job!"))

  