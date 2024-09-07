import strawberry
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from app.database.connect import get_db
from app.graphql.mutation import Mutation
from app.graphql.query import Query

schema = strawberry.Schema(query=Query, mutation=Mutation)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 비동기 DB 세션을 주입하는 미들웨어 설정
async def get_context(request: Request):
    async for db in get_db():
        request.state.db = db
    return {"db": request.state.db}


# GraphQL 라우터 추가
graphql_app: GraphQLRouter = GraphQLRouter(
    schema=schema, context_getter=get_context
)

# GraphQL 엔드포인트
app.include_router(graphql_app, prefix="/graphql")


# 루트 경로 접속 시 메시지
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Strawberry GraphQL Server!"}
