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

## Execution

```bash
# Frontend 앱 구동
$ cd frontend-react
$ npm install
$ npm start

# Backend 앱 구동
$ cd backend_python
$ python main.py

# Frontend 에서 button 을 눌렀을 때 F12로 Console Output 확인하여 access_token 의 일부 정보를 가져오는지 확인
```

## Test

```bash

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
