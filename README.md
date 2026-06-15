# Hanto Auto Trading System

한국투자증권 Open API 구조를 참고해서 만든 간단한 자동매매 프로젝트입니다.
실제 계좌 주문이 아니라, 수업 프로젝트용으로 simulation mode 중심으로 구현했습니다.

## Project goal

이 프로젝트의 목표는 자동매매 시스템의 기본 흐름을 직접 구현해 보는 것입니다.

전체 흐름은 다음과 같습니다.

1. 설정값을 불러온다.
2. 주가 데이터를 가져온다.
3. 이동평균 전략으로 BUY / SELL / HOLD 신호를 만든다.
4. 주문을 실행한다.
5. 거래 기록을 `logs/trade_log.csv`에 저장한다.

## Strategy

사용한 전략은 이동평균선 기반 전략입니다.

- 현재 가격이 이동평균보다 높으면: BUY
- 현재 가격이 이동평균보다 낮으면: SELL
- 거의 비슷하면: HOLD

복잡한 전략은 아니지만, 자동매매 시스템의 전체 구조를 이해하기 위해 사용했습니다.

## Files

```text
main.py          program start file
config.py        load settings
market_api.py    get simulated market price
strategy.py      moving average strategy
order_api.py     simulation order function
trader.py        connect the full trading process
logs/            trade record folder
```

## Trade record

거래 기록은 아래 파일에 저장했습니다.

```text
logs/trade_log.csv
```

예시 기록:

```text
date,time,stock_code,current_price,moving_average,signal,quantity,mode,order_status
2026-06-15,14:20:11,005930,73500,72500.00,BUY,1,simulation,COMPLETED
```

## How to run

```bash
python main.py
```

실행하면 현재 가격, 이동평균, 매매 신호, 주문 결과가 출력되고,
동시에 `logs/trade_log.csv`에 거래 기록이 추가됩니다.

## Note

이 프로젝트는 실제 투자가 아니라 수업 제출을 위한 simulation project입니다.
실제 투자 위험을 피하기 위해 실제 계좌 주문 기능은 사용하지 않았습니다.
