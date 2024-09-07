from sqlalchemy import BIGINT, TEXT, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from db.base import CreateModel


class User(CreateModel):
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    admin: Mapped[bool] = mapped_column(Boolean(), default=False)
    username: Mapped[str] = mapped_column(nullable=True)
    full_name: Mapped[str] = mapped_column(nullable=True)


class Network(CreateModel):
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    name: Mapped[str]
    link: Mapped[str]


class Phone(CreateModel):
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    name: Mapped[str] = mapped_column(TEXT)


class About(CreateModel):
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    name: Mapped[str] = mapped_column(TEXT)


class Channels(CreateModel):
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    url: Mapped[str] = mapped_column(String())
    title: Mapped[str] = mapped_column(String())
