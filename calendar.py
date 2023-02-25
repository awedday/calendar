import array as arr
input_thirtyDays = arr.array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
output_thirtyDays = arr.array ('i')
for number in  input_thirtyDays: #срез
    output_thirtyDays.extend(map(int,str(number)))
    resulthirty = sum(output_thirtyDays)

print('Сумма месяца из 30 дней: ', resulthirty)

input_thirtyOneDays = arr.array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31])
output_thirtyOneDays = arr.array ('i')
for number in  input_thirtyOneDays: #срез
    output_thirtyOneDays.extend(map(int,str(number)))
    resultThirtyOne = sum(output_thirtyOneDays)

print('Сумма месяца из 31 дня: ', resultThirtyOne)

input_twentyEightDays = arr.array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28])
output_twentyEightDays = arr.array ('i')
for number in  input_twentyEightDays: #срез
    output_twentyEightDays.extend(map(int,str(number)))
    resulttwentyEight = sum(output_twentyEightDays)

print('Сумма месяца из 28 дня: ', resulttwentyEight)
result = resultThirtyOne*7+resulttwentyEight+resulthirty*4
print('Сумма за год: ', result)
