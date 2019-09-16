# srt기준

if __name__ == "__main__":
    f = open("아랫줄에 올 line", 'r', encoding='UTF8')
    lines = f.readlines()
    pinyin = []
    for idx, val in enumerate(lines):
        if(idx % 4 == 2):
            pinyin.append(val)
    f.close()

    f = open("윗줄에 올 파일", 'r', encoding='UTF8')
    lines = f.readlines()
    for idx in range(len(pinyin)):
        lines.insert(idx*5+3, pinyin[idx])
    f.close()

    f = open("병합.txt", 'w', encoding='UTF8')
    f.writelines(lines)
    f.close()
    
    
