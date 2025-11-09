TIL - Django & Bootstrap 프로젝트 구현

날짜

2025년 11월 9일

⸻

오늘의 학습 내용

오늘은 Django를 이용해 명세서 기반의 웹 서비스를 구현하고, Bootstrap을 적용하여 페이지를 시각적으로 구성하였다.
기존의 단순한 CRUD 기능에서 벗어나, Bootstrap 컴포넌트를 활용해 레이아웃과 디자인을 개선하면서 실제 서비스와 유사한 형태의 결과물을 만들어냈다.

⸻

학습 과정 요약
	1.	Django 기본 세팅
	•	가상환경 생성 및 Django 설치
	•	mypjt, books 앱 생성 및 settings.py 설정
	•	모델 설계 후 makemigrations, migrate 실행
	2.	CRUD 기능 구현
	•	Book과 Thread 모델을 중심으로 데이터 등록, 조회, 수정, 삭제 기능 구현
	•	@require_http_methods, @require_POST를 이용한 HTTP 메서드 제어 적용
	3.	Bootstrap 연동
	•	base.html에 Bootstrap CDN 추가
	•	Navbar, 버튼, 테이블 등 UI 구성 요소를 활용하여 전체 페이지 통일성 확보
	4.	템플릿 구조 설계
	•	base.html → 공통 레이아웃
	•	index.html, create.html, detail.html 등 개별 페이지 확장

⸻

느낀 점

지금까지 배웠던 Django와 Bootstrap을 연결해 직접 웹 페이지를 구성하는 과정이 매우 흥미로웠다.
단순히 서버 로직만 다루던 단계에서 벗어나, 실제 서비스처럼 화면을 꾸미고 데이터를 주고받는 작업을 하니
내가 만든 웹사이트가 진짜로 돌아간다라는 실감이 났다.

앞으로 배운 기술을 바탕으로 자신만의 아이디어를 적용한 웹 서비스를 만들어 나갈 과정이 기대된다.

다음 목표
	•	Bootstrap 컴포넌트를 다양하게 적용해 반응형 디자인 구현
	•	도전 기능(API 연동, 생성형 AI 활용 등) 적용
	•	사용자 경험(UX)을 고려한 인터페이스 개선

