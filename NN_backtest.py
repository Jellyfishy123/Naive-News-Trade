from AlgoAPI import AlgoAPI_Backtest
from strategy import AlgoEvent  # Make sure this matches your filename and class name
import os

if __name__ == "__main__":
    print("Starting News-Based Trading Backtest...")

    # Initialize backtest environment
    bt = AlgoAPI_Backtest.AlgoBacktest()

    # === CONFIGURATION ===
    strategy_name = "demo_NewsDriven"
    start_date = "2019-01"
    end_date = "2019-12"
    instruments = ['SPXUSD']
    data_interval = "1d"
    base_currency = "USD"
    initial_capital = 100000
    leverage = 1
    commission = 0.0
    allow_short = True

    # === Set Parameters ===
    bt.setStrategyName(strategy_name)
    bt.setStartDate(start_date)
    bt.setEndDate(end_date)
    bt.setDataInterval(data_interval)
    bt.setBaseCurrency(base_currency)
    bt.setInitialCash(initial_capital)
    bt.setLeverage(leverage)
    bt.setCommission(commission)
    bt.setAllowShortSell(allow_short)

    # Load market and news data
    for instrument in instruments:
        market_data_path = os.path.join("data", f"{instrument}_1day.csv")
        news_data_path = os.path.join("data", f"{instrument}_news.csv")
        bt.loadMarketDataFromFile(market_data_path, instrument)
        bt.loadNewsDataFromFile(news_data_path, instrument)

    # Subscribe to instruments
    bt.setSubscribeInstrumentList(instruments)

    # Start the strategy
    algo = AlgoEvent()
    algo.start(bt)

    # Run the backtest
    bt.runBacktest()

    # === Output Results ===
    print("Backtest Completed.")
    print("Final Cash:", bt.getCash())
    print("Total P&L:", bt.getTotalPL())
    print("Open Positions:", bt.getOpenPositions())

    # Export P&L if needed
    bt.exportPL("news_strategy_results.csv")
