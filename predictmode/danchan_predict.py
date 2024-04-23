import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

def danchan_predict(area, year):
    # Download csv file from URL
    url = 'https://raw.githubusercontent.com/Te2337/predict/main/Data/hebei-pastdata.csv'

    # Read CSV file
    df = pd.read_csv(url)

    # Define area
    column_mapping = {
        '邢台': 1,
        '霸州': 2,
        # 其他地名依次添加
    }

    # 根据用户选择的地名选择相应的 Y 值列
    if area in column_mapping:
        y_column_index = column_mapping[area]
        Y = df.iloc[:, y_column_index]
    else:
        return "地名输入有误，请输入正确的地名"

    # 使用年份作为 X 值
    X = df.iloc[:, 0]

    # 定义多项式函数
    def polynomial(x, alpha, beta, gamma, phi):
        return alpha * x**3 + beta * x**2 + gamma * x + phi

    popt, pcov = curve_fit(polynomial, X, Y)

    # 提取拟合的系数
    alpha, beta, gamma, phi = popt

    #计算预测单产
    Y_t = alpha * year**3 + beta * year**2 + gamma * year + phi
    return Y_t

