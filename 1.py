from hmac import new
import time
from venv import create
import flask
import django
import sqlalchemy
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, Session
from sqlalchemy import create_engine, select

class Base(DeclarativeBase):
    pass


class Tip(Base):
    __tablename__ = 'tips'

    total_bill: Mapped[float] = mapped_column(primary_key=True)
    tip: Mapped[float]
    sex: Mapped[str]
    smoker: Mapped[str]
    day: Mapped[str]
    time: Mapped[str]
    size: Mapped[int]

    def __repr__(self) -> str:
        return f'{self.total_bill} {self.tip} {self.sex} {self.smoker}'


def get_engine():
    return create_engine('sqlite:///tips.db', echo=True)

def query(param):
    eng = get_engine()
    sess = Session(eng)

    stmt = select(Tip).where(Tip.sex.__eq__('Male'))
    for tip in sess.scalars(stmt):
        print(tip)

    newtip = Tip(total_bill=101.1, tip=1.1, sex='Male', smoker='No')
    print(newtip)

    sess.add(newtip)
    sess.commit()




if __name__ == '__main__':
    query('Male')