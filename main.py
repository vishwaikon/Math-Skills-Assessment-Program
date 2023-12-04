print("#" * 40  )
print("           The Math Skill Assesment Programme")
print ("#" * 40)
chiName = (input("Input name: "))
print( "Welcome   " + chiName )
# user input age validation
while True:
        try:
            age = int(input("Input age : "))
            if age > 8 and age < 13:
                break;
            else:
                print("Enter a value between 9 and 12")
        except ValueError:
               print("Enter an Integer")
               continue

while True:
        try:
            childClass = int(input("Input class : "))
            if childClass > 3 and childClass < 8:
                break;
            else:
                print("Enter a value between 4 and 7")
        except ValueError:
               print("Enter an Integer")
               continue
while True:
           try:
            gender = input("Input Gender : Male or Female : ")
            if gender == "Male" or gender == "Female":
                break;
            else:
                print("Enter Male or Female")
           except ValueError:
               print("Enter text")
               continue


print(" Data Entered Successfully!")
print("#" * 40)
print ("Let's Begin The Test ")
print("#" * 40)
print  (" Numerical Skills Test")
print("#" * 40)
#Questions for Numerical skill Test
n1 = """1.What is  4 + 3 = ?
a.7
b.3
c.2
"""
n2 = """2. What is 7 - 3 = ?
a.1
b.4
c.2
"""
n3 = """3.What is 12 1/2 * 4 1/2 = ?
 a.22
 b.8
 c.25"""
n4 = """Denote 7.00 PM on a Digital Clock
a. 07.00
b. 17.00
c. 19.00
"""
n5 = """ What is 3.34 + 4.83 = ?
a.8.17
b.7.43
c.9.32
"""
n6 = """ What is 7.34 * 7 = ?
a. 102.34
b. 44.87
c. 51.38
"""
n7 = """ What is 3.87 + 2.33 * 10 = ?
a.23.74
b.89.32
c. 62
  """
n8 = """ What is 9.21 * 8 = ?
a.73.68
b.34.89
c.89.3
 """
n9 = """ Display 2789ml in Liters:
a.28.89 L
b.2.789L
c.3000L
"""
n10 = """ What is 4.23 + 2.92= ?
a.7.15
b.3.34
c.4.41
"""
Nquestions = {n1:"a", n2:"b" ,n3:"c",n4:"c",n5:"a",n6:"c",n7:"c",n8:"a",n9:"b",n10:"a"}
score= 0
ranscore=0
wscore=0
for i in Nquestions:
    print(i)
    an =input("Enter a, b or c :")
    if an==Nquestions[i]:
        print("Correct Answer")
        score = score +1
        ranscore= ranscore +1
    else :
        print ("Wrong Answer")
        wscore = wscore +1



print("#" * 30 )


if score <= 4:
 print("Sorry You failed the Test")
 print("Results of the Mental Math Test ")
 print("Student Name :" + chiName)
 print("Mental Math Test Score : " + str(score))
 print("No of Correct Answers: " + str(ranscore))
 print("No of Wrong Answers :  " + str(wscore))

else:
 print("Congratulations!")
 print("Welcome to the Language Math test")
 #Questions of Language Skill Test

n1= """1. A seller sold twice as much coconut in the afternoon than previous day after
       afternoon.If he sold 200 coconuts in the afternoon, how many coconuts did he sell
       on the previous day afternoon?
            a.90
            b.100
            c.70
            """
n2 = """2. Sarah read 2/3 of a book . She calculated that she has read 120 pages. What's
            the total number of pages?
            a.190
            b.130
            c.180
            """
n3 = """3. A student selected a number , multiplied it by 2 , then subtracted 138
            from the output and the result was 102. What's the number he selected?
            a.-30
            b.70
            c.120
            """
n4 = """4.One side of a rectangle is 3cm shorter than the other side.The area increases
            by 18cm^2, when each side is increased by 1cm. Find the length of the sides
            a.8 cm and 2cm
            b.9 cm and 3cm
            c.10cm and 7cm
            """
n5 = """5.There are 24 students in the grade 8 class , They planted Jasmines and Roses
             at the school garden. Every girl planted 3 rose plants by each and every three boys planted
             1 Jasmine plant. The sum of plants they planted was 24. Find the Number of Jasmines
              and Roses they Planted
            a.20 Roses and 4 Jasmines
            b.18 Roses and 6 Jasmines
            c.12 Roses and  8 Jasmines
              """
n6 =  """6. The distance between two towns is 300Km. One train departs from town A and
            the other departs from town B, Both departed at the same time heading towards each
            other. One train moves 10Km/hr faster than the other. Calculate the speeds of the
            slower train if the distance between them is 40Km , 2 hours later from departure.(Consider two instances
            as 1.They didn't meet yet  and 2.already met each other.)
            a. 60Km/h and 80Km/h
            b. 40Km/h and 90Km/h
            c. 30Km/h and 100km/h
            """
n7 = """7. John and Mike plays badminton on weekends. John played 4 more games than
            Mike played. The total was 12 games. Find the number of games Mike played
            a.4
            b.2
            c.7
            """
n8 ="""8. The average of first 50 natural numbers is?
            a.27.30
            b.25.5
            c.12.7
            """
n9 = """ The 3 digit number which is divisible by 6?
             a.123
             b.149
             c.150
             """
n10 ="""What is 1004 divided by 2?
            a.78
            b.502
            c.442
            """

Lquestions = {n1: "b", n2: "c",n3:"c",n4:"c",n5:"b",n6:"a",n7:"a",n8:"b",n9:"c",n10:"b"}
lscore = 0
lranscore = 0
lwscore = 0
for c in Lquestions:
                print(c)
                an = input("Enter a, b or c :")
                if an == Lquestions[c]:
                    print("Correct Answer")
                    lscore = lscore + 1
                    lranscore = lranscore + 1
                else:
                    print("Wrong Answer")
                    lwscore = lwscore + 1
print("#"*40)
print("Results of the Language Math test")
print("Student Name :" + chiName)
print("Mental Math Test Score : " + str(score))
print("No of Correct Answers: " + str(ranscore))
print("No of Wrong Answers :  " + str(wscore))
print("#"*40)
print("Langauge Math Test Score : " + str(lscore))
print("No of Correct Answers: " + str(lranscore))
print("No of Wrong Answers :  " + str(lwscore))

