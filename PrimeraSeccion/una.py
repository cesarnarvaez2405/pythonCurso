# x = -10

# if x < 0 :
#     print("The negative number", x, " is not valid here")

# print("This is always printed")

##-------------------------------------------------------------------------------------------------------------------------------------

# s = " Esta es una prueba para la utilizacion de condicionales e interaciones"

# x = 0

# for i in s:
#     if i in ['a','e','i','o','u']:
#         x+=1

# print(x)

##----------------------------------------------------Q1------------------------------------------------------------------------------

# rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"

# rain = rainfall_mi.split(",")

# lista =[]

# for n in rain:
#     listas = float(n)
#     lista.append(listas)

# num_rainy_months = 0

# for i in lista:
#      if float(i) >= 3.0:
#                 num_rainy_months+=1
# print(num_rainy_months)
# ··-----------------------------------------------------Q2----------------------------------------------------------------------------
# sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# frase = sentence.split()

# print(frase)

# same_letter_count = 0

# for n in frase:
#     a = (n[0])

#     b = (n[len(n)-1])

#     if a == b :
#         same_letter_count+=1
# print(same_letter_count)

##---------------------------------------------------------------------------------------------------------------------------------------------

# s = " Esta es una prueba para la utilizacion de condicionales e interaciones"

# x = 0

# for i in s:
#     if i in ['a','e','i','o','u']:
#         x+=1

# print(x)
##--------------------------------------------------Q3------------------------------------------------------------------------

# items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
# acc_num = 0

# for n in items:
#     ad = str(n)
#     va = ad.count("w")
#     if va >= 1:
#         acc_num+=1
# print(acc_num)

##---------------------------------------------------------Q4---------------------------------------------------

# sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."

# frase = sentence.split()
# num_a_or_e = 0

# for n in frase:
#     ad = str(n)
#     a = ad.count("a")
#     e = ad.count("e")

#     if a >= 1 or e >= 1:
#         num_a_or_e+=1

# print(num_a_or_e)

##------------------------------------------------------------Q5-----------------------------------------------------------------


s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

num_vowels = 0

for i in s:
    if i in vowels:
        num_vowels+=1

print(num_vowels)
