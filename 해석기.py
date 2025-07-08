"""
[변수]를 만들(거야) (것 입니다).

이제부터 [변수]는 [](이)야 (입니다).
ex) a = 1
==> 이제부터 임시변수는 1이야.

[]에 []을/를 [사칙연산]해~ (줘, 주세요).
ex) a += 1
==> 임시변수에 1을 더해줘.
예외: [변수]에 []로 나누었을때의 나머지를 구해(줘, 주세요).

[] [사칙연산] []을/를 
ex) a + b ==> 변수1 더하기 변수2

[] [논리연산자] [](이/가) / (을/를)

[함수이름](이)라는 함수를 만들(거야, 것 입니다). 이 함수는:
([]와/과 []을/를) / ([], [], [], ... []을/를) 매개변수로 받아,
~고
~고
~(거야, 것 입니다).
ex) 
def add(a, b):
    return a + b

덧샘이라는 함수를 만들거야. 이 함수는:
변수1과 변수2를 매개변수로 받아,
변수1 더하기 변수2를 반환할거야.

먄약 ~ 다면:
그게 아니면 ~ 일때/이면:
아니면:

그 외 기능:
존댓말 안 쓰면 1/100 확률로 에러 남 ㅋㅋㅋ
"""
import sys, random
variables = {}

def printLine():
    print("================================================================================")

def throwErr(line, lineContent, type):
    ending = ["^^;;"] * 10 + ["ㅠㅠ"] * 5 + [";;"] * 5 + ["ㅎ"] * 2 + ["ㅋ"] * 2 + ["ㅎㅎ"] * 5 + ["\n\nㅋㅋㅋ 이것도 못하냐 ㅋㅋㅋㅋㅋ"]
    randomIndex = random.randint(0, len(ending) - 1)
    end = ending[randomIndex]

    printLine()
    print(str(line + 1) + "번째 줄애서 오류가 발생했습니다!\n")
    if type == "statementEnding": print("온전한 지시문을 작성하지 않았습니다. 작성한 줄이 [.]이나 [:]으로 끝나는지 확인하십시오 " + end)
    elif type == "unknownJosa": print("문자열 뒤에 알맞은 조사가 붙어있지 않군요. 국어 공부부터 다시 하세요 " + end)
    elif type == "invalidPrintEnding": print("\"출력\"뒤에 글자를 인식할 수 없습니다. [해줘], [해주세요], [해주시오], [주이소], [하라], [하여라], [하시오], [하십시오], [하셈]등으로 바꿔 주시길 바랍니다 " + end)
    elif type == "invalidString": print("문자열 안에 따움표를 추가하고 싶다면, [\\\"]을 입력하세요 " + end)
    elif type == "couldNotFindMokjuk": print("목적어를 찾을 수 없습니다. 다시 작성해 주시길 바랍니다 " + end)

    print("\n줄 " + str(line + 1) + ": ")
    print(lineContent)
    print("^" * len(lineContent))

    print(final)
    sys.exit()

printLine()
msg = """ __    __  ____    ____  _______  ____    ____  __    __  .___  ___. 
|  |  |  | \\   \\  /   / |   ____| \\   \\  /   / |  |  |  | |   \\/   |
|  |__|  |  \\   \\/   /  |  |__     \\   \\/   /  |  |  |  | |  \\  /  |
|   __   |   \\_    _/   |   __|     \\_    _/   |  |  |  | |  |\\/|  |
|  |  |  |     |  |     |  |____      |  |     |  `--'  | |  |  |  | 
|__|  |__|     |__|     |_______|     |__|      \\______/  |__|  |__|             

  ______   ______   .___  ___. .______    __   __       _______ .______      
 /      | /  __  \\  |   \\/   | |   _  \\  |  | |  |     |   ____||   _  \\    
|  ,----'|  |  |  | |  \\  /  | |  |_)  | |  | |  |     |  |__   |  |_)  |    
|  |     |  |  |  | |  |\\/|  | |   ___/  |  | |  |     |   __|  |      /     
|  `----.|  `--'  | |  |  |  | |  |      |  | |  `----.|  |____ |  |\\  \\.
 \\______| \\______/  |__|  |__| | _|      |__| |_______||_______|| _| \\__|
"""
print(msg)


printLine()
fpath = input("실행시킬 문서의 경로를 입력하세요: ")
printLine()

# print(fpath)
try:
    # f = open(fpath, "r")
    fpath = "임시.혜윰"
    if (fpath[-3:] != ".혜윰" and len(fpath) > 3 or fpath[-7:] != ".hyeyum" and len(fpath) > 7):
        print("앗! 헤윰 문서가 아니므로 실행시킬 수 없습니다. 확장자를 추가해 주세요.")
        printLine()
        sys.exit()

    f = open("임시.혜윰", "r") # temp
except:
    print("문서를 찾지 못했습니다.")
    printLine()
    sys.exit()

view = input("문서 내 항목을 보시는 것을 건너뛰려면 [↵]단추를 누르세요:")
if (view != ""): print("\n\n" + fpath + ":\n")
else: print(">> 미리보기를 건너뜁니다.")

lines = []
lineNo = 0

def merge(a):
    output = []
    for x in a:
        output.extend(x.replace("\"", ""))

    # print(output)
    return output

printLine()
print("실행 결과:\n")

inMultilineComment = False

while True:
    line = f.readline()
    if not line: break # exit after end of code
    line = line.replace("\n", "")
    line = line.strip()
    if view != "": print(line, end="")
    
    lines.append(list(map(str, line.split(' '))))
    final = [] # keywords

    variables = {}

    # line skip 
    if line == "": 
        lineNo += 1
        continue
    # comment detection
    elif line[0:3] == "주석 " or line[0:2] == "//": 
        lineNo += 1
        continue
    elif "//" in line:
        print("detected single line comment after start of line")
        index = line.find("//")
        line = line[0:index - 1]
        lines[lineNo] = list(map(str, line.split(' ')))
        
    elif "/*" in line:
        # line = line before /* and execute line
        inMultilineComment = True
        index = line.find("/*")
        line = line[0:index - 1]
        lines[lineNo] = list(map(str, line.split(' ')))
    
    if inMultilineComment:
        if "*/" in line: 
            inMultilineComment = False
            index = line.find("*/")
            line = line[index + 1:-1]
            lines[lineNo] = list(map(str, line.split(' ')))
            # print(line)
            # line = line after */ and execute line
        else: continue

    
    # string detection & list merging
    inString = False
    stringCompnents = []
    temp = []
    josa = []

    def connectStr(a):
        string = ""
        validJosa = ["을", "를", "의", "에", "라는", "이라는"]
        for i in range(len(a)):
            if i == len(a) -2: # character before space (space always comes last)
                if a[i] not in validJosa: throwErr(lineNo, line, "unknownJosa")
                global josa
                josa.append(a[i])
                break
            else: string += a[i]
        
        # print("문자열을 합친 결과: " + string)
        return string

    strCnt = 0
    tempCnt = 0
    for x in lines[lineNo]:
        if x.count("\"") > 2: throwErr(lineNo, line, "invalidString")
        if x[0] == "\"": 
            inString = True
            # print("문자열 시작 감지: " + x)
        if inString: 
            temp.append(x + " ")
            tempCnt += 1
        if x[0] != "\"" and "\"" in x or x[-2] == "\"" and tempCnt == 1: 
            inString = False
            # print("문자열 끝 감지: " + x)
            strCnt += 1
            connectedStr = connectStr(merge(temp))
            stringCompnents.append([connectedStr])

            final.append(connectedStr)
            final.append(josa[strCnt - 1])

            temp = []
    
    #print()
    # print("찾아낸 문자열: ", end="")
    # print(stringCompnents)

    final.append(lines[-1][-1])

    # finding action word
    lastChar = final[-1][-1]
    #print(str(len(stringCompnents)) + " | " + str(len(josa)))
    #print(josa)
    #print(final)

    # find 목적어
    def findMokjuk(): # returns index
        for i in range(len(final)):
            if final[i] == "을" or final[i] == "를": return i
        throwErr("couldNotFindMokjuk", line, lineNo)

    def printf(index, newline=True, end=""):
        if newline: print(final[index])
        else: print(final[index], end=end)

    def modifyVar(name, value):
        variables.update({name : value})
    
    endingByunHyeong = [
        "해",
        "해줘", 
        "하라", 
        "하셈", 
        "하슈", 
        "합써", 
        "하여라", 
        "하시오", 
        "해주이소", 
        "해주시오", 
        "하십시오", 
        "해주세요"
    ]
    def isValidEnding():
        for x in endingByunHyeong:
            l = len(x)
            #print(x, 3+l, len(final[-1]), validEnd)
            if len(final[-1]) == (2 + l + 1) and final[-1][-(l+1):-1] == x: return True
        return False


    # printing strings
    if final[-1][0:2] == "출력":
        if isValidEnding(): printf(findMokjuk() - 1)
        else: throwErr(lineNo, line, "invalidPrintEnding")
    
    # initializing variables

    # modifying variables
    elif final[-1][0:2] == "대입":
        if isValidEnding(): modifyVar(final[-1][0], findMokjuk() - 1)

    # Errors
    if (lastChar != "." and lastChar != ":"): throwErr(lineNo, line, "statementEnding")
    if (len(stringCompnents) != len(josa)): throwErr(lineNo, line, "mismatchedJosa")

    # print(final)
    lineNo += 1
f.close()