def latest(scores):
    scores.sort()
    if scores[0] == 0:
        return scores[1]
    else:
        return scores[0]


def personal_best(scores):
    scores.sort(reverse=True)
    return scores[0]


def personal_top_three(scores):
    scores.sort(reverse=True)
    return scores[0:3]


test_list = [5, 9, 0, 2, 4, 7, 6, 100, 56, 523]
latest(test_list)
personal_best(test_list)
personal_top_three(test_list)

