import pandas as pd
import requests

df = pd.read_csv("/home/cridonoso/Documents/ds-league/docs/Encuesta_fams.csv")
URL = "http://0.0.0.0:8000/app/data/family/"
for v in df.values[3:]:
    PARAMS = {
        'index': v[0],
        'index_exp': v[1],
        'folio': v[2],
        'ingreso': v[3],
        'fe': v[4],
        'np': v[6],
        'gasto': v[8],
        'ingreso_disp': v[7],
        'ptge_gasto': v[9],
    }
    r = requests.post(url = URL, data = PARAMS)
    print(PARAMS)
