reset = int(input('새로 시작할까요? 기존에 있던 데이터를 불러올까요? \n 1)새로 시작하기 2)불러오기'))


if reset == 2 :
    op = input('불러오기를 원하는 파일의 이름을 입력하세요. : ')
    f = open('%s.txt'%op,'r')
    content = f.read()
    print(content)
    f.close()

    
if reset == 1 :    
    script = str(input('스크립트를 입력하세요.'))
# A : 스크립트의 글자수 세기, B : 스크립트의 문장 세기
    A = len(script)
    B = script.count('.')
    sp = int(input('말의 속도를 선택하세요. \n 1)0.5배속 2)1.0배속 3)1.5배속 \n'))
    pause = int(input('문장 사이의 정지 시간을 선택하세요. \n 1)0.3초 2)0.5초 3)1초 4)1.5초 \n'))
#빠르기가 반영되지 않은 기본적인 시간 계산
    time1 = A / 10 * 3 + B * pause
#sp에서 입력받은 말의 빠르기 반영
    if sp == 1:
        time2 = time1 * 2
    if sp == 2:
        time2 = time1
    if sp == 3:
        time2 = time1 * 0.5
# time은 초 단위, 따라서 출력시 시간`분 단위 변환 필요
    h = time2//3600
    m = (time2 - (h *3600))//60
    s = time2 - (m*60 +h *3600)

    print('예상 발표 시간은 %d시간 %d분 %d초입니다.'%(h, m, s))

    write = int(input('파일을 저장하시겠습니까? \n 1)저장하기 2)프로그램 종료'))

    if write == 1:
    #파일 저장
        title = input('저장할 발표문의 제목을 입력하세요.')
        f = open('%s.txt'%title,'w')
        f.write(script)
        f.write('\n예상 발표 시간은 %d시간 %d분 %d초입니다.'%(h, m, s))
        f.close()
        print('안전하게 저장되었습니다.')
