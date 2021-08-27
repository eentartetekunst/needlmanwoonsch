gap = -10
match = 5
mismatch = -4
seq1 = input("enter sequence 1: ")
seq2 = input("enter sequence 2: ")

def match_score(letter1, letter2):
    if letter1 == letter2:
        return match
    elif letter1 == '-' or letter2 == '-':
        return gap
    else:
        return mismatch


def matrix(rows, columns):
    zeromatrix = []
    for k in range(rows):
        zeromatrix.append([0]*columns)
    return zeromatrix


def nw_score(seq1, seq2):
    n = len(seq1)
    m = len(seq2)
    score = matrix(m + 1, n + 1)  # нулевая матрица с кол-вом строк = длине 1 последовательности и столбцов = длине 2 послед

    # заполнение таблицы: сначала по краям выставляем штрафы за гэп
    for i in range(0, m + 1):
        score[i][0] = gap * i

    for j in range(0, n + 1):
        score[0][j] = gap * j

    # заполняем остальные значение: идем по столбцу
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match1 = score[i - 1][j - 1] + match_score(seq1[j - 1], seq2[i - 1])
            up = score[i - 1][j] + gap
            left = score[i][j - 1] + gap
            score[i][j] = max(match1, up, left)
    return score
score_matrix = nw_score(seq1, seq2)
alignment_score = score_matrix[len(seq2)][len(seq1)]
print("Score is: ", alignment_score)


def nw(seq1, seq2):
    n = len(seq1) # кол-во столбцов
    m = len(seq2) #  строк
    score = matrix(m + 1, n + 1)

    for i in range(0, m + 1): # идем по строкам
        score[i][0] = gap * i

    for j in range(0, n + 1):
        score[0][j] = gap * j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match1 = score[i - 1][j - 1] + match_score(seq1[j-1], seq2[i-1])
            up = score[i - 1][j] + gap
            left = score[i][j - 1] + gap
            score[i][j] = max(match1, up, left)

    align1 = ""
    align2 = ""
    i = m  # строк (длина сек2)
    j = n  # столбцов (длина сек1)

    while i > 0 and j > 0:
        score_current = score[i][j]
        score_diagonal = score[i - 1][j - 1]
        score_up = score[i][j - 1]
        score_left = score[i - 1][j]

        if score_current == score_diagonal + match_score(seq1[j - 1], seq2[i - 1]):
            align1 += seq1[j - 1]
            align2 += seq2[i - 1]
            i -= 1
            j -= 1

        elif score_current == score_up + gap:
            align1 += seq1[j - 1]
            align2 += '-'
            j -= 1

        elif score_current == score_left + gap:
            align1 += '-'
            align2 += seq2[i - 1]
            i -= 1

    while j > 0:
        align1 += seq1[j - 1]
        align2 += '-'
        j -= 1
    while i > 0:
        align1 += '-'
        align2 += seq2[i - 1]
        i -= 1

    align1 = align1[::-1]
    align2 = align2[::-1]

    return align1, align2

output1, output2 = nw(seq1, seq2)
print(output1 + "\n" + output2)



# ATGAGTCTCT   CTGTCTCCTG
#проверка выравниванияя: скор 15491
# https://www.ebi.ac.uk/Tools/services/web_emboss_needle/toolresult.ebi?jobId=emboss_needle-E20210201-050244-0050-18332195-p2m
