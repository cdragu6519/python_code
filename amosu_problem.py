# finds all the combinations of the word amosu

ls = ['A', 'M', 'O', 'S', 'U']
i = 1
for x in ls:
    ls1 = ['A', 'M', 'O', 'S', 'U']
    ls1.remove(x)
    for y in ls1:
        ls2 = ['A', 'M', 'O', 'S', 'U']
        ls2.remove(x)
        ls2.remove(y)
        for z in ls2:
            ls3 = ['A', 'M', 'O', 'S', 'U']
            ls3.remove(x)
            ls3.remove(y)
            ls3.remove(z)
            for a in ls3:
                ls4 = ['A', 'M', 'O', 'S', 'U']
                ls4.remove(x)
                ls4.remove(y)
                ls4.remove(z)
                ls4.remove(a)
                for b in ls4:
                    print(str(i) + ' ' + x + y + z + a + b)
                    i = i + 1
