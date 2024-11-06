# 💵통계학 기반 금융 데이터 분석 프로젝트💵
## 프로젝트 
### 주제 및 개요	1. 프로젝트 주제 : IM뱅크 고객 이탈 분석과 2030 세대 맞춤형 유지 전략 수립
### 2. 프로젝트 개요
### 목적 : IM뱅크 고객의 이탈 원인을 데이터 분석을 통해 파악하고, 그 중 장기적인 수익 창출에 기여할 2030 세대에 맞춘 유지 전략을 설계하여 고객 이탈을 줄이고 장기적인 충성도를 높임이고자 함
#### 1)	고객 이탈 원인 분석을 통한 연령별 이탈예측
#### 2)	2030 세대 맞춤형 유지 전략 수립

## 업데이트
## 1105 두 데이터의 컬럼명 통일 및 데이터 전처리및 파생변수 생성
- 카드 데이터 전처리 
  - 매년, 10월 이후 카드 기록이 없는 고객을 기준으로 이탈여부 칼럼 생성
  - 승인건수 칼럼을 범주에서 수치로 변경, 월별 승인건수 평균을 구하여 승인건수 칼럼 생성
  - 고객 id당 월별 승인 금액 합계 칼럼 생성

- 커스터머 데이터 전처리
  - 자택_시도 칼럼에서 대구/경북 1로 그 외 지역은 0으로 설정
  - 수신_펀드/ 수신_외화예금 칼럼 제외
  - 수신_요구불예금, 수신_거치식예금, 수신_적립식예금 합하여 수신잔고 칼럼 생성
  - 수신잔고가 0이 아닐 경우 대출 대비 수신 비율 칼럼 생성
      - 대출 대비 수신 비율 = 대출 / 수신잔고 
  - 분석 대상을 20-30 지정
      - 이탈 비율이 가장 높았음 





