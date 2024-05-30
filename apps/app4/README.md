# Keycloak Full Stack Test

- SPA 웹 App 에 대한 Keycloack OIDC(Authorization Code Grant) 연동 테스트
- React Frontend (SPA) -> Python Backend 

## Settings

```bash
# Requirement
- Nodejs, Python 을 로컬 환경에 설치 및 vsCode 에 각 언어별 Debugger 설치 

# Python 필요 패키지 설치
$ pip install fastapi
$ pip install uvicorn
$ pip install python-dotenv
$ pip install pydantic
$ pip install python-keycloak

# Keycloak Client 생성
Settings
  General settings
    Client ID :  demo
  Access settings
    Root URL : http://localhost:3000/
    Valid redirect URIs : http://localhost:3000/*
    Web Origins : http://localhost:3000
    Admin URL : http://localhost:3000
  Capability config
  - Client authentication : OFF (public client)
  - Authentication flow : OFF
  - Authentication flow : Standard flow, Direct access grants

# frontend/backend .env 파일을 적절히 수정 

# 실행
Frontend: npm install && npm start
Backend: python main.py
```

## Test

```bash
# Step 1 > Frontend 앱 구동
cd frontend-react
npm install
npm start
Keycloak 로그인페이지 나옴
Keycloak 로그인하면 react index 화면 전환
F12 Console 열기
Request To Backend 버튼 클릭시 Keycloak access_token 을 얻는지 Console 탭에서 확인

# Step 2> Backend 앱 구동
cd backend_python
python main.py

# Step 3 > Frontend -> Backend 
F12 Console 열기
Request To Backend 버튼 클릭시 Keycloak access_token 을 사용하여 Backend (localhost:5000/secure) 에 Request 전달됨
Console 에 로그로 대략 아래와 같이 Backend 응답이 기록됨
{
  "message": "ID=b7f528f6-71b0-4c90-bb01-603bf0456cbb, Realm Roles=['create-realm', 'default-roles-master', 'offline_access', 'admin', 'uma_authorization', 'myrole']"
}
```

## ETC

```bash
# React 기본 패키지 설치시 사용한 명령어 
$ npx create-react-app frontend_react
$ cd frontend_react
$ npm install keycloak-react-web
$ npm install axios
$ npm install keycloak-js
$ npm start
Compiled successfully!
..
webpack compiled successfully
```
