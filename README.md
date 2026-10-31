# Hojoon Lee — Build, Learn, Explain

이호준의 프로젝트·학습·튜터링 포트폴리오. GitHub Pages에서 제공하는 정적 사이트입니다.

## Local preview

```sh
python3 -m http.server 8765 --directory docs
```

http://localhost:8765 에서 확인합니다. `fetch`로 JSON을 읽으므로 HTML 파일을 직접 여는 대신 HTTP 서버를 사용합니다.

## Edit

- `docs/index.html`: 소개, 학력, 튜터링, 연락 링크
- `docs/data/projects.json`: 프로젝트 제목, 분류, 기술, 설명, 작업 범위, 공개 코드 링크
- `docs/data/videos.json`: YouTube 영상. 형식: `[{"id":"11자리영상ID","title":"영상 제목"}]`
- `docs/style.css`: 화면·반응형·다크 테마
- `docs/app.js`: 검색·필터·상세 보기·영상 연결

코드 링크가 없는 프로젝트도 소개할 수 있습니다. 영상 배열이 비어 있으면 준비 안내를 표시합니다. 영상 ID는 11자리 YouTube ID만 허용하며 iframe은 youtube-nocookie.com을 사용합니다.

## GitHub Pages

Settings → Pages → Deploy from a branch → `main` / `/docs`.
배포 주소: https://joon0512.github.io/noojohworld/

표시 이름은 새 브랜드로 개편했으며 기존 링크 유지를 위해 저장소 이름은 유지합니다.
기존 `noojohojoon/`은 과거 작업 보관용이며 Pages 배포 폴더에 포함하지 않습니다.

## Content

프로젝트 공개 README와 로컬 경험 정리 기록을 바탕으로 소개를 작성했습니다. 연구·학습·수업·AI 협업·진행 중 작업을 구분하고 확인되지 않은 성능 수치는 기재하지 않았습니다. 연구실 데이터, 증명서, 연락처 원장, 타인의 개인정보는 포함하지 않습니다.

구성 참고: [Andrej Karpathy](https://karpathy.ai/)의 프로젝트·교육 연결, [Julia Evans](https://jvns.ca/)의 주제별 학습 기록. 디자인과 문구는 이 사이트를 위해 작성했습니다.
