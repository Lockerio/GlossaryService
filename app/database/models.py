from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(), nullable=False)
    surname = Column(String(), nullable=False)
    email = Column(String(), nullable=False)
    hashed_password = Column(String(), nullable=False)


class Glossary(Base):
    __tablename__ = "glossaries"

    id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    title = Column(String(), nullable=False)
    user_id = Column(Integer(), ForeignKey("users.id"))


class Word(Base):
    __tablename__ = "words"

    id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    title = Column(String(), nullable=False)
    definition = Column(String(), nullable=False)
    context = Column(String(), nullable=False)
    translation = Column(String(), nullable=False)


class GlossaryWord(Base):
    __tablename__ = "glossaries_words"

    id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    glossary_id = Column(Integer(), ForeignKey("glossaries.id"))
    word_id = Column(Integer(), ForeignKey("words.id"))
