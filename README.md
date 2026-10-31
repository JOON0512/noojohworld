# Hojoon Lee — Systems & Architecture

이호준의 시스템·컴퓨터구조 프로젝트와 학습·튜터링 기록입니다.

**Site:** https://joon0512.github.io/noojohworld/

## Structure

네 가지 작업을 선별했습니다: proc-lens, gem5/Gshare 팀 프로젝트, xv6 실습, Zynq 보드 실습. 각각 질문, 접근, 관찰, 배운 점과 작업 범위를 담은 별도 페이지로 연결됩니다. 튜터링, 학업 배경, 짧은 연구실 학습 경험과 HAS도 소개합니다.

## Develop

Python 3만 있으면 HTML을 생성할 수 있습니다. 프런트엔드 패키지 설치는 필요하지 않습니다.

```sh
python3 scripts/build.py
python3 scripts/check.py
python3 -m http.server 8765 --bind 127.0.0.1 --directory docs
```

http://127.0.0.1:8765 에서 확인합니다.

- `scripts/build.py`: 소개 및 프로젝트 콘텐츠, 정적 HTML 템플릿, 개념도. 콘텐츠 수정 후 다시 실행합니다.
- `docs/style.css`: 레이아웃, 반응형, 다크 테마, 인쇄 스타일.
- `docs/app.js`: 테마 선택과 영상 표시. 기본 본문과 링크는 JavaScript 없이도 동작합니다.
- `docs/data/projects.json`: 빌드 시 생성되는 프로젝트 데이터 사본.
- `docs/data/videos.json`: YouTube 영상 등록 목록. 빌드 시 덮어쓰지 않습니다.
- `scripts/check.py`: HTML 제목 계층의 단일 h1, 중복 ID, 로컬 링크·앵커·자산 경로와 선별 프로젝트 데이터 점검.

영상 목록은 아래 형식입니다. `id`에는 실제 11자리 YouTube ID를 넣습니다. 목록이 비어 있으면 영상 영역 전체가 숨겨지며, 유효한 영상이 등록되면 튜터링 섹션 아래에 나타납니다. 개인정보 보호 강화 모드인 `youtube-nocookie.com`을 사용합니다.

```json
[{"id":"VIDEO_ID_11","title":"운영체제론 튜터링 제목"}]
```

Google Fonts에서 DM Sans와 IBM Plex Mono를 불러옵니다. 연결되지 않으면 시스템 글꼴로 표시됩니다.

## Deploy

GitHub Pages: `main` branch, `/docs` directory. 빌드된 HTML도 커밋하므로 별도 서버나 애플리케이션 빌드 서비스 없이 배포됩니다. 이전 `noojohojoon/` 폴더는 과거 작업 보관용이며 Pages 폴더에 포함되지 않습니다.

## Editorial scope

현재 학부 재학 상태와 관심 분야를 중심으로 구성했습니다. 개인 학습, 수업, 팀 프로젝트, 학부 연구 참여를 구분하고 검증되지 않은 성능 개선율은 넣지 않았습니다. 개념도는 설명을 위해 직접 구성한 그림이며 측정 결과가 아닙니다. 프로젝트의 세부 검증 범위는 각 페이지와 공개 저장소에 안내합니다.

## References reviewed for the redesign

20개 홈페이지의 본문·정보 구조를 검토하고, 주요 비교 대상의 브라우저 레이아웃도 확인했습니다. 타 사이트의 문구·이미지·소스는 복제하지 않았습니다.

1. [Dohyun Kim](https://dohyunkim02-portfolio.netlify.app/) — 분야와 프로젝트 역할을 앞에 제시
2. [Jihwan Park](https://aptheparker.work/en) — 소개에서 경력·선별 작업으로 이어지는 구조
3. [kdy1](https://kdy1.dev/) — 실제 작업 기록 중심
4. [Andrej Karpathy](https://karpathy.ai/) — 프로젝트와 교육 연결
5. [Julia Evans](https://jvns.ca/) — 주제별 기술 학습 기록
6. [Brittany Chiang](https://brittanychiang.com/) — 명확한 역할과 프로젝트 설명
7. [Lee Robinson](https://leerob.com/) — 짧은 소개에서 깊은 내용으로
8. [Anthony Fu](https://antfu.me/) — 프로젝트별 역할 구분
9. [Guillermo Rauch](https://rauchg.com/) — 간결한 글 인덱스
10. [Josh W. Comeau](https://www.joshwcomeau.com/) — 무엇을 배울지 알려주는 설명
11. [Tania Rascia](https://www.taniarascia.com/) — 글·프로젝트·소스의 연결
12. [Simon Willison](https://simonwillison.net/) — 실제 기술 기록과 자료 링크
13. [Lilian Weng](https://lilianweng.github.io/) — 읽기 중심의 기술 글 구조
14. [Sebastian Raschka](https://sebastianraschka.com/) — 주요 교육·기술 자료의 진입점
15. [Dan Luu](https://danluu.com/) — 기술 내용에 집중한 링크 목록
16. [Brian Lovin](https://brianlovin.com/) — 한 줄 프로젝트 설명
17. [Paco Coursey](https://paco.me/) — 현재 관심과 작업의 간결한 섹션
18. [Emil Kowalski](https://emilkowal.ski/) — 짧은 내용과 충분한 여백
19. [Arun Venkatesan](https://arun.is/) — 개인 배경과 일의 정돈된 구분
20. [Maggie Appleton](https://maggieappleton.com/) — 시각적 설명과 탐구 기록
