# AI가 계산하는 방식을 흉내 내는 작은 계산기 만들기

## 실행 방법
### 개발 환경
- 파이썬 : 3.14.6
- VSCode : 1.104.2 
- 표준 라이브러리 : json, time

### 파일 구성
```text
Mission3/
├── data.json
├── README.md
└── main.py
```
### 실행 명령어
```python
cd Mission3
python3 main.py
```

### 모드 선택 : 숫자키 입력
- 1 : 사용자 입력 모드. 3*3 사이즈의 필터 2개, 패턴 1개를 매트릭스당 공백으로 구분한 숫자 3개씩 3회 입력, 계산후 필터A,B중에서 판정값 결정.
- 2 : data.json파일에서 필터,패턴들을 읽어들여서 계산, 판정후 Cross, X, UNDECIDED 결과 출력.



