from config import load_settings
from trader import AutoTrader


def main():
    settings = load_settings()
    trader = AutoTrader(settings)
    trader.run_once()


if __name__ == "__main__":
    main()
