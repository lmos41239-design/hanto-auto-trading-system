class MovingAverageStrategy:
    def __init__(self, window: int = 5):
        self.window = window

    def calculate_moving_average(self, prices):
        selected_prices = prices[-self.window :]
        return sum(selected_prices) / len(selected_prices)

    def make_signal(self, current_price: int, moving_average: float) -> str:
        if current_price > moving_average:
            return "BUY"
        if current_price < moving_average:
            return "SELL"
        return "HOLD"
