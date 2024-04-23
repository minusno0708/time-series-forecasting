import pandas as pd

data_dir = "dataset/"
seq_len = 96

def data_loader(file):
    # csv読み込み
    df_raw = pd.read_csv(data_dir + file)

    # データのラベルの取得
    cols = list(df_raw.columns)
    cols.remove("date")
    cols.remove("OT")

    df_raw = df_raw[['date'] + cols + ["OT"]]

    num_train = int(len(df_raw) * 0.7)
    num_test = int(len(df_raw) * 0.2)
    num_vali = len(df_raw) - num_train - num_test

    cols_data = df_raw.columns[1:]
    df_data = df_raw[cols_data]
    
    data_x = df_data[:num_train]
    data_y = df_data[:num_train]

    return data_x, data_y


if __name__ == "__main__":
    x, y = data_loader("exchange_rate.csv")
    print(x.shape)
    print(y.shape)
   