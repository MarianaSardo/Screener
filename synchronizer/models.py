from sqlalchemy import Column, Integer, String, Float, DateTime, UniqueConstraint, BigInteger, CheckConstraint

from .database import Base


class Configuration(Base):
    __tablename__ = 'config'

    id = Column(Integer, primary_key=True, index=True)
    symbol_pesos = Column(String)
    symbol_dollar = Column(String)
    market = Column(String)
    symbol_foreign = Column(String)
    quantity_local = Column(Float)
    quantity_foreign = Column(Float)

    __table_args__ = (
        UniqueConstraint('symbol_pesos'),
    )


class Configuration_daily(Base):
    __tablename__ = 'config_daily'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    symbol_pesos = Column(String)
    symbol_dollar = Column(String)
    market = Column(String)
    symbol_foreign = Column(String)
    quantity_local = Column(Float)
    quantity_foreign = Column(Float)

    __table_args__ = (
        CheckConstraint(
            "NOT EXISTS (SELECT 1 FROM config_daily WHERE date = :date AND symbol_pesos = :symbol_pesos)",
            name='date_symbol_pesos'
        ),
    )


class Historical_price(Base):
    __tablename__ = 'historical_prices'

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String(255), nullable=False)
    date = Column(DateTime)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(BigInteger)
    dividends = Column(Float)
    stock_splits = Column(Float)
    market = Column(String)
