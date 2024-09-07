import strawberry
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from app.graphql.resolvers import Query

schema = strawberry.Schema(query=Query)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GraphQL 라우터 추가
graphql_app: GraphQLRouter = GraphQLRouter(schema)

# GraphQL 엔드포인트
app.include_router(graphql_app, prefix="/graphql")


# 루트 경로 접속 시 메시지
@app.get("/")
def read_root():
    return {"message": "Welcome to the Strawberry GraphQL Server!"}
