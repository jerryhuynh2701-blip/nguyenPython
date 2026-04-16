def helper(sentence):
    d = {}

    for word in sentence:
        d[word] = d.get(word, 0) + 1
       
        
    print(d)
    print(len(d)) 


str_input = input()

helper(str_input)



