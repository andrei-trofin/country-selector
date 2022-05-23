from sklearn.preprocessing import MinMaxScaler, StandardScaler

# TODO create function to deal with feature inverse for standard scaling
data_scaler_type = "min_max"

data_scaler = MinMaxScaler() if data_scaler_type.__eq__("min_max") else StandardScaler()