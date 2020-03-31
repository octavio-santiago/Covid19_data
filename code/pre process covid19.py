import pandas as pd
import glob

files = glob.glob(r"C:\Users\braeued1\Documents\Octavio\projetos\COVID-19\csse_covid_19_data\csse_covid_19_daily_reports\*.csv")

for idx,file in enumerate(files):
    if idx == 0 :
        df = pd.read_csv(file,sep=",")
    else:
        df = df.append(pd.read_csv(file,sep=","))

print(df.head())


def export():
    df.to_excel(r"C:\Users\braeued1\Documents\Octavio\projetos\Covid19_data\dataset\daily cases.xlsx")

    
export()
