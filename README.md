# 💵통계학 기반 금융 데이터 분석 프로젝트💵
## 프로젝트 
### 주제 및 개요	1. 프로젝트 주제 : IM뱅크 고객 이탈 분석과 2030 세대 맞춤형 유지 전략 수립
### 2. 프로젝트 개요
### 목적 : IM뱅크 고객의 이탈 원인을 데이터 분석을 통해 파악하고, 그 중 장기적인 수익 창출에 기여할 2030 세대에 맞춘 유지 전략을 설계하여 고객 이탈을 줄이고 장기적인 충성도를 높임이고자 함
#### 1)	고객 이탈 원인 분석을 통한 연령별 이탈예측
#### 2)	2030 세대 맞춤형 유지 전략 수립

## 업데이트
## 1105 두 데이터의 컬럼명 통일 및 데이터 전처리및 파생변수 생성
### 진행
 - 카드 데이터 전처리💳 
  - 매년, 10월 이후 카드 기록이 없는 고객을 기준으로 이탈여부 칼럼 생성
  - 승인건수 칼럼을 범주에서 수치로 변경, 월별 승인건수 평균을 구하여 승인건수 칼럼 생성
  - 고객 id당 월별 승인 금액 합계 칼럼 생성

- 커스터머 데이터 전처리 👨‍💼👩‍💼
  - 자택_시도 칼럼에서 대구/경북 1로 그 외 지역은 0으로 설정
  - 수신_펀드/ 수신_외화예금 칼럼 제외
  - 수신_요구불예금, 수신_거치식예금, 수신_적립식예금 합하여 수신잔고 칼럼 생성
  - 수신잔고가 0이 아닐 경우 대출 대비 수신 비율 칼럼 생성
      - 대출 대비 수신 비율 = 대출 / 수신잔고 
  - 분석 대상을 20-30 지정
      - 이탈 비율이 가장 높았음 **

## 1106 전처리한 카드 데이터와 커스터머 데이터를 JOIN 부분 시각화
### 진행
 - 카드 데이터와 커스터머 데이터를 JOIN
     - 카드 데이터 ID와 커스터머ID를 INNER JOIN
     - 두 데이터에 있는 모든 컬럼을 병합
 - 태블로를 통한 시각화
     - 2021 커스터머 데이터로 진행
        - 2021 고객 연령 대비(20/30)
        - 2021년 고객 연령별 성별 분포
        - 2021년 고객 등급 비율
        - 2021 고객 이탈/비이탈 구성비율
        - 2021 고객 자택_시도>
        - 2021년 고객 지역구분 (대구/경북 기준)
        - 2021 지역구분에 따른 이탈/비이탈
        - 이탈여부에 따른 수신잔고 박스플롯
        - 이탈/비이탈 고객의 수신대비대출비율 분포
        - 연령대 별 이탈/비이탈
        - 연령별 지역에 따른 이탈, 비이탈
  - github를 통해 작업환경 통일(코드 통일)
  - 이탈/비이탈 고객id를 대상으로 card와 customer 데이터 연도별로 총 6개 생성
  - 파생변수 생성

### 아쉬운 점
    1. 
    - 처음에 LEFT JOIN을 진행
        --> 커스터머 ID에 대응되는 카드ID가 없는 경우 결측값이 발생
    - 커스터머 아이디와 카드 아이디가 어떤 점에서 다른지 몰라서 긴 토론..
    --> INNER JOIN을 해야 한다는 결론
        -  커스터머ID와 카드ID의 교집합을 선택하기 위해 INNER JOIN 선택
        -  iM Bank 계좌와 iM 카드를 연계해 사용하는 고객만을 분석 대상으로 선택
    2. 
    - 카드 데이터에서 2030 연령대만 추출하는 방식의 오류 
    3.
    - 커뮤니케이션 부재
        - 코드 통일 없이 각자 (조금씩 잘못된)분석을 하여 동일 데이터셋을 찾기가 어려웠음
          --> 통일한 코드를 깃허브에 업로드


## 1107 컬럼별 검정 분석 및 시각화를 통해 유의미 한지 논의
### 진행
  - 이탈여부 정의
     - 매년 카드 데이터 기준으로 3개월 간 미사용을 이탈로 정의함
     - 해당 기준으로 카드 데이터 / 커스터머 데이터 이탈여부 정의
  - 어제 만든 파생변수에 대한 시각화 및 유의 여부 평가 개선 방향 도출
 - 개선방향으로 평균승인건수에 대해 유의미 하지 않다 판단 하고 변화 추이 도출
 - 기존 제외 했던 카드 업종 대상으로 시각화후 인사이트 하나 도출
 - 인사이트 도출은 30대의 이탈과 비이탈은 기혼과 미혼으로 나눌수있다는 가능성을 도출
 - 도출한 인사이트(기혼과 미혼을 나누는 가능성) 가 유의미 한것인지 카이제곱 검정을 통해 유의미 하다는것을 도출
 - 수신요구불예금이 20대~30대 의 이탈여부에 영향이 있는지에 대해 단일 T 검정을 통해 차이가 있음을 확인 
 - 카드 3개월 사용이력으로 커스터머 이탈을 정의 할수 있는지 논의
 - 업종명별의 T 검정을 시행하기 위해 업종명별로 대분류를 진행중 (3개년 모두)
 - 컬럼별로 사용할수 있는 변수에 대해 데이터 가공중

- 아쉬운 점
1. 대응표본 t검정은 현재 데이터에 맞지 않음 통계분석에 대한 지식부족으로 인한 작업 지연 

2. 자유로운 질문을 하지 못해 작업의 지연 모르는 것은 강사님께 질문을 제시하자 ★★★

## 1108 업데이트
