import yfinance as yf

from .database import SessionLocal
from .models import Historical_price, Configuration


def get_history(symbol, market):
    try:
        history = yf.Ticker(symbol).history()  # obtiene el historico del simbolo

        history.columns = history.columns.str.lower()  # convierte los nombres de las columnas en minúsculas

        return history

    except Exception as e:
        print(f"Error al obtener datos históricos para {symbol}: {e}")
        return None


def save_data_to_db():
    db = SessionLocal()
    symbols = db.query(Configuration).all()  # obtiene todos los simbolos de la tabla config

    for simbolo in symbols:
        symbol = simbolo.symbol_pesos
        market = simbolo.market

        history = get_history(symbol, market)

        if history is not None:

            for index, row in history.iterrows():
                date = index
                open_price = row['open']
                high_price = row['high']
                low_price = row['low']
                close_price = row['close']
                volume = int(row['volume'])
                dividends = row.get('dividends')
                stock_splits = row.get('stock_splits')

                historical_price = Historical_price(

                    date=date,
                    symbol=symbol,
                    open=open_price,
                    high=high_price,
                    low=low_price,
                    close=close_price,
                    volume=volume,
                    dividends=dividends,
                    stock_splits=stock_splits,
                    market=market
                )

                db.add(historical_price)
                db.commit()

            print(f"Datos históricos de {symbol} cargados con éxito en la base de datos.")


if __name__ == "__main__":
    save_data_to_db()
    # print(yf.Ticker("AAPL").history())
