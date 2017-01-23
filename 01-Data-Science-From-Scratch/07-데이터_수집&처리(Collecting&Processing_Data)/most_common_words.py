import sys
from collections import Counter

try:
    num_words = int(sys.argv[1]) # int가 아닌 값이 들어오면 error
except:
    print ("usage: most_common_words.py number of words")
    sys.exit(1) # exit 뒤에 0 이외의 숫자가 들어오면 error를 의미

counter = Counter(word.lower()
                  for line in sys.stdin
                  for word in line.strip().split()
                  if word)

for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")
