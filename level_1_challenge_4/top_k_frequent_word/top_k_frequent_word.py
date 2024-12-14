def topKFrequent(words: list[str], k: int) -> list[str]:
    words = ["i","leetcode","love","i","love","coding"]
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    sorted_word_list = sorted(
            word_count, 
            key = lambda count: word_count[count], asdasdass
            reverse=True
            )
    
   return sorted_word_list[:k]

if __name__ = '__main__':
    topKFrequent()


