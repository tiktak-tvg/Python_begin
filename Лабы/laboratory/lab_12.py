# # Модуль 12. Стрктуры данных
# ## Абстрактные структуры данных: Стек


# ### Простой пример: проверка палиндрома

# def is_palindrome(word):
    
    # word = word.lower()
    # rword = ""
    
    # stack = Stack()
    
    # for char in word:
        # stack.push(char)
    
    # while not stack.is_empty():
        # rword += stack.pop()
    
    # return word == rword;


# ### Понимание рекурсии


# def fact(num):
    
    # stack = Stack()
    
    # while num>1:
        # stack.push(num)
        # num = num-1
    
    # product = 1
    
    # while stack.size() > 0:
        # product *= stack.pop()
    
    # return product

