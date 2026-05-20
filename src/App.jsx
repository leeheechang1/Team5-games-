import { useEffect, useMemo, useState } from "react";

const GAME_SECONDS = 30;
const BOARD_SIZE = 16;

const NEWS_QUESTIONS = [
  { headline: "삼성전자, 엔비디아 인수 추진", fake: true },
  { headline: "주식 앱 설치만 하면 매일 수익률 100% 보장", fake: true },
  { headline: "현대차, 전기차 배터리 연구 인력 추가 채용", fake: false },
  { headline: "SK하이닉스, 메모리 반도체 수요 회복 기대감에 주가 강세", fake: false },
  { headline: "카카오, 메신저 이용자에게 주식 1주씩 무상 지급", fake: true },
  { headline: "LG에너지솔루션, 생산 라인 효율 개선 투자 검토", fake: false },
  { headline: "한국거래소, 내일부터 모든 주식 가격을 2배로 변경", fake: true },
  { headline: "삼성바이오로직스, 위탁생산 계약 체결 소식에 상승", fake: false },
  { headline: "삼성전자 주식, 오늘부터 편의점에서 현금처럼 사용 가능", fake: true },
  { headline: "LG전자, 가전 구독 서비스 지역 확대", fake: false },
  { headline: "정부, 모든 개인 투자자 손실을 전액 보상 결정", fake: true },
  { headline: "삼성SDI, 차세대 배터리 개발 연구 지속", fake: false },
  { headline: "한 주만 사면 평생 월급 지급하는 종목 등장", fake: true },
  { headline: "SK텔레콤, AI 서비스 고도화 계획 공개", fake: false },
  { headline: "삼성전자, 반도체 공장에 우주 엘리베이터 설치", fake: true },
  { headline: "CJ제일제당, 해외 식품 매출 확대 전략 발표", fake: false },
  { headline: "주식 10주를 사면 회사 대표가 집으로 방문", fake: true },
  { headline: "대한항공, 국제선 운항 스케줄 일부 조정", fake: false },
  { headline: "코스닥 전 종목, 오늘 오후 3시에 동시에 상한가 예정", fake: true },
  { headline: "HMM, 해상 운임 지표 변화에 주가 등락", fake: false }
];

function getRandomIndex(excludeIndex = -1) {
  let nextIndex = Math.floor(Math.random() * BOARD_SIZE);

  while (nextIndex === excludeIndex) {
    nextIndex = Math.floor(Math.random() * BOARD_SIZE);
  }

  return nextIndex;
}

function shuffleItems(items) {
  return [...items].sort(() => Math.random() - 0.5);
}

function getInitialGame() {
  const path = window.location.pathname.toLowerCase();
  const hash = window.location.hash.toLowerCase();

  if (path.includes("fake-news") || hash.includes("news")) {
    return "news";
  }

  return "thief";
}

function ThiefGame() {
  const [score, setScore] = useState(0);
  const [timeLeft, setTimeLeft] = useState(GAME_SECONDS);
  const [isPlaying, setIsPlaying] = useState(true);
  const [thiefIndex, setThiefIndex] = useState(() => getRandomIndex());

  const citizens = useMemo(() => ["🙂", "😐", "😎", "🧑", "👩", "👨", "👵", "👴"], []);

  useEffect(() => {
    if (!isPlaying) {
      return undefined;
    }

    const timerId = window.setInterval(() => {
      setTimeLeft((current) => {
        if (current <= 1) {
          setIsPlaying(false);
          return 0;
        }

        return current - 1;
      });
    }, 1000);

    return () => window.clearInterval(timerId);
  }, [isPlaying]);

  useEffect(() => {
    if (!isPlaying) {
      return undefined;
    }

    const moveId = window.setInterval(() => {
      setThiefIndex((current) => getRandomIndex(current));
    }, 850);

    return () => window.clearInterval(moveId);
  }, [isPlaying]);

  function handleTileClick(index) {
    if (!isPlaying) {
      return;
    }

    if (index === thiefIndex) {
      setScore((current) => current + 1);
      setThiefIndex((current) => getRandomIndex(current));
      return;
    }

    setScore((current) => current - 1);
  }

  function restartGame() {
    setScore(0);
    setTimeLeft(GAME_SECONDS);
    setThiefIndex(getRandomIndex());
    setIsPlaying(true);
  }

  return (
    <>
      <div className="score-panel">
        <div>
          <span>남은 시간</span>
          <strong>{timeLeft}s</strong>
        </div>
        <div>
          <span>점수</span>
          <strong>{score}</strong>
        </div>
        <div>
          <span>상태</span>
          <strong>{isPlaying ? "진행 중" : "종료"}</strong>
        </div>
      </div>

      <div className="board" role="grid" aria-label="도둑을 찾아 클릭하세요">
        {Array.from({ length: BOARD_SIZE }).map((_, index) => {
          const isThief = index === thiefIndex;
          const citizen = citizens[index % citizens.length];

          return (
            <button
              className={`tile ${isThief ? "thief" : "citizen"}`}
              key={index}
              type="button"
              onClick={() => handleTileClick(index)}
              disabled={!isPlaying}
              aria-label={isThief ? "도둑" : "시민"}
            >
              <span>{isThief ? "🕵️" : citizen}</span>
            </button>
          );
        })}
      </div>

      {!isPlaying && (
        <div className="result" role="status">
          <p>게임 종료</p>
          <strong>최종 점수: {score}</strong>
          <button type="button" onClick={restartGame}>
            다시 시작
          </button>
        </div>
      )}
    </>
  );
}

function FakeNewsGame() {
  const [questions, setQuestions] = useState(() => shuffleItems(NEWS_QUESTIONS).slice(0, 10));
  const [currentIndex, setCurrentIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [selected, setSelected] = useState(null);
  const [isDone, setIsDone] = useState(false);

  const currentQuestion = questions[currentIndex];

  function answer(userSaysFake) {
    if (selected !== null || isDone) {
      return;
    }

    setSelected(userSaysFake);

    if (userSaysFake === currentQuestion.fake) {
      setScore((current) => current + 1);
    }
  }

  function nextQuestion() {
    if (currentIndex >= questions.length - 1) {
      setIsDone(true);
      return;
    }

    setCurrentIndex((current) => current + 1);
    setSelected(null);
  }

  function restartGame() {
    setQuestions(shuffleItems(NEWS_QUESTIONS).slice(0, 10));
    setCurrentIndex(0);
    setScore(0);
    setSelected(null);
    setIsDone(false);
  }

  if (isDone) {
    return (
      <div className="news-card result-card">
        <p>판별 완료</p>
        <strong>최종 점수: {score}/{questions.length}</strong>
        <button type="button" onClick={restartGame}>
          다시 시작
        </button>
      </div>
    );
  }

  const isCorrect = selected === currentQuestion.fake;

  return (
    <section className="news-card" aria-label="주식 가짜 뉴스 판별게임">
      <div className="news-meta">
        <span>
          문제 {currentIndex + 1}/{questions.length}
        </span>
        <strong>점수 {score}</strong>
      </div>

      <h2>{currentQuestion.headline}</h2>

      <div className="answer-grid">
        <button type="button" onClick={() => answer(false)} disabled={selected !== null}>
          진짜 뉴스
        </button>
        <button type="button" onClick={() => answer(true)} disabled={selected !== null}>
          가짜 뉴스
        </button>
      </div>

      {selected !== null && (
        <div className={`feedback ${isCorrect ? "correct" : "wrong"}`}>
          <strong>{isCorrect ? "정답입니다!" : "오답입니다."}</strong>
          <p>정답: {currentQuestion.fake ? "가짜 뉴스" : "진짜 뉴스"}</p>
          <button type="button" onClick={nextQuestion}>
            다음 문제
          </button>
        </div>
      )}
    </section>
  );
}

export default function App() {
  const [game, setGame] = useState(() => getInitialGame());

  function changeGame(nextGame) {
    setGame(nextGame);
    window.history.replaceState(null, "", nextGame === "news" ? "#news" : "#thief");
  }

  return (
    <main className="app">
      <section className="game-shell" aria-label="Team 5 웹게임">
        <div className="topbar">
          <div>
            <p className="eyebrow">Team 5 Mini Game</p>
            <h1>{game === "thief" ? "도둑잡기" : "주식 가짜 뉴스"}</h1>
          </div>
        </div>

        <div className="mode-tabs" aria-label="게임 선택">
          <button
            className={game === "thief" ? "active" : ""}
            type="button"
            onClick={() => changeGame("thief")}
          >
            도둑잡기
          </button>
          <button
            className={game === "news" ? "active" : ""}
            type="button"
            onClick={() => changeGame("news")}
          >
            가짜 뉴스
          </button>
        </div>

        {game === "thief" ? <ThiefGame /> : <FakeNewsGame />}
      </section>
    </main>
  );
}
