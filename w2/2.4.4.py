l = []
with open('dataset_24465_4.txt', 'r') as f, open('new.txt', 'w') as new_file:
    for line in f:
        l.append(line.rstrip())
        
    l.reverse()
    l2= '\n'.join(l)
    new_file.write(l2)
