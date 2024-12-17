def top_k_frequent(words: list[str], k: int) -> list[str]:
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    sorted_word_list = sorted(
            word_count, 
            key = lambda count: word_count[count], 
            reverse=True
            )
    
    return sorted_word_list[:k]



