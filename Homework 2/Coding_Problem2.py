#Brandon Escamilla PSID: 1823960

input_file = open('C:\\Users\\Brand\\PycharmProjects\\Homework-2\\Coding_Problem2\\inputDates.txt','r')
output_file = open('C:\\Users\\Brand\\PycharmProjects\\Homework-2\\Coding_Problem2\\parsedDates.txt','w')


month_list={ "january":"1","february":"2", "march":"3",
             "april":"4", "may":"5","june":"6",
             "july":"7", "august":"8", "september":"9",
             "october":"10", "november":"11", "december":"12"}
for each in input_file:
    if each!="-1":
        lis=each.split()
        if len (lis) >=3:
            month=lis [0]
            day=lis[1]
            year=lis [2]
            if month.lower() in month_list:
                comma=day[-1]
                if comma==',':
                    day=day[:len (day)-1]
                    month_number=month_list[month.lower()]
                    ans = month_number+"/"+day+"/"+year

                    output_file.write (ans)
                    output_file.write("\n")
output_file.close()
input_file.close()