#Adrian Grimm
#This lab takes input test scores, calculates the average, and assigns a letter grade to the average.

total = 0
counter = 0

#write the loop to input test scores
while True:
	entry = int(input ("Enter test score: "))
	if entry == 0: break
	total += entry
	counter += 1

#Determine the average score
total = total * 1.0
if counter == 0: exit(1)
avg = total / counter
print ("Average score is %.f" % avg + '%')

#Display the number of total entries
print ("Number of entries:", counter)

#Determine the letter grade
#Grade is based on the average score
if avg >= 90:
  print ("Grade is an A")
  print ("Great Job!")
elif avg >= 80 and avg < 90:
  print ("Grade is a B")
  print ("Good Work")
elif avg >= 70 and avg < 80:
  print ("Grade is a C")
  print ("Needs improvement")
elif avg >= 60 and avg < 70:
  print ("Grade is a D")
  print ("Barely above a disgrace")
elif avg < 60:
  print ("Grade is an F")
  print ("Such FAIL")