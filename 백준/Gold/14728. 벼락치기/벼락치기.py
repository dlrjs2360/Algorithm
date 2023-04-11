n,t = map(int,input().split())
chapter = [list(map(int,input().split())) for _ in range(n)]
study = {0:0}
for w,v in chapter:
    tmp = dict()
    for dv,dw in study.items():
        if (sumw := w + dw) < study.get((sumv := v + dv), t + 1):
            tmp[sumv] = sumw
    study.update(tmp)
print(max(study.keys()))