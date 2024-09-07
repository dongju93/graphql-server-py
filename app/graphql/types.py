from datetime import date, datetime
from typing import Optional

import strawberry


@strawberry.type
class ActorGQL:
    actor_id: strawberry.ID
    first_name: str
    last_name: str
    last_update: datetime


@strawberry.type
class AddressGQL:
    address_id: strawberry.ID
    address: str
    address2: Optional[str]
    district: str
    city_id: strawberry.ID
    postal_code: Optional[str]
    phone: str
    last_update: datetime


@strawberry.type
class CategoryGQL:
    category_id: strawberry.ID
    name: str
    last_update: datetime


@strawberry.type
class CityGQL:
    city_id: strawberry.ID
    city: str
    country_id: strawberry.ID
    last_update: datetime


@strawberry.type
class CountryGQL:
    country_id: strawberry.ID
    country: str
    last_update: datetime


@strawberry.type
class CustomerGQL:
    customer_id: strawberry.ID
    store_id: strawberry.ID
    first_name: str
    last_name: str
    email: Optional[str]
    address_id: strawberry.ID
    activebool: bool
    create_date: date
    last_update: Optional[datetime]
    active: Optional[int]


@strawberry.type
class FilmGQL:
    film_id: strawberry.ID
    title: str
    description: Optional[str]
    release_year: Optional[int]
    language_id: strawberry.ID
    rental_duration: int
    rental_rate: float
    length: Optional[int]
    replacement_cost: float
    rating: Optional[str]
    last_update: datetime
    special_features: Optional[list[str]]
    fulltext: str


@strawberry.type
class FilmActorGQL:
    actor_id: strawberry.ID
    film_id: strawberry.ID
    last_update: datetime


@strawberry.type
class FilmCategoryGQL:
    film_id: strawberry.ID
    category_id: strawberry.ID
    last_update: datetime


@strawberry.type
class InventoryGQL:
    inventory_id: strawberry.ID
    film_id: strawberry.ID
    store_id: strawberry.ID
    last_update: datetime


@strawberry.type
class LanguageGQL:
    language_id: strawberry.ID
    name: str
    last_update: datetime


@strawberry.type
class PaymentGQL:
    payment_id: strawberry.ID
    customer_id: strawberry.ID
    staff_id: strawberry.ID
    rental_id: strawberry.ID
    amount: float
    payment_date: datetime


@strawberry.type
class RentalGQL:
    rental_id: strawberry.ID
    rental_date: datetime
    inventory_id: strawberry.ID
    customer_id: strawberry.ID
    return_date: Optional[datetime]
    staff_id: strawberry.ID
    last_update: datetime


@strawberry.type
class StaffGQL:
    staff_id: strawberry.ID
    first_name: str
    last_name: str
    address_id: strawberry.ID
    email: Optional[str]
    store_id: strawberry.ID
    active: bool
    username: str
    password: Optional[str]
    last_update: datetime
    picture: Optional[str]


@strawberry.type
class StoreGQL:
    store_id: strawberry.ID
    manager_staff_id: strawberry.ID
    address_id: strawberry.ID
    last_update: datetime
