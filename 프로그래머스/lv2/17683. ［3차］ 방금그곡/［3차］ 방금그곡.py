def convertor(time):
    hour,minute = time.split(':')
    return 60*int(hour)+int(minute)

def removeShop(s):
    ns = s.replace("C#",'c').replace("D#",'d').replace('F#','f').replace('G#','g').replace('A#','a')
    return ns

def solution(m, musicinfos):
    answer = []
    m = removeShop(m)
    for i,x in enumerate(musicinfos):
        start,end,name,music = x.split(',')
        music = removeShop(music)
        playTime = convertor(end) - convertor(start)
        origin = music*(playTime // L)+music[:(playTime % L)] if playTime > (L:=len(music)) else music[:playTime]
        if m in origin:
            answer.append((-playTime,i,name))
    return sorted(answer)[0][2] if answer else "(None)"