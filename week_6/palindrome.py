# def is_palindrome(word):
#     new_word = word[::-1]

#     if word == new_word:
#         return True
#     else:
#         return False


# print(is_palindrome(input("Enter a word: ")))


def is_palindrome(word):
    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1

    return True


word = input("Enter a word: ")
print(is_palindrome(word))
