import { useEffect, useMemo, useState } from "react";

const GAME_SECONDS = 30;
const BOARD_SIZE = 16;

function getRandomIndex(excludeIndex = -1) {
  let nextIndex = Math.floor(Math.random() * BOARD_SIZE);

  while (nextIndex === excludeIndex) {
    nextIndex = Math.floor(Math.random() * BOARD_SIZE);
  }

  return nextIndex;
}

export default function App() {
  const [score, setScore] = useState(0);
  const [timeLeft, setTimeLeft] = useState(GAME_SECONDS);
  const [isPlaying, setIsPlaying] = useState(true);
  const [thiefIndex, setThiefIndex] = useState(() => getRandomIndex());

  const citizens = useMemo(
    () => ["🧑", "👩", "👨", "👵", "👴", "🧒", "👮", "🧑‍🍳"],
    []
  );

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
    <main className="app">
      <section className="game-shell" aria-label="도둑잡기 게임">
        <div className="topbar">
          <div>
            <p className="eyebrow">Team 5 Mini Game</p>
            <h1>도둑잡기</h1>
          </div>
          <button className="restart-button" type="button" onClick={restartGame}>
            다시 시작
          </button>
        </div>

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
      </section>
    </main>
  );
}
