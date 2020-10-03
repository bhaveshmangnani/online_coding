
fh = open("alchemy_input.txt",'r')
fop = open("alchemy_output.txt",'w')
try :
    from collections import Counter
    tc = int(fh.readline())
    for t in range(tc):
        n = int(fh.readline())
        s = fh.readline()
        dct = dict(Counter(s))
        fop.write('Case #'+str(t+1)+": ")
        if 'A' not in dct:
            fop.write('N\n')
        elif 'B' not in dct:
            fop.write('N\n')
        elif abs(dct['A']-dct['B']) == 1:
            fop.write('Y\n')
        else:
            fop.write('N\n')
finally:
    fh.close()
    fop.close()

        
