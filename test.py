A=('G0.4-0.4,6-5-5;6-9-11(PL),VT4.1-0.1;G0.4-0.4,5-5-16;12-14-6(PL)')
B=A.split("G")
C=B[1:len(B)]
print len(C)
print C
for i in B:
    C=str(i)
    print C
    C1=str(C).split(",")
    print C1
    print C

