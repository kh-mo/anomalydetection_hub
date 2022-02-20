import argparse
import os

import requests
from tqdm import tqdm


class UCR_TimeseriesAnomalyArchive:
    def __init__(self):
        self.url = "https://www.cs.ucr.edu/~eamonn/time_series_data_2018/UCR_TimeSeriesAnomalyDatasets2021.zip"
        self.save_path = "data/UCR_TimeSeriesAnomalyDatasets2021.zip"

    def download(self):
        r = requests.get(self.url, stream=True)
        total_size_in_bytes = int(r.headers.get("content-length", 0))
        block_size = 1024  # 1 Kibibyte
        progress_bar = tqdm(total=total_size_in_bytes, unit="iB", unit_scale=True)
        with open(self.save_path, "wb") as fd:
            for chunk in r.iter_content(block_size):
                progress_bar.update(len(chunk))
                fd.write(chunk)
            print("done")
        progress_bar.close()


def main(args):
    os.makedirs("data", exist_ok=True)
    if args.name == "ucr_time_series_anomaly_archive":
        UCR_TimeseriesAnomalyArchive().download()


if __name__ == "__main__":
    """
    python download_data.py --name=ucr_time_series_anomaly_archive
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--name")
    args = parser.parse_args()

    main(args)
