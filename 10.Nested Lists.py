# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example

# The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

# alpha
# beta
# Input Format

# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines.
# - The first line contains a student's name.
# - The second line contains their grade.

# Constraints

# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry


    
N = int(input())
nested_list = []
if __name__ == '__main__':
    
    for i in range(N):
        name = str(input())
        score = float(input())
        nested_list.append([name,score]); #[['Harry', 37.21], ['Berry', 37.21]]
    # print(nested_list)
    marks = []
    for i in range(N):
      if nested_list[i][1]>0:
        marks.append([nested_list[i][1]])
    
    marks.sort()
    # print(marks)
    if len(marks)<2:
      second_lowest = marks[0]
    else:
      second_lowest = marks[1]
    # print(second_lowest)
    name_list = []
    for i in range(N):
        if nested_list[i][1]==second_lowest[0]:
            name_list.append(nested_list[i][0])
    name_list.sort()
    # print(name_list)
    print ('\n'.join(name_list))
    

    if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    students = sorted(students, key = lambda x: x[1])
    #print(students)
    #second_lowest_score = students[1][1]
    second_lowest_score = sorted(list(set([x[1] for x in students])))[1]
    desired_students = []
    for stu in students:
        if stu[1] == second_lowest_score:
            desired_students.append(stu[0])
    print("\n".join(sorted(desired_students)))
    