"""
Prob : 01. Letter Pairs Frequency  
 
Given a piece of text, create a histogram of letter pairs (order from high to 
low). For instance, for the text, "this is a good thing"
 
the letter pairs are: th, hi, is, is, go, oo, od, th, hi, in, and ng. (ignore a) 
 
The histogram will be: 
 
th: 2, is: 2, hi: 2 go: 1, oo: 1, od: 1, in: 1, ng: 1 
 
 
Sample Input/Output: 
 
Enter text: this is a good thing
Histogram: th: 2, is: 2, hi: 2 go: 1, oo: 1, od: 1, in: 1, ng: 1


Enter text: coooooool
Histogram: oo: 6, co: 1, ol: 1
"""

INPUT_STRING = str(input("Enter text: "))
#INPUT_STRING = "this is a good thing"
IGNORE_LEETER = "a"

OUTPUT_HISTOGRAM_DATA = {}
pair_result_list = []
# Split input string by space(" ")
for each_word in INPUT_STRING.split(' '):
    # skip/ignore all "a" word/letter matches
    if each_word != IGNORE_LEETER:
        # Iterate each word
        for letter_index, each_letter in  enumerate(each_word):
            try:
                next_letter = each_word[letter_index+1]
                # build current & next letter
                pair_letters_ptn = "{0}{1}".format(each_letter, next_letter)
                # find unique combination pair
                if pair_letters_ptn not in pair_result_list:
                    pair_result_list.append(pair_letters_ptn)
            except IndexError as e:
                # Skip Next
                pass
    else:
        continue

for each_pair_letters_ptn in pair_result_list:
    # for each pattern find no of occurences from input sting
    total_count = len([i for i in range(len(INPUT_STRING)) if INPUT_STRING.startswith(each_pair_letters_ptn, i)])
    OUTPUT_HISTOGRAM_DATA[each_pair_letters_ptn] = total_count

# Sorting a dictionary by value then key
result = sorted(OUTPUT_HISTOGRAM_DATA.items(), key=lambda x: x[1], reverse=True)
print ("Histogram: {}".format(", ".join(["{0}: {1}".format(each[0],each[1]) for each in result])))
