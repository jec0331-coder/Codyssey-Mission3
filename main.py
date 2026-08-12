# X패턴 생성(n값)
def GeneratePatternX(size):
    valueList = []
    # 버퍼=0
    buffer = 0
    for h in range[0, size]:
        for w in range[0, size]:
            # i가 버퍼,n-버퍼일때; 1;
            if w == buffer or w == size - buffer:
                valueList.append(1)
            # 아니면;0;
            else:
                valueList.append(0)

            buffer += 1


# +패턴 생성(n값)
def GeneratePatternCross(size):
    valueList = []
    halfValue = size / 2
    for h in range[0, size]:
        for w in range[0, size]:
            if h == halfValue:
                valueList.append(1)
            # 1;
            elif w == halfValue:
                valueList.append(1)
            # 아니면;0;
            else:
                valueList.append(0)


def PrintMenu():
    print("=== Mini NPU Simulator ===")
    print("")
    print("[모드 선택]")
    print("")
    print("1. 사용자 입력 (3x3)")
    print("2. data.json 분석")
    selectAction(int(input("선택:")))


def selectAction(input):
    if input == 1:
        CallMode1()
    elif input == 2:
        CallMode2()


def CallMode1():
    print("#--------------")
    print("#[1] 필터 입력")
    print("#--------------")
    print("필터 A (3줄 입력, 공백 구분)")

    filterValueListA = []
    # 행값=0;
    row = 0
    while True:
        # rowValueArr = InterpritInput(input(""))
        inputStr = input("").strip()

        try:
            # 문자열을 " "으로 파싱해서 리스트에 담고;
            parsedList = [int(x) for x in inputStr.split()]
            # 길이가 3이 아니면 -1값 리턴;
            if len(parsedList) != 3:
                print("숫자 3개를 공백으로 구분해서 입력하세요.")

            else:
                filterValueListA.extend(parsedList)
                row += 1

                # for i in range(len(parsedList)):
                # arr[i] = parsedList[i]

                if row == 3:
                    break

        except ValueError:
            print("숫자 3개를 공백으로 구분해서 입력하세요.")

        # if rowValueArr[2] < 0:
        #    # print("제대로 입력하세요.")
        #    print("숫자 3개를 공백으로 구분해서 입력하세요.")
        # else:
        #    # filterValueListA.append(rowValueArr)
        #    filterValueListA.extend(rowValueArr)
        #    row += 1
        # if row == 3:
        #    break

    print("필터 B (3줄 입력, 공백 구분)")
    filterValueListB = []
    # 행값=0;
    row = 0
    while True:
        inputStr = input("").strip()

        try:
            # 문자열을 " "으로 파싱해서 리스트에 담고;
            parsedList = [int(x) for x in inputStr.split()]
            # 길이가 3이 아니면 -1값 리턴;
            if len(parsedList) != 3:
                print("숫자 3개를 공백으로 구분해서 입력하세요.")

            else:
                filterValueListB.extend(parsedList)
                row += 1

                if row == 3:
                    break

        except ValueError:
            print("숫자 3개를 공백으로 구분해서 입력하세요.")

        # if rowValueArr[2] < 0:
        #    print("숫자 3개를 공백으로 구분해서 입력하세요.")
        # else:
        #    filterValueListB.extend(rowValueArr)
        #    row += 1
        # if row == 3:
        #    break

    print("#--------------")
    print("#[2] 패턴 입력")
    print("#--------------")

    patternValueList = []
    # 행값=0;
    row = 0
    while True:
        # rowValueArr = InterpritInput(input(""))
        inputStr = input("").strip()

        try:
            # 문자열을 " "으로 파싱해서 리스트에 담고;
            parsedList = [int(x) for x in inputStr.split()]
            # 길이가 3이 아니면 -1값 리턴;
            if len(parsedList) != 3:
                print("숫자 3개를 공백으로 구분해서 입력하세요.")

            else:
                patternValueList.extend(parsedList)
                row += 1

                if row == 3:
                    break

        except ValueError:
            print("숫자 3개를 공백으로 구분해서 입력하세요.")

        # if rowValueArr[2] < 0:
        #    print("제대로 입력하세요.")
        # else:
        #    patternValueList.extend(rowValueArr)
        #    row += 1
        # if row == 3:
        #    break

    # 필터A와 패턴값으로 점수 계산()
    scoreA, evgTimeA = MAC_for_Mode1(filterValueListA, patternValueList)
    # 필터B와 패턴값으로 점수 계산()
    scoreB, evgTimeB = MAC_for_Mode1(filterValueListB, patternValueList)

    # 허용 오차값
    e = 1e-9

    # 오차범위 밖이면;
    if abs(scoreA - scoreB) > e:
        # 연산 시간 출력;
        # print("평균 연산 시간 : ", evgTimeA)
        print(f"연산 시간(평균/10회): {evgTimeA * 1000:.2f} ms")

        print("#--------------")
        print("#[3] MAC 결과")
        print("#--------------")

        print("A 점수:", scoreA)
        print("B 점수:", scoreB)

        # 판정: 점수 큰값;
        if scoreA > scoreB:
            print("판정 : A")
        elif scoreA < scoreB:
            print("판정 : B")
        else:
            print("판정 : 동점")

    # 오차범위 안이면;
    else:
        print("#--------------")
        print("#[3] MAC 결과(판정 불가)")
        print("#--------------")

        print("A 점수:", scoreA)
        print("B 점수:", scoreB)

        # 판정불가 프린트;
        print("판정 : 판정 불가(|A-B| < 1e-9)")


import time


def MAC_for_Mode1(filterValueList, patternValueList):
    # score 계산
    score = 0
    for i in range(len(filterValueList)):
        score += filterValueList[i] * patternValueList[i]

    # return score

    # 평균 계산 시간 계산
    tmpScore = 0
    start_time = time.perf_counter()

    for i in range(10):
        for j in range(len(filterValueList)):
            tmpScore += filterValueList[j] * patternValueList[j]

    end_time = time.perf_counter()
    evgTime = (end_time - start_time) / 10
    return score, evgTime


def MacForMode2(pattern, filter):
    accScore = 0
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            accScore += pattern[i][j] * filter[i][j]

    return accScore


def CalculateEvgTimeOfMac(pattern, filter):

    if pattern == None:
        pattern = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
        filter = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]

    start_time = time.perf_counter()

    for _ in range(10):
        accScore = 0
        for i in range(len(pattern)):
            for j in range(len(pattern[i])):
                accScore += pattern[i][j] * filter[i][j]

    end_time = time.perf_counter()
    evgTime = (end_time - start_time) / 10

    return evgTime


# def InterpritInput(inputStr):
#    arr = [-1, -1, -1]

#    # 문자열을 " "으로 파싱해서 리스트에 담고;
#    parsedList = [int(x) for x in inputStr.split()]

#    # 길이가 3이 아니면 -1값 리턴;
#    if len(parsedList) != 3:
#        return arr
#    # 아니면 다 담아서 리턴;
#    else:
#        for i in range(len(parsedList)):
#            arr[i] = parsedList[i]

#    return arr


import json

# filterList=[]
# size_5_cross_Filter = None
# size_5_x_Filter = None
# size_13_cross_Filter = None
# size_13_x_Filter = None
# size_25_cross_Filter = None
# size_25_x_Filter = None
size_5_Filter = None
size_13_Filter = None
size_25_Filter = None


patternList = []


def GenerateFiltersAndPatternsFromJsonFile():
    # global filterList
    # global size_5_x_Filter
    # global size_5_cross_Filter
    # global size_13_x_Filter
    # global size_13_cross_Filter
    # global size_25_x_Filter
    # global size_25_cross_Filter
    global size_5_Filter
    global size_13_Filter
    global size_25_Filter

    global patternList

    try:
        with open("Mission3/data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        print("▶ 성공: JSON 파일을 성공적으로 불러왔습니다.\n")
    except FileNotFoundError:
        print(f"▶ 오류: 'data.json' 파일을 찾을 수 없습니다.")
        data = {}
    except json.JSONDecodeError:
        print("▶ 오류: JSON 파일이 손상되었거나 괄호가 닫히지 않았습니다.")
        data = {}

    # 데이터가 정상적으로 로드된 경우 변수에 정보 할당하기
    if data:
        # 딕셔너리 체이닝을 활용해 안전하게 특정 필터 배열을 변수에 할당합니다.
        filters_dict = data.get("filters", {})
        ## size_5의 데이터들 추출
        # size_5_cross_Filter = filters_dict.get("size_5", {}).get("cross", [])
        # size_5_x_Filter = filters_dict.get("size_5", {}).get("x", [])
        ## size_13의 데이터들 추출
        # size_13_cross_Filter = filters_dict.get("size_13", {}).get("cross", [])
        # size_13_x_Filter = filters_dict.get("size_13", {}).get("x", [])
        ## size_25의 데이터들 추출
        # size_25_cross_Filter = filters_dict.get("size_25", {}).get("cross", [])
        # size_25_x_Filter = filters_dict.get("size_25", {}).get("x", [])
        size_5_Filter = filters_dict.get("size_5", {})
        size_13_Filter = filters_dict.get("size_13", {})
        size_25_Filter = filters_dict.get("size_25", {})
        # print(size_5_Filter)
        # 라벨 정규화;
        # size_5_Filter["Cross"] = size_5_Filter.pop("cross")
        # size_5_Filter["X"] = size_5_Filter.pop("x")
        # size_13_Filter["Cross"] = size_13_Filter.pop("cross")
        # size_13_Filter["X"] = size_13_Filter.pop("x")
        # size_25_Filter["Cross"] = size_25_Filter.pop("cross")
        # size_25_Filter["X"] = size_25_Filter.pop("x")

        #
        patternData = data.get("patterns", {})
        for name, content in patternData.items():
            # content는 {"input": [...], "expected": "x"} 형태.
            content["name"] = name  # 딕셔너리 내부에 "name": "size_5_1" 쌍을 새로 추가

            # 라벨 정규화;
            # if content["expected"] == "+":
            #    content["expected"] = "Cross"
            # elif content["expected"] == "x":
            #    content["expected"] = "X"

            patternList.append(content)

        # for patternDict in patterns_dicts:
        #    dict
        # 라벨 정규화;
        NormalizeLabel()


# 라벨 정규화 함수
def NormalizeLabel():
    global patternList
    global size_5_Filter
    global size_13_Filter
    global size_25_Filter

    # filter
    size_5_Filter["Cross"] = size_5_Filter.pop("cross")
    size_5_Filter["X"] = size_5_Filter.pop("x")
    size_13_Filter["Cross"] = size_13_Filter.pop("cross")
    size_13_Filter["X"] = size_13_Filter.pop("x")
    size_25_Filter["Cross"] = size_25_Filter.pop("cross")
    size_25_Filter["X"] = size_25_Filter.pop("x")

    # pattern
    for pattern in patternList:
        if pattern["expected"] == "+":
            pattern["expected"] = "Cross"
        elif pattern["expected"] == "x":
            pattern["expected"] = "X"


def CheckSizeOfMatrix(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        return False

    for i in range(len(matrix1)):
        if len(matrix1[i]) != len(matrix2[i]):
            return False

    return True


def CallMode2():
    # global filterList
    global patternList

    print("#---------------------------------------")
    print("# [1] 필터 로드")
    print("#---------------------------------------")

    # json파일에서 사이즈별 필터2종씩 나눠 받아서 2차원 리스트로 생성;
    GenerateFiltersAndPatternsFromJsonFile()

    print("✓ size_5  필터 로드 완료 (Cross, X)")
    print("✓ size_13  필터 로드 완료 (Cross, X)")
    print("✓ size_25  필터 로드 완료 (Cross, X)")

    print("#---------------------------------------")
    print("# [2] 패턴 분석 (라벨 정규화 적용)")
    print("#---------------------------------------")

    timeOfSize3 = CalculateEvgTimeOfMac(None, None)
    timeOfSize5 = 0
    timeOfSize13 = 0
    timeOfSize25 = 0

    passedCount = 0
    failedPatternIndexList = []
    # 패턴 리스트에서
    for i in range(len(patternList)):
        # print(type(patternList))
        pattern = patternList[i]

        ## 라벨 정규화;
        # if pattern["expected"] == "+":
        #    pattern["expected"] = "Cross"
        # elif pattern["expected"] == "x":
        #    pattern["expected"] = "X"

        xFilterToUse = None
        crossFilterToUse = None

        # ---size_5_1---
        print(pattern["name"])
        # 키값에서 사이즈값을 추출
        if "_5" in pattern["name"]:
            crossFilterToUse = size_5_Filter[
                "Cross"
            ]  # size_5_cross_Filter  # filterList["size_5"]["cross"]
            xFilterToUse = size_5_Filter[
                "X"
            ]  # size_5_x_Filter  # filterList["size_5"]["x"]

            #
            timeOfSize5 = CalculateEvgTimeOfMac(pattern["input"], size_5_Filter["X"])

        elif "_13" in pattern["name"]:
            crossFilterToUse = size_13_Filter[
                "Cross"
            ]  # size_13_cross_Filter  # filterList["size_13"]["cross"]
            xFilterToUse = size_13_Filter[
                "X"
            ]  # size_13_x_Filter  # filterList["size_13"]["x"]

            #
            timeOfSize13 = CalculateEvgTimeOfMac(pattern["input"], size_13_Filter["X"])

        else:
            crossFilterToUse = size_25_Filter[
                "Cross"
            ]  # size_25_cross_Filter  # filterList["size_25"]["cross"]
            xFilterToUse = size_25_Filter[
                "X"
            ]  # size_25_x_Filter  # filterList["size_25"]["x"]

            #
            timeOfSize25 = CalculateEvgTimeOfMac(pattern["input"], size_25_Filter["X"])

        hasSameSize = CheckSizeOfMatrix(pattern["input"], crossFilterToUse)

        if hasSameSize == False:
            print("패턴의 사이즈가 필터와 맞지 않아 FAIL")
            pattern["result"] = "isNotSaveSize"
            failedPatternIndexList.append(i)
            continue

        # 해당 사이즈의 필터 2종과 MAC연산;
        crossScore = MacForMode2(crossFilterToUse, pattern["input"])
        xScore = MacForMode2(xFilterToUse, pattern["input"])
        # Cross 점수: 1.0
        print("Cross 점수:", crossScore)
        # X 점수: 5.0
        print("X 점수:", xScore)

        # 판정값 할당
        if abs(crossScore - xScore) < 1e-9:
            patternList[i]["result"] = "UNDECIDED"
        else:
            if crossScore > xScore:
                patternList[i]["result"] = "Cross"
            else:
                patternList[i]["result"] = "X"

        # 판정: X | expected: X | PASS
        # 예측값과 일치;
        if patternList[i]["result"] == pattern["expected"]:
            print(
                "판정:",
                patternList[i]["result"],
                "| expected:",
                pattern["expected"],
                "| PASS",
            )
            passedCount += 1
        # 예측값과 불일치;
        else:
            # failCount+=1
            failedPatternIndexList.append(i)

            if patternList[i]["result"] == "UNDECIDED":
                print(
                    "판정:",
                    patternList[i]["result"],
                    "| expected:",
                    pattern["expected"],
                    "| FAIL(동점규칙)",
                )
            else:
                print(
                    "판정:",
                    patternList[i]["result"],
                    "| expected:",
                    pattern["expected"],
                    "| FAIL",
                )

    # passCount=0
    ##failCount=0
    # failCaseList=[]

    # for pattern in 패턴리스트:
    #    print("패턴 :", 패턴명) #size_5_1
    #    #패턴의 십자,엑스의 MAC값 계산()
    #    scoreWithCross=
    #    scoreWithX=
    #    exp=

    #    #판정값 할당
    #    if abs(scoreWithCross-scoreWithX)>1e-9:
    #        result="UNDECIDED"
    #    else:
    #        if scoreWithX > scoreWithCross:
    #            result="X"
    #        else:
    #            result="Cross"

    #    print("Cross 점수:", scoreWithCross)
    #    print("X 점수:", scoreWithX)

    #    #예측값과 일치;
    #    if result == exp:
    #        print("판정:", result, "| expected:",exp,"| PASS")
    #        passCount+=1
    #    #예측값과 불일치;
    #    else:
    #        #failCount+=1
    #        failCaseList.extend(새 클래스에 정보 채워서)

    #        if result=="UNDECIDED":
    #            print("판정:", result, "| expected:",exp,"| FAIL(동점규칙)")
    #        else:
    #            print("판정:", result, "| expected:",exp,"| FAIL")

    print("#---------------------------------------")
    print("# [3] 성능 분석 (평균/10회)")
    print("#---------------------------------------")
    print("크기       평균 시간(ms)    연산 횟수")
    print("-------------------------------------")

    # timeOfSize3=CalculateEvgTimeOfMac()
    # timeOfSize5=
    # timeOfSize13=
    # timeOfSize25=
    # print(f"연산 시간(평균/10회): {evgTimeA * 1000:.2f} ms")

    print(f"3x3        {timeOfSize3*1000:.4f}ms         {3 * 3}")
    print(f"5x5        {timeOfSize5*1000:.4f}ms         {5 * 5}")
    print(f"13x13      {timeOfSize13*1000:.4f}ms         {13 * 13}")
    print(f"25x25      {timeOfSize25*1000:.4f}ms         {25 * 25}")

    print("#---------------------------------------")
    print("# [4] 결과 요약")
    print("#---------------------------------------")
    print("총 테스트:", str(len(patternList)), "개")
    print("통과:", str(passedCount), "개")
    print("실패:", str(len(failedPatternIndexList)), "개")

    if len(failedPatternIndexList) > 0:
        print("실패 케이스:")

        for i in range(len(failedPatternIndexList)):
            if patternList[failedPatternIndexList[i]]["result"] == "UNDECIDED":
                print(
                    patternList[failedPatternIndexList[i]]["name"],
                    ":",
                    "동점(UNDECIDED) 처리 규칙에 따라 FAIL",
                )
            elif patternList[failedPatternIndexList[i]]["result"] == "isNotSaveSize":
                print(
                    patternList[failedPatternIndexList[i]]["name"],
                    ":",
                    "패턴의 사이즈가 필터와 맞지 않아 FAIL",
                )
            else:
                print(
                    patternList[failedPatternIndexList[i]]["name"],
                    ":",
                    "판정 결과",
                    patternList[failedPatternIndexList[i]]["result"] + "로 FAIL",
                )


# 실패 케이스:
# - size_13_1: 동점(UNDECIDED) 처리 규칙에 따라 FAIL


# def SaveDataToJsonFile():
#    global highestScore
#    global quizList
#    quizDictlist = [vars(item) for item in quizList]

#    global scoreRecordList
#    recordDictlist = [vars(item) for item in scoreRecordList]

#    # 두 리스트를 하나의 큰 딕셔너리로 묶기.
#    combined_data = {
#        "best_score": highestScore,
#        "quizzes": quizDictlist,
#        "recordData": recordDictlist,
#    }

#    # 파일 쓰기 (indent=4를 주면 가독성 있게 줄바꿈됩니다)
#    with open("state.json", "w", encoding="utf-8") as file:
#        json.dump(combined_data, file, ensure_ascii=False, indent=4)


# def LoadDataFromJsonFile():
#    global highestScore

#    try:
#        # json파일 읽어들이기
#        with open("state.json", "r", encoding="utf-8") as file:
#            loaded_data = json.load(file)

#            #
#            highestScore = loaded_data.get("best_score", 0)
#            # 퀴즈 리스트
#            quizDictList = loaded_data.get("quizzes", [])
#            global quizList
#            quizList = [Quiz(**item) for item in quizDictList]

#            # 기록 리스트
#            recordDictList = loaded_data.get("recordData", [])

#    except FileNotFoundError:
#        #
#        highestScore = 0
#        # quizDictList = []
#        GenerateDefaultQuizList()
#        # 기록 리스트
#        recordDictList = []

#    except json.JSONDecodeError:
#        #
#        highestScore = 0

#        print("데이터 파일이 손상되어, 기본 퀴즈 데이터로 복구/초기화합니다.")
#        GenerateDefaultQuizList()
#        # 기록 리스트
#        recordDictList = []
#        #
#        SaveDataToJsonFile()

#    finally:
#        #
#        GenerateRemainingQuizIndexList()
#        # 기록 리스트
#        global scoreRecordList
#        scoreRecordList = [Record(**item) for item in recordDictList]


PrintMenu()
