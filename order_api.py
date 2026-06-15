class SimulationOrderAPI:
    def place_order(self, stock_code: str, signal: str, quantity: int, price: int):
        if signal == "HOLD":
            message = f"No order placed for {stock_code}. Signal is HOLD."
            status = "SKIPPED"
        else:
            message = (
                f"Simulation order completed: {signal} {quantity} share(s) "
                f"of {stock_code} at {price} KRW"
            )
            status = "COMPLETED"

        return {
            "stock_code": stock_code,
            "signal": signal,
            "quantity": quantity,
            "price": price,
            "status": status,
            "message": message,
        }
