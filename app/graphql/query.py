# from app.database.models import *
import strawberry
from pg_sample_schema.models import *
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from app.database.connect import get_db
from app.graphql.types import *


@strawberry.type
class Query:
    @strawberry.field
    async def actors(
        self,
        info,
        limit: int = 10,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
    ) -> list[ActorGQL]:
        # 비동기 세션 가져오기
        async_session: AsyncSession = info.context["db"]

        # 비동기 SQLAlchemy 쿼리 작성
        query = select(ActorTable)

        # 필터 조건 추가
        if first_name:
            query = query.where(ActorTable.first_name == first_name)
        if last_name:
            query = query.where(ActorTable.last_name == last_name)

        # 쿼리 실행
        result = await async_session.execute(query.limit(limit))
        actors = result.scalars().all()

        # ActorGQL 객체 리스트 반환
        return [
            ActorGQL(
                actor_id=actor.actor_id,
                first_name=actor.first_name,
                last_name=actor.last_name,
                last_update=actor.last_update,
            )
            for actor in actors
        ]

    @strawberry.field
    async def addresses(self, limit: int = 10) -> list[AddressGQL]:
        db: Session = next(get_db())
        addresses = db.query(AddressTable).limit(limit).all()
        return [
            AddressGQL(
                address_id=address.address_id,
                address=address.address,
                address2=address.address2,
                district=address.district,
                city_id=address.city_id,
                postal_code=address.postal_code,
                phone=address.phone,
                last_update=address.last_update,
            )
            for address in addresses
        ]

    @strawberry.field
    async def categories(self, limit: int = 10) -> list[CategoryGQL]:
        db: Session = next(get_db())
        categories = db.query(CategoryTable).limit(limit).all()
        return [
            CategoryGQL(
                category_id=category.category_id,
                name=category.name,
                last_update=category.last_update,
            )
            for category in categories
        ]

    @strawberry.field
    async def cities(self, limit: int = 10) -> list[CityGQL]:
        db: Session = next(get_db())
        cities = db.query(CityTable).limit(limit).all()
        return [
            CityGQL(
                city_id=city.city_id,
                city=city.city,
                country_id=city.country_id,
                last_update=city.last_update,
            )
            for city in cities
        ]

    @strawberry.field
    async def countries(self, limit: int = 10) -> list[CountryGQL]:
        db: Session = next(get_db())
        countries = db.query(CountryTable).limit(limit).all()
        return [
            CountryGQL(
                country_id=country.country_id,
                country=country.country,
                last_update=country.last_update,
            )
            for country in countries
        ]

    @strawberry.field
    async def customers(self, limit: int = 10) -> list[CustomerGQL]:
        db: Session = next(get_db())
        customers = db.query(CustomerTable).limit(limit).all()
        return [
            CustomerGQL(
                customer_id=customer.customer_id,
                store_id=customer.store_id,
                first_name=customer.first_name,
                last_name=customer.last_name,
                email=customer.email,
                address_id=customer.address_id,
                activebool=customer.activebool,
                create_date=customer.create_date,
                last_update=customer.last_update,
                active=customer.active,
            )
            for customer in customers
        ]

    @strawberry.field
    async def films(self, limit: int = 10) -> list[FilmGQL]:
        db: Session = next(get_db())
        films = db.query(FilmTable).limit(limit).all()
        return [
            FilmGQL(
                film_id=film.film_id,
                title=film.title,
                description=film.description,
                release_year=film.release_year,
                language_id=film.language_id,
                rental_duration=film.rental_duration,
                rental_rate=film.rental_rate,
                length=film.length,
                replacement_cost=film.replacement_cost,
                rating=film.rating,
                last_update=film.last_update,
                special_features=film.special_features,
                fulltext=film.fulltext,
            )
            for film in films
        ]

    @strawberry.field
    async def film_actors(self, limit: int = 10) -> list[FilmActorGQL]:
        db: Session = next(get_db())
        film_actors = db.query(FilmActorTable).limit(limit).all()
        return [
            FilmActorGQL(
                actor_id=film_actor.actor_id,
                film_id=film_actor.film_id,
                last_update=film_actor.last_update,
            )
            for film_actor in film_actors
        ]

    @strawberry.field
    async def film_categories(self, limit: int = 10) -> list[FilmCategoryGQL]:
        db: Session = next(get_db())
        film_categories = db.query(FilmCategoryTable).limit(limit).all()
        return [
            FilmCategoryGQL(
                film_id=film_category.film_id,
                category_id=film_category.category_id,
                last_update=film_category.last_update,
            )
            for film_category in film_categories
        ]

    @strawberry.field
    async def inventories(self, limit: int = 10) -> list[InventoryGQL]:
        db: Session = next(get_db())
        inventories = db.query(InventoryTable).limit(limit).all()
        return [
            InventoryGQL(
                inventory_id=inventory.inventory_id,
                film_id=inventory.film_id,
                store_id=inventory.store_id,
                last_update=inventory.last_update,
            )
            for inventory in inventories
        ]

    @strawberry.field
    async def languages(self, limit: int = 10) -> list[LanguageGQL]:
        db: Session = next(get_db())
        languages = db.query(LanguageTable).limit(limit).all()
        return [
            LanguageGQL(
                language_id=language.language_id,
                name=language.name,
                last_update=language.last_update,
            )
            for language in languages
        ]

    @strawberry.field
    async def payments(self, limit: int = 10) -> list[PaymentGQL]:
        db: Session = next(get_db())
        payments = db.query(PaymentTable).limit(limit).all()
        return [
            PaymentGQL(
                payment_id=payment.payment_id,
                customer_id=payment.customer_id,
                staff_id=payment.staff_id,
                rental_id=payment.rental_id,
                amount=payment.amount,
                payment_date=payment.payment_date,
            )
            for payment in payments
        ]

    @strawberry.field
    async def rentals(self, limit: int = 10) -> list[RentalGQL]:
        db: Session = next(get_db())
        rentals = db.query(RentalTable).limit(limit).all()
        return [
            RentalGQL(
                rental_id=rental.rental_id,
                rental_date=rental.rental_date,
                inventory_id=rental.inventory_id,
                customer_id=rental.customer_id,
                return_date=rental.return_date,
                staff_id=rental.staff_id,
                last_update=rental.last_update,
            )
            for rental in rentals
        ]

    @strawberry.field
    async def staffs(self, limit: int = 10) -> list[StaffGQL]:
        db: Session = next(get_db())
        staffs = db.query(StaffTable).limit(limit).all()
        return [
            StaffGQL(
                staff_id=staff.staff_id,
                first_name=staff.first_name,
                last_name=staff.last_name,
                address_id=staff.address_id,
                email=staff.email,
                store_id=staff.store_id,
                active=staff.active,
                username=staff.username,
                password=staff.password,
                last_update=staff.last_update,
                picture=staff.picture_base64,
            )
            for staff in staffs
        ]

    @strawberry.field
    async def stores(self, limit: int = 10) -> list[StoreGQL]:
        db: Session = next(get_db())
        stores = db.query(StoreTable).limit(limit).all()
        return [
            StoreGQL(
                store_id=store.store_id,
                manager_staff_id=store.manager_staff_id,
                address_id=store.address_id,
                last_update=store.last_update,
            )
            for store in stores
        ]
