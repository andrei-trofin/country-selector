from sklearn.preprocessing import MinMaxScaler, StandardScaler

data_scaler_type = "min_max"

data_scaler = MinMaxScaler() if data_scaler_type.__eq__("min_max") else StandardScaler()
