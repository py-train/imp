import sqlalchemy
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, Session
from sqlalchemy import create_engine, select

class Base(DeclarativeBase):
    pass

class Tips(Base):
    __tablename__ = "tips"
    
    total_bill: Mapped[float] = mapped_column(primary_key=True)
    tip: Mapped[float]
    sex: Mapped[str]
    smoker: Mapped[str]
    day: Mapped[str]
    time: Mapped[str]
    size: Mapped[int]

    def __repr__(self):
        return f'Tips({self.total_bill}, {self.tip}, {self.sex})'
    
engine = create_engine(url='sqlite:///tips.db', echo=True)

with Session(engine) as session:
    stmt = select(Tips).filter(Tips.sex.__eq__('Male'))

    result = session.scalars(stmt)
    print(result)
    for row in result:
        print(row)