import strawberry
from sqlalchemy.orm import Session

from app.database.connect import get_db
from app.database.models import *
from app.graphql.types import *


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_actor(
        self, first_name: str, last_name: str, last_update: datetime
    ) -> ActorGQL:
        db: Session = next(get_db())

        # 새로운 배우 생성
        new_actor = ActorTable(
            first_name=first_name, last_name=last_name, last_update=last_update
        )
        db.add(new_actor)
        db.commit()
        db.refresh(new_actor)

        return ActorGQL(
            actor_id=strawberry.ID(str(new_actor.actor_id)),
            first_name=new_actor.first_name,
            last_name=new_actor.last_name,
            last_update=new_actor.last_update,
        )
