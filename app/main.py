from ariadne.asgi import GraphQL
from fastapi import FastAPI

from app.schema import schema

app = FastAPI()

# GraphQL 엔드포인트 설정
app.mount("/graphql", GraphQL(schema), name="graphql")
