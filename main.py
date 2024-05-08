from synchronizer.volcado_precios_historico import save_data_to_db
from synchronizer.volcado_tabla_config import volcado_config_daily

if __name__ == "__main__":
    # Volcar tabla config a config daily
    volcado_config_daily()

    print("----------------------------------------------------------------")

    # Volcar datos historicos a BD
    save_data_to_db()
