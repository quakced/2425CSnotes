import statistics

numbers=[]

numbers.append(eval(input(f"Give me your first favorite number ")))
numbers.append(eval(input(f"Give me your second favorite number ")))
numbers.append(eval(input(f"Give me a random number ")))
numbers.append(eval(input(f"Give me your another number ")))
numbers.append(eval(input(f"Give me your final number ")))
 
minimum=min(numbers)
maximum=max(numbers)
total=sum(numbers)
mode=statistics.mode(numbers)
standard=statistics.stdev(numbers)


print(f'''
min = {minimum}
max = {maximum}
ave = {total/5}
sum = {total}
mod = {mode}
std = {standard}
''')
