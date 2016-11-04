# import string
import pprint
import operator
import csv

f = open('TomSawyer.txt', 'r')
contents = f.read()

content_list = contents.split(" ")

common_words = open('common_words_list.txt', 'r').read()
common_words_list = common_words.split('\n')

word_table = dict(zip(common_words_list, [0]*len(common_words_list)))

stripped = contents.translate(string.maketrans("",""), string.punctuation).lower()

##print contents
##print "_______________"
##print stripped


#print word_table

for current_word in content_list:
    if current_word in common_words_list:
        word_table[current_word] += 1

##word_subtable = dict((a,b) for a,b in word_table.items() if b != 0)

sorted_table = sorted(word_table.items(), key=operator.itemgetter(0));
sorted_table.sort(key=operator.itemgetter(1), reverse=True);

ranked_table = dict(zip([i[0] for i in sorted_table], range(len(sorted_table))))
common_words_ranked_table = dict(zip(common_words_list, range(len(common_words_list))))

#pprint.pprint(common_words_ranked_table)

offset_table = []

for item,value in ranked_table.iteritems():
    offset_table.append( (item, common_words_ranked_table.get(item)-value, value, common_words_ranked_table.get(item)) )

offset_table.sort(key=lambda k: k[1], reverse=True)
pprint.pprint(offset_table)

with open('TomSawyer.csv','wb') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['Word','Frequency Score', 'Book Frequency', 'English Frequency'])
    for row in offset_table:
        csv_out.writerow(row)
