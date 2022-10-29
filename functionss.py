from collections import Counter
val = input("Enter string: ")


frequency_per_char = Counter(val)


print ("Per char frequency in '{}' is :\n {}".format(val, str(frequency_per_char)))
print ("Type of frequency_per_char is: ", type(frequency_per_char))
