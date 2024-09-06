from ariadne import gql, load_schema_from_path, make_executable_schema

from app.resolvers import query

# GraphQL 스키마 정의 파일 로드
type_defs = load_schema_from_path("graphql/dvdrental.graphql")

# GraphQL 스키마 생성
schema = make_executable_schema(type_defs, query)
