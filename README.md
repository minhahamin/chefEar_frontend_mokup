# ChefEar Frontend Mockup

ChefEar 서비스의 화면 프로토타입 저장소다. 백엔드(`orchestration.pipeline`, `stt/infer.py`,
`tts/infer.py`)가 아직 미완성인 상태에서, 화면 디자인과 흐름만 먼저 눈으로 확인·시연할 수 있도록
가짜 데이터로 만든 목업이다. 같은 화면 12개를 **HTML**과 **Streamlit(Python)** 두 형식으로
각각 구현했다.

자세한 내용은 [ui/README.md](ui/README.md)를 참고한다.

## 폴더 구조

```
ui/
  app.py                    # Streamlit 진입점(라우터)
  nav.py                    # 화면 전환 헬퍼
  theme.py                  # 공통 CSS + 배지/칩/대화로그 렌더 헬퍼
  mock_data.py               # 가짜 레시피 데이터
  streamlit_screens/         # 화면별 render() 모듈 12개
  html/
    01_start.html ~ 11_unclassified.html, 12_cooking_complete.html
    flowmap.html            # 전체 화면 지도(포트폴리오용 인덱스)
    assets/style.css        # 공통 디자인 토큰 + 스타일
```

## 빠르게 보기

**HTML 버전** — 서버·빌드 없이 파일을 바로 열면 된다.

- 화면 하나씩: [ui/html/01_start.html](ui/html/01_start.html)
- 전체 지도: [ui/html/flowmap.html](ui/html/flowmap.html)

**Streamlit 버전** — 실제로 상태가 바뀌는(단계 이동, 재료 대체, 레시피 교체 등) 인터랙티브 버전이다.

```
pip install streamlit
streamlit run ui/app.py
```

## 화면 목록 (12개)

| 순서 | 화면 | 대응 요구사항 |
| --- | --- | --- |
| 01 | 시작 (자유발화 유도) | FR-01 |
| 02 | 레시피 확인 (표준 레시피 자동 채택) | FR-05 |
| 03 | 조리 진행 (메인 화면) | FR-02, FR-03, 3.3 |
| 12 | 조리 완성 (마지막 단계 완료 축하, 저장 완료와는 별개) | FR-02, FR-03 |
| 04 | 재료 대체 제안 확인 | FR-04 ①, 시나리오 B |
| 05 | 매칭 실패 정직 안내 | FR-04 ③, 시나리오 C |
| 06 | 신규 등록 제안 | FR-06, 시나리오 D |
| 07 | 신규 등록 1/3 — 요리명 | FR-06 |
| 08 | 신규 등록 2/3 — 재료 + 확인 체크포인트 | FR-06 |
| 09 | 신규 등록 3/3 — 순서 + 최종 확인 체크포인트 | FR-06 |
| 10 | 완료 (원본 보존 + user_custom 저장) | FR-08 |
| 11 | 음성 인식/의도분류 실패 Fallback | FR-16, AC-02/AC-09 |

자세한 화면별 동작, 데이터 근거, 검증 상태는 [ui/README.md](ui/README.md)에 정리되어 있다.
