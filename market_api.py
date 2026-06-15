class SimulationMarketAPI:
    def __init__(self):
        self.prices = [71000, 71500, 72000, 72500, 73000, 73500]

    def get_recent_prices(self, stock_code: str):
        return self.prices

    def get_current_price(self, stock_code: str):
        return self.prices[-1]
