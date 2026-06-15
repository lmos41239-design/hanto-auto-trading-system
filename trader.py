import csv
import os
from datetime import datetime

from market_api import SimulationMarketAPI
from order_api import SimulationOrderAPI
from strategy import MovingAverageStrategy


class AutoTrader:
    def __init__(self, settings):
        self.settings = settings
        self.market_api = SimulationMarketAPI()
        self.order_api = SimulationOrderAPI()
        self.strategy = MovingAverageStrategy(settings.ma_window)
        self.log_path = os.path.join("logs", "trade_log.csv")

    def run_once(self):
        prices = self.market_api.get_recent_prices(self.settings.stock_code)
        current_price = self.market_api.get_current_price(self.settings.stock_code)
        moving_average = self.strategy.calculate_moving_average(prices)
        signal = self.strategy.make_signal(current_price, moving_average)

        print(
            f"[CONFIG] mode={self.settings.mode}, "
            f"stock_code={self.settings.stock_code}, quantity={self.settings.quantity}"
        )
        print(f"[PRICE] current_price={current_price}, moving_average={moving_average:.2f}")
        print(f"[SIGNAL] {signal}")

        order_result = self.order_api.place_order(
            self.settings.stock_code,
            signal,
            self.settings.quantity,
            current_price,
        )
        print(f"[ORDER] {order_result['message']}")

        self._save_trade_log(current_price, moving_average, signal, order_result["status"])

    def _save_trade_log(self, current_price, moving_average, signal, order_status):
        os.makedirs("logs", exist_ok=True)
        file_exists = os.path.exists(self.log_path)
        now = datetime.now()

        with open(self.log_path, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(
                    [
                        "date",
                        "time",
                        "stock_code",
                        "current_price",
                        "moving_average",
                        "signal",
                        "quantity",
                        "mode",
                        "order_status",
                    ]
                )

            writer.writerow(
                [
                    now.strftime("%Y-%m-%d"),
                    now.strftime("%H:%M:%S"),
                    self.settings.stock_code,
                    current_price,
                    f"{moving_average:.2f}",
                    signal,
                    self.settings.quantity,
                    self.settings.mode,
                    order_status,
                ]
            )
