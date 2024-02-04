def find_ap_series(a,d,n):
    ap_series=[]
    for i in range(n):
        ap_series.append(a+i*d)
    return ap_series
def main():
    a,d,n=map(int,input().split())
    ap_series=find_ap_series(a,d,n)
    print(ap_series)
    print(', '.join(map(str,ap_series)))

if __name__== '__main__':
    main()