words = ["i","leetcode","love","i","love","coding"]
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

reversed_sorted_unique_word_count_values = list(reversed(list(set(word_count.values()))))
print(reversed_sorted_unique_word_count_values)

for value in reversed_sorted_unique_word_count_values:
    for word, count in word_count.items():
        if count == value:
            print(word_count[word])
