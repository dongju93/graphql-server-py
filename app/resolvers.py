from ariadne import QueryType
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import (
    Actor,
    Address,
    Category,
    City,
    Country,
    Customer,
    Film,
    FilmActor,
    FilmCategory,
    Inventory,
    Language,
    Payment,
    Rental,
    Staff,
    Store,
)

query = QueryType()


@query.field("actors")
def resolve_actors(_, info, limit: int = 10):
    db: Session = next(get_db())
    return db.query(Actor).limit(limit).all()


@query.field("addresses")
def resolve_addresses(_, info, limit: int = 10):
    db: Session = next(get_db())
    return db.query(Address).limit(limit).all()


@query.field("categories")
def resolve_categories(_, info, limit: int = 10):
    db: Session = next(get_db())
    return db.query(Category).limit(limit).all()


@query.field("cities")
def resolve_cities(_, info, limit: int = 10):
    db: Session = next(get_db())
    return db.query(City).limit(limit).all()


@query.field("countries")
def resolve_countries(_, info, limit: int = 10):
    db: Session = next(get_db())
    return db.query(Country).limit(limit).all()


@query.field("customers")
def resolve_customers(_, info, limit: int = 10):
    db: Session = next(get_db())
    return db.query(Customer).limit(limit).all()


@query.field("films")
def resolve_films(_, info, limit: int = 10):
    db: Session = next(get_db())
    return db.query(Film).limit(limit).all()


@query.field("filmActors")
def resolve_film_actors(_, info, limit: int = 10):
    db: Session = next(get_db())
    return db.query(FilmActor).limit(limit).all()


@query.field("filmCategories")
def resolve_film_categories(_, info, limit: int = 10):
    db: Session = next(get_db())
    return db.query(FilmCategory).limit(limit).all()


@query.field("inventories")
def resolve_inventories(_, info, limit: int = 10):
    db: Session = next(get_db())
    return db.query(Inventory).limit(limit).all()


@query.field("languages")
def resolve_languages(_, info, limit: int = 10):
    db: Session = next(get_db())
    return db.query(Language).limit(limit).all()


@query.field("payments")
def resolve_payments(_, info, limit: int = 10):
    db: Session = next(get_db())
    return db.query(Payment).limit(limit).all()


@query.field("rentals")
def resolve_rentals(_, info, limit: int = 10):
    db: Session = next(get_db())
    return db.query(Rental).limit(limit).all()


@query.field("staffs")
def resolve_staffs(_, info, limit: int = 10):
    db: Session = next(get_db())
    staffs = db.query(Staff).limit(limit).all()
    """
    바이너리 타입으로 구성된 picture 필드를 사용하기 위해
    Base64로 인코딩된 picture 필드를 추가하고 (picture_base64)
    전체 결과를 리스트에 딕셔너리로 담아 반환
    """
    results = []
    for staff in staffs:
        results.append(
            {
                "staff_id": staff.staff_id,
                "first_name": staff.first_name,
                "last_name": staff.last_name,
                "address_id": staff.address_id,
                "email": staff.email,
                "store_id": staff.store_id,
                "active": staff.active,
                "username": staff.username,
                "password": staff.password,
                "last_update": staff.last_update.isoformat(),
                "picture": staff.picture_base64,
            }
        )

    return results


@query.field("stores")
def resolve_stores(_, info, limit: int = 10):
    db: Session = next(get_db())
    return db.query(Store).limit(limit).all()
