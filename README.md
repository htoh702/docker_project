#여행 기록 일지 서비스(TravelLog) – Toy Project

개발 기간: 
2021.03.21 ~ 2021.03.28

개발환경: 
Docker, ngnix, HAproxy, Django, React, MySQL

개발 인원: 
4명

맡은 역할: 
Django를 활용한 백엔드 개발, MySQL을 이용한 데이터 모델 설계 및 구축, Docker를 이용한 Dockerfile 작성 및 Docker Compose 구성

내용 요약:
여행 중 방문한 장소를 기록하고 다른 사람과 공유할 수 있는 다이어리 서비스를 개발했습니다. 

---
<img width="219" alt="image" src="https://github.com/user-attachments/assets/9e52ca3e-0857-413b-a8f5-8fc8640cac66">
<img width="211" alt="image" src="https://github.com/user-attachments/assets/eab56208-ad95-448c-9920-b355f3ae0c65">


구성도

 <img width="313" alt="image" src="https://github.com/user-attachments/assets/44094d71-5b9e-4b31-9fa4-44dfecdf8de9">

-	Docker Compose를 활용하여 컨테이너들을 생성
-	Nginx, React, HAProxy, Django, MySQL 이미지를 사용하여 컨테이너를 생성
-	React와 Django 인스턴스를 각각 여러 개 생성하여 고가용성을 확보
-	Nginx는 React를, HAProxy는 Django를 로드밸런싱하도록 설계

