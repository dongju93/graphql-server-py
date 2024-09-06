# GraphQL server

## 데이터
* 데이터베이스 : PostgreSQL
* 데이터 : https://www.postgresqltutorial.com/postgresql-getting-started/load-postgresql-sample-database/

## 서버 실행
```Bash
# 종속성 설치
poetry install
# 실행
poetry run uvicorn app.main:app --port 8200 --reload
```