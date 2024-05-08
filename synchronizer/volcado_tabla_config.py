from datetime import datetime

from .database import SessionLocal
from .models import Configuration, Configuration_daily


def volcado_config_daily():
    db = SessionLocal()

    config = db.query(Configuration).all()  # obtiene todos los simbolos de la tabla config

    for item in config:
        symbol_pesos = item.symbol_pesos
        symbol_dollar = item.symbol_dollar
        market = item.market
        symbol_foreign = item.symbol_foreign
        quantity_local = item.quantity_local
        quantity_foreign = item.quantity_foreign
        date = datetime.now().date()

        # verifica si la fila ya existe en config_daily usando date y symbol pesos como referencia
        existing = db.query(Configuration_daily).filter_by(date=date, symbol_pesos=symbol_pesos).first()

        if existing:
            # si existe, actualiza
            existing.symbol_dollar = symbol_dollar
            existing.market = market
            existing.symbol_foreign = symbol_foreign
            existing.quantity_local = quantity_local
            existing.quantity_foreign = quantity_foreign
        else:
            # si no existe, inserta una fila nueva
            new = Configuration_daily(
                symbol_pesos=symbol_pesos,
                symbol_dollar=symbol_dollar,
                market=market,
                symbol_foreign=symbol_foreign,
                quantity_local=quantity_local,
                quantity_foreign=quantity_foreign,
                date=date
            )
            db.add(new)

    db.commit()
    db.close()

    print("Volcado de datos de config a config_daily completado con éxito")


if __name__ == "__main__":
    volcado_config_daily()
