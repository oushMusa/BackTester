import pandas as pd
from binance.client import Client as BClient
import config as cfg



client = BClient(cfg.apiKey, cfg.secretKey)  #


def getMinuteData(symbol, interval, lookback):
    frame = pd.DataFrame(
        client.get_historical_klines(symbol, interval, lookback + " min ago UTC")
    )
    frame = frame.iloc[:, :6]
    #     frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    #     frame = frame.set_index('Time')
    frame[0] = pd.to_datetime(frame[0], unit="ms")
    # frame = frame.astype(float)
    data = frame
    print(data)
    data.to_csv("DataFrame.csv", index=False)
    # return frame

