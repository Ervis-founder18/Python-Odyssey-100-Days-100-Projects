# Topic: sum() function and max()function  
# #1.Sum() function:
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_score= sum(student_scores) # sum() here inside ()u have to put put the iterable Datatype like List to do the sum 
print(total_score)

# 2.this same sum()function can be done in for loop also
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
sum=0 # assigning a variable to store the sum of the scores
for i in student_scores: # here we are iterating through the list and adding each score to the sum variable
    sum =sum+i
print(sum) 


# 3. max() and min() function:

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
highest_score = max(student_scores) # max() here inside ()u have to put put the
print(highest_score)

lowest_score = min(student_scores) # min() here inside ()u have to put put the
print(lowest_score)

#4. same thing can be done using for loop also:

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
max_score=0
for score in student_scores:
    if score> max_score:
        max_score=score
print(max_score)

student_scores = [10,30,45,8]
min_score=student_scores[0]
for i in student_scores:
    if i < min_score:
        min_score=i
print(min_score)