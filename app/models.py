import base64
from typing import Never, Optional

from sqlalchemy import (
    TIMESTAMP,
    Boolean,
    Column,
    Date,
    ForeignKey,
    Integer,
    LargeBinary,
    Numeric,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import ARRAY, TSVECTOR
from sqlalchemy.ext.hybrid import hybrid_property

from app.database import Base


# Actor 테이블 모델 정의
class Actor(Base):
    __tablename__ = "actor"

    actor_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    last_update = Column(TIMESTAMP, nullable=False)


# Address 테이블 모델 정의
class Address(Base):
    __tablename__ = "address"

    address_id = Column(Integer, primary_key=True, index=True)
    address = Column(String(50), nullable=False)
    address2 = Column(String(50), nullable=True)
    district = Column(String(20), nullable=False)
    city_id = Column(Integer, ForeignKey("city.city_id"), nullable=False)
    postal_code = Column(String(10), nullable=True)
    phone = Column(String(20), nullable=False)
    last_update = Column(TIMESTAMP, nullable=False)


# Category 테이블 모델 정의
class Category(Base):
    __tablename__ = "category"

    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(25), nullable=False)
    last_update = Column(TIMESTAMP, nullable=False)


# City 테이블 모델 정의
class City(Base):
    __tablename__ = "city"

    city_id = Column(Integer, primary_key=True, index=True)
    city = Column(String(50), nullable=False)
    country_id = Column(
        Integer, ForeignKey("country.country_id"), nullable=False
    )
    last_update = Column(TIMESTAMP, nullable=False)


# Country 테이블 모델 정의
class Country(Base):
    __tablename__ = "country"

    country_id = Column(Integer, primary_key=True, index=True)
    country = Column(String(50), nullable=False)
    last_update = Column(TIMESTAMP, nullable=False)


# Customer 테이블 모델 정의
class Customer(Base):
    __tablename__ = "customer"

    customer_id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer, nullable=False)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    email = Column(String(50), nullable=True)
    address_id = Column(
        Integer, ForeignKey("address.address_id"), nullable=False
    )
    activebool = Column(Boolean, nullable=False, default=True)
    create_date = Column(Date, nullable=False)
    last_update = Column(TIMESTAMP, nullable=True)
    active = Column(Integer, nullable=True)


# Film 테이블 모델 정의
class Film(Base):
    __tablename__ = "film"

    film_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    release_year = Column(Integer, nullable=True)
    language_id = Column(
        Integer, ForeignKey("language.language_id"), nullable=False
    )
    rental_duration = Column(Integer, nullable=False, default=3)
    rental_rate = Column(Numeric(4, 2), nullable=False, default=4.99)
    length = Column(Integer, nullable=True)
    replacement_cost = Column(Numeric(5, 2), nullable=False, default=19.99)
    rating = Column(String, nullable=True)
    last_update = Column(TIMESTAMP, nullable=False)
    special_features: Column[Never] = Column(ARRAY(Text), nullable=True)

    fulltext = Column(TSVECTOR, nullable=False)


# FilmActor 테이블 모델 정의
class FilmActor(Base):
    __tablename__ = "film_actor"

    actor_id = Column(
        Integer,
        ForeignKey("actor.actor_id", ondelete="RESTRICT", onupdate="CASCADE"),
        primary_key=True,
    )
    film_id = Column(
        Integer,
        ForeignKey("film.film_id", ondelete="RESTRICT", onupdate="CASCADE"),
        primary_key=True,
    )
    last_update = Column(TIMESTAMP, nullable=False)


# FilmCategory 테이블 모델 정의
class FilmCategory(Base):
    __tablename__ = "film_category"

    film_id = Column(
        Integer,
        ForeignKey("film.film_id", ondelete="RESTRICT", onupdate="CASCADE"),
        primary_key=True,
    )
    category_id = Column(
        Integer,
        ForeignKey(
            "category.category_id", ondelete="RESTRICT", onupdate="CASCADE"
        ),
        primary_key=True,
    )
    last_update = Column(TIMESTAMP, nullable=False)


# Inventory 테이블 모델 정의
class Inventory(Base):
    __tablename__ = "inventory"

    inventory_id = Column(Integer, primary_key=True, index=True)
    film_id = Column(
        Integer,
        ForeignKey("film.film_id", ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=False,
    )
    store_id = Column(Integer, nullable=False)
    last_update = Column(TIMESTAMP, nullable=False)


# Language 테이블 모델 정의
class Language(Base):
    __tablename__ = "language"

    language_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), nullable=False)
    last_update = Column(TIMESTAMP, nullable=False)


# Payment 테이블 모델 정의
class Payment(Base):
    __tablename__ = "payment"

    payment_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(
        Integer,
        ForeignKey(
            "customer.customer_id", ondelete="RESTRICT", onupdate="CASCADE"
        ),
        nullable=False,
    )
    staff_id = Column(
        Integer,
        ForeignKey("staff.staff_id", ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=False,
    )
    rental_id = Column(
        Integer,
        ForeignKey(
            "rental.rental_id", ondelete="SET NULL", onupdate="CASCADE"
        ),
        nullable=False,
    )
    amount = Column(Numeric(5, 2), nullable=False)
    payment_date = Column(TIMESTAMP, nullable=False)


# Rental 테이블 모델 정의
class Rental(Base):
    __tablename__ = "rental"

    rental_id = Column(Integer, primary_key=True, index=True)
    rental_date = Column(TIMESTAMP, nullable=False)
    inventory_id = Column(
        Integer,
        ForeignKey(
            "inventory.inventory_id", ondelete="RESTRICT", onupdate="CASCADE"
        ),
        nullable=False,
    )
    customer_id = Column(
        Integer,
        ForeignKey(
            "customer.customer_id", ondelete="RESTRICT", onupdate="CASCADE"
        ),
        nullable=False,
    )
    return_date = Column(TIMESTAMP, nullable=True)
    staff_id = Column(
        Integer,
        ForeignKey("staff.staff_id", ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=False,
    )
    last_update = Column(TIMESTAMP, nullable=False)


# Staff 테이블 모델 정의
class Staff(Base):
    __tablename__ = "staff"

    staff_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    address_id = Column(
        Integer,
        ForeignKey(
            "address.address_id", ondelete="RESTRICT", onupdate="CASCADE"
        ),
        nullable=False,
    )
    email = Column(String(50), nullable=True)
    store_id = Column(Integer, nullable=False)
    active = Column(Boolean, nullable=False, default=True)
    username = Column(String(16), nullable=False)
    password = Column(String(40), nullable=True)
    last_update = Column(TIMESTAMP, nullable=False)
    picture = Column(LargeBinary, nullable=True)

    # picture 필드를 Base64로 인코딩된 문자열로 반환
    @hybrid_property
    def picture_base64(self) -> Optional[str]:
        if self.picture:
            picture_str = base64.b64encode(self.picture).decode("utf-8")
            return picture_str
        return None


# Store 테이블 모델 정의
class Store(Base):
    __tablename__ = "store"

    store_id = Column(Integer, primary_key=True, index=True)
    manager_staff_id = Column(
        Integer,
        ForeignKey("staff.staff_id", ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=False,
    )
    address_id = Column(
        Integer,
        ForeignKey(
            "address.address_id", ondelete="RESTRICT", onupdate="CASCADE"
        ),
        nullable=False,
    )
    last_update = Column(TIMESTAMP, nullable=False)
