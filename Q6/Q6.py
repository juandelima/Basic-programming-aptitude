'''
--- FIRMAN TUHAN ---
Amsal 14:23
Dalam tiap jerih payah ada keuntungan, tetapi kata-kata belaka mendatangkan kekurangan saja.

Yeremia 29:11
Sebab Aku ini mengetahui rancangan-rancangan apa yang ada pada-Ku mengenai kamu,
demikianlah firman TUHAN, yaitu rancangan damai sejahtera dan bukan rancangan kecelakaan,
untuk memberikan kepadamu hari depan yang penuh harapan.
'''
import string

#search other factions
def travel_xy(map_row, map_col, j, x):
    alphabet = string.ascii_lowercase
    factions = ""
    #return map_col[j][x]
    if x > 0 and x != len(map_row) - 1:
        index_x = x + 1
        while map_row[index_x] == '.' or map_row[index_x] in alphabet:
            if map_row[index_x] in alphabet:
                factions += map_row[index_x]
            
            if j != len(map_col) - 1:
                travel_col = j + 1
                while map_col[travel_col][index_x] == '.' or map_col[travel_col][index_x] in alphabet:
                    if map_col[travel_col][index_x] in alphabet:
                        if factions.count(map_col[travel_col][index_x]) >= 1:
                            break
                        factions += map_col[travel_col][index_x]
                    if travel_col == len(map_col) - 1:
                        break
                    travel_col += 1

                travel_col = j
                while map_col[travel_col][index_x] == '.' or map_col[travel_col][index_x] in alphabet:
                    if map_col[travel_col][index_x] in alphabet:
                        if factions.count(map_col[travel_col][index_x]) >= 1:
                            break
                        factions += map_col[travel_col][index_x]
                    if travel_col == 0:
                        break
                    travel_col -= 1
            else:
                travel_col = j
                while map_col[travel_col][index_x] == '.' or map_col[travel_col][index_x] in alphabet:
                    if map_col[travel_col][index_x] in alphabet:
                        if factions.count(map_col[travel_col][index_x]) >= 1:
                            break
                        factions += map_col[travel_col][index_x]
                    if travel_col == len(map_col) - 1:
                        break
                    travel_col += 1
            
            if index_x == len(map_row) - 1:
                if j != len(map_col) - 1:
                    travel_col = j + 1
                    index = len(map_row) - 1
                    while map_col[travel_col][index] == '.' or map_col[travel_col][index] in alphabet:
                        if map_col[travel_col][index] in alphabet:
                            if factions.count(map_col[travel_col][index]) >= 1:
                                break
                            factions += map_col[travel_col][index]

                        if travel_col == len(map_col) - 1:
                            idx = len(map_row) - 2
                            while map_col[travel_col][idx] == '.' or map_col[travel_col][idx] in alphabet:
                                if map_col[travel_col][idx] in alphabet:
                                    if factions.count(map_col[travel_col][idx]) >= 1:
                                        break
                                    factions += map_col[travel_col][idx]
                                if idx == 0:
                                    break
                                idx -= 1
                            break
                        travel_col += 1
                
                else:                    
                    index = len(map_row) - 1
                    travel_col = j - 1
                    while map_col[travel_col][index] == '.' or map_col[travel_col][index] in alphabet:
                        if map_col[travel_col][index] in alphabet:
                            if factions.count(map_col[travel_col][index]) >= 1:
                                break
                            factions += map_col[travel_col][index]

                        if travel_col == 0:
                            idx = len(map_row) - 2
                            while map_col[travel_col][idx] == '.' or map_col[travel_col][idx] in alphabet:
                                if map_col[travel_col][idx] in alphabet:
                                    if factions.count(map_col[travel_col][idx]) >= 1:
                                        break
                                    factions += map_col[travel_col][idx]
                                if idx == 0:
                                    break
                                idx -= 1
                            break
                        travel_col -= 1
                break
            index_x += 1
            
    elif x == 0 or x == len(map_row) - 1:
        index_x = x
        #return map_row[index_x]
        while map_row[index_x] == '.' or map_row[index_x] in alphabet:
            if map_row[index_x] in alphabet:
                factions += map_row[index_x]
            if j != len(map_col) - 1:
                travel_col = j + 1
                while map_col[travel_col][index_x] == '.' or map_col[travel_col][index_x] in alphabet:
                    if map_col[travel_col][index_x] in alphabet:
                        if factions.count(map_col[travel_col][index_x]) >= 1:
                            break
                        factions += map_col[travel_col][index_x]
                    if travel_col == len(map_col) - 1:
                        break
                    travel_col += 1
            else:
                travel_col = j
                #return travel_col, index_x
                while map_col[travel_col][index_x] == '.' or map_col[travel_col][index_x] in alphabet:
                    if map_col[travel_col][index_x] in alphabet:
                        if factions.count(map_col[travel_col][index_x]) >= 1:
                            break
                        factions += map_col[travel_col][index_x]
                    if travel_col == len(map_col) - 1:
                        break
                    travel_col += 1

            travel_col = j - 1
            #return map_col[travel_col][index_x]
            while map_col[travel_col][index_x] == '.' or map_col[travel_col][index_x] in alphabet:
                if map_col[travel_col][index_x] in alphabet:
                    if factions.count(map_col[travel_col][index_x]) >= 1:
                        break
                    factions += map_col[travel_col][index_x]
                if travel_col == 0:
                    break
                travel_col -= 1
                
            if index_x == len(map_row) - 1:
                index = len(map_row) - 1
                if j != len(map_col) - 1:
                    travel_col = j + 1
                    while map_col[travel_col][index] == '.' or map_col[travel_col][index] in alphabet:
                        if map_col[travel_col][index] in alphabet:
                            if factions.count(map_col[travel_col][index]) >= 1:
                                break
                            factions += map_col[travel_col][index]
                
                        if travel_col == len(map_col) - 1:
                            idx = len(map_row) - 2
                            while map_col[travel_col][idx] == '.' or map_col[travel_col][idx] in alphabet:
                                if map_col[travel_col][idx] in alphabet:
                                    if factions.count(map_col[travel_col][index]) >= 1:
                                        break
                                    factions += map_col[travel_col][idx]
                                if idx == 0:
                                    break
                                idx -= 1
                            break
                        travel_col += 1
                else:
                    travel_col = j
                    while map_col[travel_col][index] == '.' or map_col[travel_col][index] in alphabet:
                        if map_col[travel_col][index] in alphabet:
                            if factions.count(map_col[travel_col][index]) >= 1:
                                break
                            factions += map_col[travel_col][index]
                        if travel_col == len(map_col) - 1:
                            idx = len(map_row) - 2
                            while map_col[travel_col][idx] == '.' or map_col[travel_col][idx] in alphabet:
                                if map_col[travel_col][idx] in alphabet:
                                    if factions.count(map_col[travel_col][idx]) >= 1:
                                        break
                                    factions += map_col[travel_col][idx]
                                if idx == 0:
                                    break
                                idx -= 1
                            break
                        travel_col += 1
                
                index = len(map_row) - 1
                travel_col = j - 1
                while map_col[travel_col][index] == '.' or map_col[travel_col][index] in alphabet:
                    if map_col[travel_col][index] in alphabet:
                        if factions.count(map_col[travel_col][index]) >= 1:
                            break
                        factions += map_col[travel_col][index]

                    if travel_col == 0:
                        idx = len(map_row) - 2
                        while map_col[travel_col][idx] == '.' or map_col[travel_col][idx] in alphabet:
                            if map_col[travel_col][idx] in alphabet:
                                factions += map_col[travel_col][idx]
                            if idx == 0:
                                break
                            idx -= 1
                        break
                    travel_col -= 1
                break
            index_x += 1

    if x > 0 and x != len(map_row) - 1:
        index_x = x - 1
        while map_row[index_x] == '.' or map_row[index_x] in alphabet:
            if map_row[index_x] in alphabet:
                factions += map_row[index_x]

            if j != len(map_col) - 1:
                travel_col = j + 1
                while map_col[travel_col][index_x] == '.' or map_col[travel_col][index_x] in alphabet:
                    if map_col[travel_col][index_x] in alphabet:
                        if factions.count(map_col[travel_col][index_x]) >= 1:
                            break
                        factions += map_col[travel_col][index_x]
                    if travel_col == len(map_col) - 1:
                        break
                    travel_col += 1
            else:
                travel_col = j
                while map_col[travel_col][index_x] == '.':
                    if map_col[travel_col][index_x] in alphabet:
                        if factions.count(map_col[travel_col][index_x]) >= 1:
                            break
                        factions += map_col[travel_col][index_x]
                    if travel_col == len(map_col) - 1:
                        break
                    travel_col += 1
                    
            travel_col = j
            while map_col[travel_col][index_x] == '.' or map_col[travel_col][index_x] in alphabet:
                if map_col[travel_col][index_x] in alphabet:
                    if factions.count(map_col[travel_col][index_x]) >= 1:
                        break
                    factions += map_col[travel_col][index_x]
                if travel_col == 0:
                    break
                travel_col -= 1
                

            if index_x == 0:
                index = 0
                if j != len(map_col) - 1:
                    travel_col = j + 1           
                    while map_col[travel_col][index] == '.' or map_col[travel_col][index] in alphabet:
                        if map_col[travel_col][index] in alphabet:
                            if factions.count(map_col[travel_col][index]) >= 1:
                                break
                            factions += map_col[travel_col][index]

                        if travel_col == len(map_col) - 1:
                            idx = 1
                            while map_col[travel_col][idx] == '.' or map_col[travel_col][idx] in alphabet:
                                if map_col[travel_col][idx] in alphabet:
                                    if factions.count(map_col[travel_col][idx]) >= 1:
                                        break
                                    factions += map_col[travel_col][idx]
                                if idx == len(map_row) - 1:
                                    break
                                idx += 1
                            break
                        travel_col += 1
                else:
                    travel_col = j          
                    while map_col[travel_col][index] == '.' or map_col[travel_col][index] in alphabet:
                        if map_col[travel_col][index] in alphabet:
                            if factions.count(map_col[travel_col][index]) >= 1:
                                break
                            factions += map_col[travel_col][index]

                        if travel_col == len(map_col) - 1:
                            idx = 1
                            while map_col[travel_col][idx] == '.' or map_col[travel_col][idx] in alphabet:
                                if map_col[travel_col][idx] in alphabet:
                                    if factions.count(map_col[travel_col][idx]) >= 1:
                                        break
                                    factions += map_col[travel_col][idx]
                                if idx == len(map_row) - 1:
                                    break
                                idx += 1
                            break
                        travel_col += 1

                index = 0
                travel_col = j - 1
                while map_col[travel_col][index] == '.' or map_col[travel_col][index] in alphabet:
                    if map_col[travel_col][index] in alphabet:
                        if factions.count(map_col[travel_col][index]) >= 1:
                            break
                        factions += map_col[travel_col][index]

                    if travel_col == 0:
                        idx = x + 1
                        while map_col[travel_col][idx] == '.' or map_col[travel_col][idx] in alphabet:
                            if map_col[travel_col][idx] in alphabet:
                                if factions.count(map_col[travel_col][idx]) >= 1:
                                    break
                                factions += map_col[travel_col][idx]
                            if idx == len(map_row) - 1:
                                break
                            idx += 1
                        break
                    travel_col -= 1
                break
            index_x -= 1
        
    elif x == 0 or x == len(map_row) - 1:
        index_x = x
        while map_row[index_x] == '.' or map_row[index_x] in alphabet:
            if map_row[index_x] in alphabet:
                if factions.count(map_row[index_x]) >= 1:
                    break
                factions += map_row[index_x]

            if j != len(map_col) - 1:
                travel_col = j + 1
                while map_col[travel_col][index_x] == '.' or map_col[travel_col][index_x] in alphabet:
                    if map_col[travel_col][index_x] in alphabet:
                        if factions.count(map_col[travel_col][index_x]) >= 1:
                            break
                        factions += map_col[travel_col][index_x]
                    if travel_col == len(map_col) - 1:
                        break
                    travel_col += 1

                travel_col = j - 1
                while map_col[travel_col][index_x] == '.' or map_col[travel_col][index_x] in alphabet:
                    if map_col[travel_col][index_x] in alphabet:
                        if factions.count(map_col[travel_col][index_x]) >= 1:
                            break
                        factions += map_col[travel_col][index_x]
                    if travel_col == 0:
                        break
                    travel_col -= 1
            else:
                travel_col = j
                while map_col[travel_col][index_x] == '.' or map_col[travel_col][index_x] in alphabet:
                    if map_col[travel_col][index_x] in alphabet:
                        if factions.count(map_col[travel_col][index_x]) >= 1:
                            break
                        factions += map_col[travel_col][index_x]
                    if travel_col == len(map_col) - 1:
                        break
                    travel_col += 1
                

            if index_x == 0:
                index = 0
                if j != len(map_col) - 1:
                    travel_col = j + 1           
                    while map_col[travel_col][index] == '.' or map_col[travel_col][index] in alphabet:
                        if map_col[travel_col][index] in alphabet:
                            if factions.count(map_col[travel_col][index]) >= 1:
                                break
                            factions += map_col[travel_col][index]

                        if travel_col == len(map_col) - 1:
                            idx = 1
                            while map_col[travel_col][idx] == '.' or map_col[travel_col][idx] in alphabet:
                                if map_col[travel_col][idx] in alphabet:
                                    if factions.count(map_col[travel_col][idx]) >= 1:
                                        break
                                    factions += map_col[travel_col][idx]
                                if idx == len(map_row) - 1:
                                    break
                                idx += 1
                            break
                        travel_col += 1
                else:
                    travel_col = j          
                    while map_col[travel_col][index] == '.' or map_col[travel_col][index] in alphabet:
                        if map_col[travel_col][index] in alphabet:
                            if factions.count(map_col[travel_col][index]) >= 1:
                                break
                            factions += map_col[travel_col][index]

                        if travel_col == len(map_col) - 1:
                            idx = 1
                            while map_col[travel_col][idx] == '.' or map_col[travel_col][idx] in alphabet:
                                if map_col[travel_col][idx] in alphabet:
                                    if factions.count(map_col[travel_col][idx]) >= 1:
                                        break
                                    factions += map_col[travel_col][idx]
                                if idx == len(map_row) - 1:
                                    break
                                idx += 1
                            break
                        travel_col += 1

                index = 0
                travel_col = j - 1
                while map_col[travel_col][index] == '.' or map_col[travel_col][index] in alphabet:
                    if map_col[travel_col][index] in alphabet:
                        if factions.count(map_col[travel_col][index]) >= 1:
                            break
                        factions += map_col[travel_col][index]

                    if travel_col == 0:
                        idx = x + 1
                        while map_col[travel_col][idx] == '.' or map_col[travel_col][idx] in alphabet:
                            if map_col[travel_col][idx] in alphabet:
                                if factions.count(map_col[travel_col][idx]) >= 1:
                                    break
                                factions += map_col[travel_col][idx]
                            if idx == len(map_row) - 1:
                                break
                            idx += 1
                        break
                    travel_col -= 1
                break
            index_x -= 1

    if j != len(map_col) - 1:
        index = x
        indexx = x + 1
        travel_col = j + 1
        indexx_ = x - 1
        while map_col[travel_col][index] == '.' or map_col[travel_col][index] in alphabet:
            if map_col[travel_col][index] in alphabet:
                if factions.count(map_col[travel_col][index]) >= 1:
                    break
                factions += map_col[travel_col][index]

            if x != len(map_row) - 1:
                while map_col[travel_col][indexx] == '.' or map_col[travel_col][indexx] in alphabet:
                    if map_col[travel_col][indexx] in alphabet:
                        if factions.count(map_col[travel_col][indexx]) >= 1:
                            break
                        factions += map_col[travel_col][indexx]
                    if indexx == len(map_row) - 1:
                        break
                    indexx += 1
                indexx = x
                index = x
            else:
                while map_col[travel_col][index] == '.' or map_col[travel_col][index] in alphabet:
                    if map_col[travel_col][index] in alphabet:
                        if factions.count(map_col[travel_col][index]) >= 1:
                            break
                        factions += map_col[travel_col][index]
                    if index == len(map_row) - 1:
                        break
                    index += 1
                index = x

            
            if travel_col == len(map_col) - 1:
                break
            travel_col += 1
    else:
        index = x
        indexx = x + 1
        travel_col = j
        indexx_ = x - 1
        while map_col[travel_col][index] == '.' or map_col[travel_col][index] in alphabet:
            if map_col[travel_col][index] in alphabet:
                if factions.count(map_col[travel_col][index]) >= 1:
                    break
                factions += map_col[travel_col][index]

            if x != len(map_row) - 1:
                while map_col[travel_col][indexx] == '.' or map_col[travel_col][indexx] in alphabet:
                    if map_col[travel_col][indexx] in alphabet:
                        if factions.count(map_col[travel_col][indexx]) >= 1:
                            break
                        factions += map_col[travel_col][indexx]
                    if indexx == len(map_row) - 1:
                        break
                    indexx += 1
                indexx = x
                index = x
            else:
                while map_col[travel_col][index] == '.' or map_col[travel_col][index] in alphabet:
                    if map_col[travel_col][index] in alphabet:
                        if factions.count(map_col[travel_col][index]) >= 1:
                            break
                        factions += map_col[travel_col][index]
                    if index == len(map_row) - 1:
                        break
                    index += 1
                index = x

            while map_col[travel_col][indexx_] == '.' or map_col[travel_col][indexx_] in alphabet:
                if map_col[travel_col][indexx_] in alphabet:
                    if factions.count(map_col[travel_col][indexx]) >= 1:
                        break
                    factions += map_col[travel_col][indexx_]
                if indexx_ == 0:
                    break
                indexx_ -= 1
            indexx_ = x
            index = x
            
            if travel_col == len(map_col) - 1:
                break
            travel_col += 1
        
    return factions
    
def map_of_kingdom(mapp, T, string):
    #search factions
    alphabet = string.ascii_lowercase
    factions = []
    for i in range(len(mapp)):
        tmp = []
        for j in range(len(mapp[i])):
            for x in range(len(mapp[i][j])):
                if mapp[i][j][x] != '#' and mapp[i][j][x] != '.':
                    if (x >= 0 and x < len(mapp[i][j]) - 1) and (j >= 0 and j < len(mapp[i]) - 1):
                        if mapp[i][j][x] == mapp[i][j][x+1] or mapp[i][j][x] == mapp[i][j+1][x]:
                            continue
                    tmp.append(mapp[i][j][x])
        factions.append(tmp)
    #return factions
    #war - berperang
    filter_factions = []
    for i in range(len(mapp)):
        temp = []
        for j in range(len(mapp[i])):
            str_tmp = ""
            for x in range(len(mapp[i][j])):
                if mapp[i][j][x] != '#' and mapp[i][j][x] != '.':
                    if (x >= 0 and x < len(mapp[i][j]) - 1) and (j >= 0 and j < len(mapp[i]) - 1):
                        if mapp[i][j][x] == mapp[i][j][x+1] or mapp[i][j][x] == mapp[i][j+1][x]:
                            continue
                    cek = travel_xy(mapp[i][j], mapp[i], j, x)
                    if cek != "":
                        if len(cek) > 1:
                            for _ in cek:
                                if mapp[i][j][x] != _:
                                    continue
                                str_tmp += mapp[i][j][x]
                        else:
                            if mapp[i][j][x] != cek:
                                continue
                    str_tmp += mapp[i][j][x]        
            temp.append(str_tmp)
        filter_factions.append(temp)
        
    #join elemen
    join_factions = []
    for i in range(len(filter_factions)):
        tmp = []
        for j in range(len(filter_factions[i])):
            for k in range(len(filter_factions[i][j])):
                tmp.append(filter_factions[i][j][k])
        join_factions.append(tmp)
    
    #remove duplicate elemen
    fix_factions = []
    for i in range(len(join_factions)):
        join_factions[i].sort()
        tmp = []
        for j in range(len(join_factions[i])):
            if len(join_factions[i]) > 1:
                if join_factions[i][j-1] == join_factions[i][j]:
                    continue
                tmp.append(join_factions[i][j])
            else:
                tmp.append(join_factions[i][j])
        fix_factions.append(tmp)

    ''' search contested '''
    contested = []
    for i in range(len(mapp)):
        counter = 0
        cts_temp = []
        for j in range(len(mapp[i])):
            tmp = []
            for x in range(len(mapp[i][j])):
                if mapp[i][j][x] != '.' and mapp[i][j][x] != '#':
                    if x >= 0 and x < len(mapp[i][j]) - 1:
                        index_j = j
                        while mapp[i][index_j][x] == '.' or mapp[i][index_j][x] in alphabet:
                            index_x = x
                            while mapp[i][index_j][index_x] == '.' or mapp[i][index_j][index_x] in alphabet:
                                if mapp[i][j][x] != mapp[i][index_j][index_x] and mapp[i][index_j][index_x] in alphabet:
                                   counter += 1
                                   tmp += [i, 'Contested %d'%(counter)]
                                if index_x == len(mapp[i][j]) - 1:
                                    break
                                index_x += 1
                            if index_j == len(mapp[i]) - 1:
                                break
                            index_j += 1
                    else:
                        if j >= 0 and j < len(mapp[i]) - 1:
                            index_j = j + 1
                            while mapp[i][index_j][x] == '.':
                                if mapp[i][j][x] != mapp[i][index_j][x] and mapp[i][index_j][x] in alphabet:
                                   counter += 1
                                   tmp += [i, 'Contested %d'%(counter)]
                                if index_j == len(mapp[i]) - 1:
                                    break
                                index_j += 1
            if tmp != []:
                cts_temp.append(tmp)
        contested.append(cts_temp)
    #return contested
                            
                            

    final_factions = []
    for i in range(len(fix_factions)):
        tmp1 = []
        for j in range(len(fix_factions[i])):
            tmp1 += [[fix_factions[i][j], factions[i].count(fix_factions[i][j])]]
        final_factions.append(tmp1)
    
    for i in range(len(final_factions)):
        print("Case %d:"%(i+1))
        for j in range(len(final_factions[i])):
            for x in range(len(final_factions[i][j])):
                print(final_factions[i][j][x], end = ' ')
            print()
        if contested[i] != []:
            if contested[i][0][0] == i:
                print(contested[i][0][1])
def main():
    T = int(input())
    mapp = [""]*T
    found = []
    if 1 <= T <= 100:
        for i in range(T):
            N = int(input())
            M = int(input())
            if 1 <= N <= 100 and 1 <= M <= 100:
                mapp[i] = [""]*N
                for j in range(N):
                    MT = input()
                    if len(MT) == M:
                        mapp[i][j] = MT
        map_of_kingdom(mapp, T, string)

if __name__ == "__main__":
    main()
