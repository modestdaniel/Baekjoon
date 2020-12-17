for a in range (2,101):
    for b in range(2, 101):
        for c in range(2, 101):
            for d in range(2, 101):
                if pow(a,3)==pow(b,3)+pow(c,3)+pow(d,3):
                    if b<c and c<d:
                        print("Cube = %d, Triple = (%d,%d,%d)"%(a,b,c,d)) ;break