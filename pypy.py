import time
import pandas as pd
from ftx_client import FtxClient


def get_ftx_data(start_date: str, end_date: str):
    start_time = time.mktime(
        time.strptime(f"{start_date} 00:00:00", "%d/%m/%Y %H:%M:%S")
    )
    end_time = time.mktime(time.strptime(f"{end_date} 00:00:00", "%d/%m/%Y %H:%M:%S"))
    ftx_client = FtxClient(
        api_key="TOeiS15UOBWSFgNfhLDHnrnJrMjOg_P8n1LxBa3s",
        api_secret="ghjMqclQDf4hHNGoE5NVOpeHsTbYdjihMD9EJ3oQ",
    )

    data = ftx_client.get_all_historic_data(
        market="BTC-PERP",
        resolution=3600,
        start_time=start_time,
        end_time=end_time,
    )




start_date = "01/04/2022"
end_date = "26/06/2022"

get_ftx_data(start_date=start_date, end_date=end_date)
