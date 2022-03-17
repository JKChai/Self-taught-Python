words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

## inti variables
token_total = 0
token_concat = ''

## temporary storage
temp_list = []

for token in words:

    if token_total == 0:
        token_total = len(token)
    else:
        token_total += len(token)

    # print(token_total, token_concat)

    if token_total < maxWidth:

        token = token + ' '
        token_concat += token

        token_total += 1

        ## check last word
        if token[-1] == '.':
            token_concat += token
            token_concat = token_concat.ljust(maxWidth, " ")
            temp_list.append(token_concat)

        # print(token_total, token_concat)
    else:
        ## store string
        temp_list.append(token_concat)
        
        ## reset
        token_total = len(token) + 1
        token_concat = token + ' '

        ## check last word
        if token[-1] == '.':
            token_concat = token_concat.ljust(maxWidth, " ")
            temp_list.append(token_concat)


print(temp_list)



