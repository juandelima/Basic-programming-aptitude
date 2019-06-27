'''
Amsal 19:20-21
"Dengarkanlah nasihat dan terimalah didikan, supaya engkau menjadi bijak di masa depan.
Banyaklah rancangan di hati manusia, tetapi keputusan Tuhan-lah yang terlaksana."


Amsal 28:13
"Karena masa depan sungguh ada, dan harapanmu tidak akan hilang."
'''

def horizontal_search(words, w):
    found_word = []
    found_index = []
    cnt = 0
    for i in range(len(words)):
        founded = []
        for j in range(len(words[0])):
            if w[0] == words[i][j]:
                founded.append(j)
        found_index.append(founded)

    for i in range(len(found_index)):
        for j in range(len(found_index[i])):
            match = ""
            calculate_index = len(words[0]) - found_index[i][j]
            if calculate_index >= len(w):
                index = found_index[i][j]
                for k in range(len(w)):
                    match += words[i][index]
                    index += 1
                found_word.append(match)

    cnt += found_word.count(w)

    #reverse_string
    rev_string = []
    for i in range(len(words)):
        kolombaru = ""
        for j in range(len(words[0]) - 1, -1, -1):
            kolombaru += words[i][j]
        rev_string.append(kolombaru)

    found_word = []
    found_index = []
    for i in range(len(rev_string)):
        founded = []
        for j in range(len(rev_string[0])):
            if w[0] == rev_string[i][j]:
                founded.append(j)
        found_index.append(founded)

    for i in range(len(found_index)):
        for j in range(len(found_index[i])):
            match = ""
            calculate_index = len(rev_string[0]) - found_index[i][j]
            if calculate_index >= len(w):
                index = found_index[i][j]
                for k in range(len(w)):
                    match += rev_string[i][index]
                    index += 1
                found_word.append(match)

    cnt += found_word.count(w)
    
    return cnt

def vertical_search(words, w):
    transpose_word = []
    for i in range(len(words[0])):
        new_text = ""
        for j in range(len(words)):
            new_text += words[j][i]
        transpose_word.append(new_text)

    found_word = []
    found_index = []
    cnt = 0
    for i in range(len(transpose_word)):
        founded = []
        for j in range(len(transpose_word[0])):
            if w[0] == transpose_word[i][j]:
                founded.append(j)
        found_index.append(founded)

    for i in range(len(found_index)):
        for j in range(len(found_index[i])):
            match = ""
            calculate_index = len(transpose_word[0]) - found_index[i][j]
            if calculate_index >= len(w):
                index = found_index[i][j]
                for k in range(len(w)):
                    match += transpose_word[i][index]
                    index += 1
                found_word.append(match)

    cnt += found_word.count(w)

    #reverse_string
    rev_string = []
    for i in range(len(transpose_word)):
        kolombaru = ""
        for j in range(len(transpose_word[0]) - 1, -1, -1):
            kolombaru += transpose_word[i][j]
        rev_string.append(kolombaru)

    found_word = []
    found_index = []
    for i in range(len(rev_string)):
        founded = []
        for j in range(len(rev_string[0])):
            if w[0] == rev_string[i][j]:
                founded.append(j)
        found_index.append(founded)

    for i in range(len(found_index)):
        for j in range(len(found_index[i])):
            match = ""
            calculate_index = len(rev_string[0]) - found_index[i][j]
            if calculate_index >= len(w):
                index = found_index[i][j]
                for k in range(len(w)):
                    match += rev_string[i][index]
                    index += 1
                found_word.append(match)

    cnt += found_word.count(w)

    return cnt

def diagonal_search(words, w):
    cnt = 0
    found_index = []
    for i in range(len(words)):
        t_index = []
        for j in range(len(words[0])):
            if w[0] == words[i][j]:
                if j <= ((len(words[0]) - len(w)) + 1 ) - 1:
                    t_index.append(j)
        found_index.append(t_index)

    found_find = []
    for i in range((len(found_index) - len(w)) + 1):
        next_index = i
        for j in range(len(found_index[i])):
            start_index = found_index[i][j]
            match = ""
            for k in range(len(w)):
                match += words[next_index][start_index]
                start_index += 1
                next_index += 1
            found_find.append(match)
            next_index = i
        
    cnt += found_find.count(w)

    #reverse_string
    rev_string = []
    for i in range(len(words)):
        kolombaru = ""
        for j in range(len(words[0]) - 1, -1, -1):
            kolombaru += words[i][j]
        rev_string.append(kolombaru)

    found_index = []
    for i in range(len(rev_string)):
        t_index = []
        for j in range(len(rev_string[0])):
            if w[0] == rev_string[i][j]:
                if j <= ((len(rev_string[0]) - len(w)) + 1 ) - 1:
                    t_index.append(j)
        found_index.append(t_index)


    found_find = []
    for i in range((len(found_index) - len(w)) + 1):
        next_index = i
        for j in range(len(found_index[i])):
            start_index = found_index[i][j]
            match = ""
            for k in range(len(w)):
                match += rev_string[next_index][start_index]
                start_index += 1
                next_index += 1
            found_find.append(match)
            next_index = i
                
    cnt += found_find.count(w)


    #reverse index
    reverse_index = []
    #last = len(words) - len(w) - 1
    for i in range(len(words) - 1, -1, -1):
        new_str = ""
        new_str += words[i]
        reverse_index.append(new_str)

    found_index = []
    for i in range(len(reverse_index)):
        t_index = []
        for j in range(len(reverse_index[0])):
            if w[0] == reverse_index[i][j]:
                if j <= ((len(reverse_index[0]) - len(w)) + 1 ) - 1:
                    t_index.append(j)
        found_index.append(t_index)


    found_find = []
    for i in range((len(found_index) - len(w)) + 1):
        next_index = i
        for j in range(len(found_index[i])):
            start_index = found_index[i][j]
            match = ""
            for k in range(len(w)):
                match += reverse_index[next_index][start_index]
                start_index += 1
                next_index += 1
            found_find.append(match)
            next_index = i
        
    cnt += found_find.count(w)


    #reverse_string
    rev_string = []
    for i in range(len(reverse_index)):
        kolombaru = ""
        for j in range(len(reverse_index[0]) - 1, -1, -1):
            kolombaru += reverse_index[i][j]
        rev_string.append(kolombaru)


    found_index = []
    for i in range(len(rev_string)):
        t_index = []
        for j in range(len(rev_string[0])):
            if w[0] == rev_string[i][j]:
                if j <= ((len(rev_string[0]) - len(w)) + 1 ) - 1:
                    t_index.append(j)
        found_index.append(t_index)


    found_find = []
    for i in range((len(found_index) - len(w)) + 1):
        next_index = i
        for j in range(len(found_index[i])):
            start_index = found_index[i][j]
            match = ""
            for k in range(len(w)):
                match += rev_string[next_index][start_index]
                start_index += 1
                next_index += 1
            found_find.append(match)
            next_index = i
                
    cnt += found_find.count(w)
         
    return cnt


def main():
    T = int(input())
    arr = [0]*T
    count = [0]*T
    if 1 <= T <= 100:
        for i in range(T):
            N = int(input())
            M = int(input())
            arr[i] = [""]*N
            if 1 <= N <= 100 and 1 <= M <= 100:
                for j in range(N):
                    MT = input()
                    if len(MT) == M:
                        arr[i][j] = MT
                W = input()
                if 1 <= len(W) <= 100:
                    result = horizontal_search(arr[i], W) + vertical_search(arr[i], W) + diagonal_search(arr[i], W)
                    count[i] += result
                    
        for i in range(len(count)):
            print("Case %d: %d"%(i+1, count[i]))
                    
if __name__ == "__main__":
    main()
