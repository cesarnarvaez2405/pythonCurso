# nums = [1,2,3,4,5,6,7,8,9,10]

# accum = 0

# for w in nums :
#      accum = accum + w
#      print(accum)


# print("range(5): ")
# for i in range(5):
#  print(i)

# print("range(0,5): ") 
# for i in range(0,5):
#     print(i)

# print(list(range(5)))

# print(list(range(0,5)))

# La varibla en modo plural e la secuencia, donde tiene que estar en la variable los datos 


## Imprimiendo resultados intermediados

# w = range(10)

# tot = 0

# for num in w:
#     print("-")
#     tot+=num
#     print(tot)
# print(tot)

# addition_str = "2+5+10+20"

# addition_str = addition_str.split("+")

# addition_str = list(map(int, addition_str))
# sum_val = 0


# for sum_vals in addition_str:

#     sum_val = sum_val + sum_vals
    
# print(sum_val)

# week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

# week_temps_f = week_temps_f.split(",")

# week_temps_f = list(map(float, week_temps_f))

# avg_temp = 0
# a = 0

# for av_temp in week_temps_f:

#     a = av_temp + a
#     avg_temp = a/(len(week_temps_f))
# print(avg_temp)

# original_str = "The quick brown rhino jumped over the extremely lazy fox"

# original_str = original_str.split()
# num_words_list=0

# a=0

# for n in original_str:
#     a = len(n)
#     print(a)
#     num_words_list = a + num_words_list 

# print(num_words_list)

let = "b"
lett = ""
for n in range(7):
    lett = let + lett
print(lett)