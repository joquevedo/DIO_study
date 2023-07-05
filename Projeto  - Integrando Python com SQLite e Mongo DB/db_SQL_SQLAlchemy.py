"""
Este código faz parte de uma etapa do curso Python Developer da Digital Inovation One.
Especificamente faz parte da unidade que fala sobre integração de Python com frameworks,
e este implementa duas tabelas em um banco de dados relacional através do 
SQLAlchemy.

Procurei me basear tanto nas informações dadas pelo curso quanto na própria documentação do
framework. O código ainda precisa ser refatorado e aprimorado

Trata-se de um exercício de fins educacionais.
"""
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy import select

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import Session
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


#defining an in-memory sqlite engine 
engine = create_engine("sqlite+pysqlite:///:memory:",echo = True )

class Base(DeclarativeBase):
    """Calling declarative base for modeling tables"""
    pass

class Cliente(Base):
    """"A Table representing a user (cliente) """
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key = True)
    nome: Mapped[str] = mapped_column(String)
    cpf: Mapped[str] = mapped_column(String(9))
    endereco: Mapped[str] = mapped_column(String(9))

    conta = relationship(
        "Conta", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Cliente (id = {self.id}, nome = {self.nome})"

class Conta(Base):
    """A table representing an account (conta)"""
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key= True)
    tipo: Mapped[str] = mapped_column(String)
    agencia: Mapped[str] = mapped_column(String)
    num: Mapped[int] = mapped_column
    id_cliente: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable= False)
    saldo: Mapped[float] = mapped_column

    user = relationship(
        "Cliente", back_populates="conta"
    )

    def __repr__(self):
        return f"Cliente(id = {self.id_cliente}) Conta (num = {self.num} ag = {self.agencia})"
    

Base.metadata.create_all(engine)

with Session(engine) as session:
    jean = Cliente(
        nome = 'jean de oliveira quevedo',
        cpf = 156753321,
        endereco = 1123456789
    )

    john = Cliente(
        nome = 'john romero',
        cpf = 666666666,
        endereco = 333333333,
    )

    adams = Cliente(
        nome = 'douglas adams',
        cpf = 424242424,
        endereco = 242242242,
    )

    session.add_all([jean, john, adams])

    session.commit()

stmt  = select(Cliente).where(Cliente.nome.in_(['john romero']))

for user in session.scalars(stmt):
    print(user)