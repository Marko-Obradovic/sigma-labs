"""Returns the top k frequent words from the input list.
"""

def generate_top_k_frequent_words(words: list[str], k: int) -> list[str]:
    word_count: dict[str, int] = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    top_k_words = sorted(
            word_count,
            key = lambda count: word_count[count],
            reverse=True
            )

    return top_k_words[:k]
