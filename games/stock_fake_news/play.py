import random


QUESTIONS = [
    {"headline": "삼성전자, 엔비디아 인수 추진", "is_fake": True, "reason": "초대형 인수 뉴스는 공식 공시나 주요 언론 확인 없이 믿기 어렵습니다."},
    {"headline": "네이버, 다음 달부터 모든 검색 결과를 유료화", "is_fake": True, "reason": "서비스 전체 유료화처럼 큰 변화는 공식 발표 확인이 필요합니다."},
    {"headline": "카카오, 메신저 이용자에게 주식 1주씩 무상 지급", "is_fake": True, "reason": "이용자 전체에게 주식을 지급한다는 내용은 현실성이 낮습니다."},
    {"headline": "현대차, 전기차 배터리 연구 인력 추가 채용", "is_fake": False, "reason": "기업의 연구 인력 채용은 충분히 가능한 일반적인 뉴스입니다."},
    {"headline": "LG에너지솔루션, 생산 라인 효율 개선 투자 검토", "is_fake": False, "reason": "설비 투자 검토는 기업 뉴스에서 자주 나오는 정상적인 형태입니다."},
    {"headline": "SK하이닉스, 메모리 반도체 수요 회복 기대감에 주가 강세", "is_fake": False, "reason": "수요 전망과 주가 움직임을 연결한 일반적인 증시 기사입니다."},
    {"headline": "셀트리온, 감기약 하나로 모든 암 치료 성공", "is_fake": True, "reason": "모든 암 치료처럼 과장된 표현은 가짜 뉴스 가능성이 큽니다."},
    {"headline": "삼성전자, 새 스마트폰 공개 행사 일정 발표", "is_fake": False, "reason": "신제품 공개 일정 발표는 정상적인 기업 뉴스입니다."},
    {"headline": "기아, 중형 전기 SUV 해외 판매 확대 추진", "is_fake": False, "reason": "해외 판매 확대는 자동차 기업에서 자연스러운 뉴스입니다."},
    {"headline": "포스코홀딩스, 리튬 사업 관련 투자 계획 점검", "is_fake": False, "reason": "사업 투자 계획 점검은 충분히 가능한 내용입니다."},
    {"headline": "한국거래소, 내일부터 모든 주식 가격을 2배로 변경", "is_fake": True, "reason": "시장 전체 가격을 임의로 2배 변경하는 일은 불가능에 가깝습니다."},
    {"headline": "삼성바이오로직스, 위탁생산 계약 체결 소식에 상승", "is_fake": False, "reason": "계약 체결에 따른 주가 반응은 일반적인 기사입니다."},
    {"headline": "두산로보틱스, 협동로봇 신제품 전시회 참가", "is_fake": False, "reason": "전시회 참가와 신제품 소개는 정상적인 기업 활동입니다."},
    {"headline": "엔씨소프트, 게임 업데이트 일정 공개", "is_fake": False, "reason": "게임사 업데이트 일정 공개는 흔한 뉴스입니다."},
    {"headline": "하이브, 아이돌 팬 전원에게 배당금 지급", "is_fake": True, "reason": "주주가 아닌 팬에게 배당금을 지급한다는 내용은 맞지 않습니다."},
    {"headline": "대한항공, 국제선 운항 스케줄 일부 조정", "is_fake": False, "reason": "항공편 스케줄 조정은 현실적인 뉴스입니다."},
    {"headline": "쿠팡, 물류센터 자동화 설비 추가 도입", "is_fake": False, "reason": "물류 자동화 설비 도입은 기업 전략으로 자연스럽습니다."},
    {"headline": "아모레퍼시픽, 신제품 출시 후 온라인 판매 강화", "is_fake": False, "reason": "화장품 기업의 신제품 및 판매 채널 강화는 정상적입니다."},
    {"headline": "삼성전자 주식, 오늘부터 편의점에서 현금처럼 사용 가능", "is_fake": True, "reason": "상장 주식을 편의점 결제수단으로 바로 쓰는 것은 사실성이 낮습니다."},
    {"headline": "롯데케미칼, 원재료 가격 변동에 수익성 관리 강화", "is_fake": False, "reason": "원가와 수익성 관리는 기업 실적 기사에서 흔합니다."},
    {"headline": "LG전자, 가전 구독 서비스 지역 확대", "is_fake": False, "reason": "서비스 지역 확대는 일반적인 사업 뉴스입니다."},
    {"headline": "한화에어로스페이스, 방산 수주 기대감에 관심", "is_fake": False, "reason": "수주 기대감은 증시 기사에서 자주 쓰입니다."},
    {"headline": "카카오뱅크, 모바일 앱 기능 개편", "is_fake": False, "reason": "은행 앱 기능 개편은 충분히 가능한 뉴스입니다."},
    {"headline": "정부, 모든 개인 투자자 손실을 전액 보상 결정", "is_fake": True, "reason": "투자 손실 전액 보상은 현실성이 매우 낮고 공식 확인이 필요합니다."},
    {"headline": "삼성SDI, 차세대 배터리 개발 연구 지속", "is_fake": False, "reason": "배터리 연구 개발은 업종 특성상 자연스러운 내용입니다."},
    {"headline": "현대모비스, 자율주행 부품 기술 전시", "is_fake": False, "reason": "자동차 부품사의 기술 전시는 정상적인 뉴스입니다."},
    {"headline": "주식 앱 설치만 하면 매일 수익률 100% 보장", "is_fake": True, "reason": "수익률 보장은 투자 사기성 문구일 가능성이 큽니다."},
    {"headline": "KB금융, 주주환원 정책 검토 소식", "is_fake": False, "reason": "금융사의 주주환원 정책 검토는 가능한 뉴스입니다."},
    {"headline": "신한지주, 금리 환경 변화에 실적 전망 주목", "is_fake": False, "reason": "금리와 금융주 실적은 연결성이 있습니다."},
    {"headline": "삼성전자, 반도체 공장에 우주 엘리베이터 설치", "is_fake": True, "reason": "우주 엘리베이터 설치는 현실적 기업 뉴스가 아닙니다."},
    {"headline": "CJ제일제당, 해외 식품 매출 확대 전략 발표", "is_fake": False, "reason": "해외 매출 확대 전략은 일반적인 기업 뉴스입니다."},
    {"headline": "오리온, 신제품 과자 출시 후 편의점 판매 시작", "is_fake": False, "reason": "식품 신제품 출시와 유통은 정상적입니다."},
    {"headline": "LG화학, 친환경 소재 사업 투자 확대 검토", "is_fake": False, "reason": "친환경 소재 투자는 화학 기업에서 가능한 방향입니다."},
    {"headline": "한국전력, 전기요금 관련 정책 변화에 주가 변동", "is_fake": False, "reason": "정책 변화는 공기업 주가에 영향을 줄 수 있습니다."},
    {"headline": "두산에너빌리티, 발전 설비 수주 기대감 부각", "is_fake": False, "reason": "발전 설비 수주는 해당 업종의 주요 뉴스입니다."},
    {"headline": "한미약품, 임상시험 결과 발표 일정 안내", "is_fake": False, "reason": "제약사의 임상 일정 안내는 정상적인 공시성 뉴스입니다."},
    {"headline": "넷마블, 모든 유저 계정을 주식 계좌로 전환", "is_fake": True, "reason": "게임 계정을 주식 계좌로 바꾼다는 내용은 비현실적입니다."},
    {"headline": "삼성물산, 건설 프로젝트 수주 소식에 관심", "is_fake": False, "reason": "건설 수주는 기업 가치에 영향을 줄 수 있는 일반 뉴스입니다."},
    {"headline": "HD현대중공업, 선박 수주 협상 진행", "is_fake": False, "reason": "조선사의 선박 수주 협상은 현실적인 뉴스입니다."},
    {"headline": "에코프로, 2차전지 소재 시장 전망에 주가 등락", "is_fake": False, "reason": "시장 전망에 따른 주가 등락은 일반적인 기사입니다."},
    {"headline": "한 주만 사면 평생 월급 지급하는 종목 등장", "is_fake": True, "reason": "평생 월급 보장처럼 과도한 약속은 가짜 뉴스 가능성이 큽니다."},
    {"headline": "SK텔레콤, AI 서비스 고도화 계획 공개", "is_fake": False, "reason": "통신사의 AI 서비스 강화는 충분히 가능한 뉴스입니다."},
    {"headline": "KT, 데이터센터 사업 협력 확대", "is_fake": False, "reason": "데이터센터 사업 협력은 통신사 사업과 관련이 있습니다."},
    {"headline": "LG유플러스, 기업용 통신 서비스 상품 개편", "is_fake": False, "reason": "기업용 서비스 개편은 정상적인 영업 뉴스입니다."},
    {"headline": "삼성전자, 주가가 오르면 자동으로 스마트폰 무료 지급", "is_fake": True, "reason": "주가 상승과 제품 무료 지급은 직접 관련이 없습니다."},
    {"headline": "현대글로비스, 물류 운임 변화에 실적 전망 관심", "is_fake": False, "reason": "운임 변화는 물류 기업 실적에 영향을 줄 수 있습니다."},
    {"headline": "호텔신라, 면세점 수요 회복 기대감 부각", "is_fake": False, "reason": "면세 수요 회복은 관련 기업 기사로 자연스럽습니다."},
    {"headline": "강원랜드, 방문객 증가 기대에 주가 변동", "is_fake": False, "reason": "방문객 수는 실적과 관련될 수 있습니다."},
    {"headline": "모든 코스피 기업, 내일부터 이름을 삼성으로 통일", "is_fake": True, "reason": "상장사 이름을 일괄 통일하는 것은 불가능합니다."},
    {"headline": "유한양행, 신약 후보물질 연구 결과 발표", "is_fake": False, "reason": "신약 연구 결과 발표는 제약사에서 가능한 뉴스입니다."},
    {"headline": "삼성전기, 전장용 부품 수요 증가 기대", "is_fake": False, "reason": "전장용 부품 수요는 전자부품 기업과 관련이 있습니다."},
    {"headline": "카카오페이, 결제 서비스 편의 기능 추가", "is_fake": False, "reason": "핀테크 기업의 서비스 기능 추가는 일반적입니다."},
    {"headline": "미래에셋증권, 해외주식 거래 서비스 개선", "is_fake": False, "reason": "증권사의 거래 서비스 개선은 정상적입니다."},
    {"headline": "증권사 직원이 말한 종목은 무조건 상한가 확정", "is_fake": True, "reason": "상한가 확정처럼 단정적인 표현은 위험합니다."},
    {"headline": "삼성전자, 반도체 재고 조정 마무리 기대감", "is_fake": False, "reason": "재고 조정과 업황 전망은 반도체 기사에서 흔합니다."},
    {"headline": "LG디스플레이, OLED 패널 공급 확대 기대", "is_fake": False, "reason": "디스플레이 공급 확대는 업종과 잘 맞는 뉴스입니다."},
    {"headline": "현대로템, 철도 차량 수주 관련 협상 진행", "is_fake": False, "reason": "철도 차량 수주는 해당 기업의 일반적인 사업입니다."},
    {"headline": "한국조선해양, 친환경 선박 수요 증가 기대", "is_fake": False, "reason": "친환경 선박 수요는 조선업 관련 주요 이슈입니다."},
    {"headline": "주식 시장, 내일부터 점심시간마다 수익률 추첨 지급", "is_fake": True, "reason": "거래소가 수익률을 추첨 지급한다는 내용은 비현실적입니다."},
    {"headline": "농심, 라면 수출 증가 기대감에 관심", "is_fake": False, "reason": "식품 수출 증가는 기업 실적과 연결될 수 있습니다."},
    {"headline": "삼양식품, 해외 판매 호조 소식에 주가 강세", "is_fake": False, "reason": "해외 판매 호조와 주가 반응은 일반적인 기사입니다."},
    {"headline": "BGF리테일, 편의점 신사업 테스트 운영", "is_fake": False, "reason": "편의점 기업의 신사업 테스트는 가능한 뉴스입니다."},
    {"headline": "이마트, 온라인 배송 서비스 개편", "is_fake": False, "reason": "유통사의 배송 서비스 개편은 정상적입니다."},
    {"headline": "주식 10주를 사면 회사 대표가 집으로 방문", "is_fake": True, "reason": "주식 매수 혜택으로 대표 방문은 현실성이 낮습니다."},
    {"headline": "대한전선, 전력망 투자 확대 기대감", "is_fake": False, "reason": "전력망 투자는 전선 기업과 관련된 이슈입니다."},
    {"headline": "LS ELECTRIC, 전력기기 수요 증가 전망", "is_fake": False, "reason": "전력기기 수요 전망은 해당 기업 기사로 자연스럽습니다."},
    {"headline": "코웨이, 렌털 계정 증가에 실적 기대", "is_fake": False, "reason": "렌털 계정 증가는 렌털 기업 실적과 관련이 있습니다."},
    {"headline": "한샘, 주거 인테리어 수요 변화에 전략 조정", "is_fake": False, "reason": "수요 변화에 따른 전략 조정은 일반적인 기업 뉴스입니다."},
    {"headline": "삼성전자 주식 보유자는 지하철 무료 탑승 가능", "is_fake": True, "reason": "주식 보유와 공공요금 무료 혜택은 관련성이 없습니다."},
    {"headline": "제주항공, 여행 수요 회복 기대에 주가 변동", "is_fake": False, "reason": "여행 수요는 항공주에 영향을 줄 수 있습니다."},
    {"headline": "진에어, 국제선 노선 운항 확대 검토", "is_fake": False, "reason": "항공사의 노선 확대 검토는 정상적인 뉴스입니다."},
    {"headline": "에스엠, 아티스트 활동 일정 공개", "is_fake": False, "reason": "엔터사의 활동 일정 공개는 일반적인 뉴스입니다."},
    {"headline": "JYP Ent., 해외 공연 일정 확대 기대감", "is_fake": False, "reason": "해외 공연 일정은 엔터사 실적과 연결될 수 있습니다."},
    {"headline": "연예인 이름이 들어간 주식은 무조건 10배 상승", "is_fake": True, "reason": "무조건 상승 같은 표현은 신뢰하기 어렵습니다."},
    {"headline": "HMM, 해상 운임 지표 변화에 주가 등락", "is_fake": False, "reason": "해상 운임은 해운주에 직접적인 영향을 줄 수 있습니다."},
    {"headline": "팬오션, 벌크선 시황 회복 기대감", "is_fake": False, "reason": "벌크선 시황은 해운 기업과 관련이 있습니다."},
    {"headline": "현대백화점, 소비 심리 회복 여부 주목", "is_fake": False, "reason": "소비 심리는 백화점 실적과 연결됩니다."},
    {"headline": "신세계, 면세점과 백화점 매출 흐름 관심", "is_fake": False, "reason": "매출 흐름은 유통 기업 기사에서 자연스럽습니다."},
    {"headline": "코스닥 전 종목, 오늘 오후 3시에 동시에 상한가 예정", "is_fake": True, "reason": "모든 종목의 상한가를 예정한다는 말은 불가능합니다."},
    {"headline": "펄어비스, 신작 게임 출시 일정 기대감", "is_fake": False, "reason": "게임사의 신작 일정은 투자자 관심 뉴스입니다."},
    {"headline": "컴투스, 모바일 게임 업데이트 효과 주목", "is_fake": False, "reason": "업데이트 효과는 게임사 실적과 관련될 수 있습니다."},
    {"headline": "레인보우로보틱스, 로봇 자동화 수요 확대 기대", "is_fake": False, "reason": "로봇 자동화 수요는 관련 기업 기사로 자연스럽습니다."},
    {"headline": "로봇 주식 매수자는 집안일 로봇을 무료 제공", "is_fake": True, "reason": "주식 매수와 제품 무료 제공은 일반적인 주주 혜택이 아닙니다."},
    {"headline": "한화솔루션, 태양광 시장 회복 기대감", "is_fake": False, "reason": "태양광 시장 전망은 해당 기업에 영향을 줄 수 있습니다."},
    {"headline": "OCI홀딩스, 폴리실리콘 가격 변화에 관심", "is_fake": False, "reason": "원재료 가격은 관련 기업 실적과 연결됩니다."},
    {"headline": "롯데쇼핑, 점포 효율화 전략 추진", "is_fake": False, "reason": "점포 효율화는 유통 기업에서 가능한 전략입니다."},
    {"headline": "GS리테일, 편의점 신규 서비스 테스트", "is_fake": False, "reason": "편의점 신규 서비스 테스트는 정상적인 뉴스입니다."},
    {"headline": "내일부터 주식 매수 버튼을 많이 누르면 가격 상승", "is_fake": True, "reason": "버튼 클릭 횟수만으로 가격이 오르지는 않습니다."},
    {"headline": "삼성생명, 보험 영업 환경 변화에 실적 전망 관심", "is_fake": False, "reason": "보험 영업 환경은 보험사 실적과 관련됩니다."},
    {"headline": "DB손해보험, 손해율 개선 기대감", "is_fake": False, "reason": "손해율은 보험사 실적의 주요 지표입니다."},
    {"headline": "기업은행, 중소기업 대출 수요 변화 주목", "is_fake": False, "reason": "대출 수요는 은행 실적과 관련이 있습니다."},
    {"headline": "우리금융지주, 배당 정책 변화 가능성에 관심", "is_fake": False, "reason": "금융지주의 배당 정책은 투자자 관심사입니다."},
    {"headline": "은행주 보유자는 은행 창구에서 줄 서지 않아도 됨", "is_fake": True, "reason": "주식 보유와 창구 이용 혜택은 직접 관련이 없습니다."},
    {"headline": "현대제철, 철강 수요 회복 기대감", "is_fake": False, "reason": "철강 수요는 철강사 실적과 연결됩니다."},
    {"headline": "고려아연, 금속 가격 변동에 주가 움직임", "is_fake": False, "reason": "금속 가격은 비철금속 기업 실적과 관련됩니다."},
    {"headline": "금호석유, 합성고무 수요 전망 주목", "is_fake": False, "reason": "제품 수요 전망은 화학 기업 기사로 자연스럽습니다."},
    {"headline": "S-Oil, 국제 유가 변동에 실적 전망 관심", "is_fake": False, "reason": "유가 변동은 정유사 실적과 연결됩니다."},
    {"headline": "주유소에서 S-Oil 주식으로 바로 기름값 결제 가능", "is_fake": True, "reason": "주식을 일반 결제수단처럼 바로 쓰는 것은 사실성이 낮습니다."},
    {"headline": "SK이노베이션, 배터리와 정유 사업 흐름 주목", "is_fake": False, "reason": "사업 부문별 흐름은 기업 분석 기사로 자연스럽습니다."},
    {"headline": "삼성전자, 화성에 반도체 공장 착공", "is_fake": True, "reason": "지구 밖 행성 공장 착공은 비현실적인 표현입니다."},
]


def ask_question(question_number, question):
    print()
    print(f"문제 {question_number}")
    print(question["headline"])
    print("1. 진짜 뉴스")
    print("2. 가짜 뉴스")

    while True:
        answer = input("선택하세요 (1/2): ").strip()
        if answer in ["1", "2"]:
            break
        print("1 또는 2를 입력하세요.")

    user_thinks_fake = answer == "2"
    is_correct = user_thinks_fake == question["is_fake"]

    if is_correct:
        print("정답입니다!")
    else:
        print("오답입니다.")

    print(f"해설: {question['reason']}")
    return is_correct


def play_game(question_count=10):
    question_count = min(question_count, len(QUESTIONS))
    selected_questions = random.sample(QUESTIONS, question_count)
    score = 0

    print()
    print("주식 가짜 뉴스 판별게임을 시작합니다.")
    print("이 게임의 뉴스 문장은 학습용 예시입니다. 실제 투자 판단에는 공식 공시를 확인하세요.")

    for index, question in enumerate(selected_questions, start=1):
        if ask_question(index, question):
            score += 1

    print()
    print(f"최종 점수: {score}/{question_count}")
    return score


def start_game(player_info):
    print()
    print(f"[주식 가짜 뉴스 판별게임] {player_info['name']}님, 게임을 시작합니다!")

    score = play_game()
    reward = score * 5
    player_info["chips"] += reward

    print(f"보상으로 칩 {reward}개를 얻었습니다.")
    print(f"현재 칩: {player_info['chips']}개")
    print("게임을 종료하고 로비로 돌아갑니다.")

    return player_info


def start_stock_fake_news(player_info):
    return start_game(player_info)


if __name__ == "__main__":
    test_player = {"name": "Player 1", "chips": 100}
    start_game(test_player)
