def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Different Hamming type")
    differ = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            differ += 1

    return differ


#distance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCC')
