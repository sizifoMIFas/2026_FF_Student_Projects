import pandas as pd
from pathlib import Path

root = Path(__file__).parent.parent
pathraw = root / "data" / "raw"
pathprocessed = root / "data" / "processed"

txtfile = pathraw / "Archigos_4.1.txt"
csvfile = pathprocessed / "Archigos_4.1.csv"
sep = "\t"

convert = pd.read_csv(txtfile, sep=sep, encoding = "latin-1")
convert.to_csv(csvfile, index=False, encoding = "utf-8")