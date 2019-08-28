# import the libraries
import calendar
import pandas as pd
import numpy as np

# for slicing purposes
jan_range = range(0,31)
dec_rangeReg = range(334,365)
dec_rangeLeap = range(335,366)
# regYrStart and regYrEnd used for years that aren't leap years
regYrStart = [0,31,59,90,120,151,181,212,243,273,304,334]
regYrEnd = [31,59,90,120,151,181,212,243,273,304,334,365]
# leapYrStart and leapYrEnd are used for leap year slicing
leapYrStart = [0,31,60,91,121,152,182,213,244,274,305,335]
leapYrEnd = [31,60,91,121,152,182,213,244,274,304,334,365]

def first_year(x, jan, dec, avg):
    for k in jan_range:
        jan.append(x.iloc[9,k])
    for k in dec_rangeReg:
        dec.append(x.iloc[9,k])

    for j, k in zip(regYrStart, regYrEnd):
        z = x.iloc[9,j:k]
        avg.append(z.mean())

def avgInput(year, dataframe, jan, dec, avg):
    """

    """

    if(calendar.isleap(year)):
        for j, k in zip(leapYrStart, leapYrEnd):
            z = dataframe.iloc[9,j:k]
            avg.append(z.mean())
        for k in jan_range:
            jan.append(dataframe.iloc[9,k])
        for k in dec_rangeLeap:
            dec.append(dataframe.iloc[9,k])
    else:
        for j, k in zip(regYrStart, regYrEnd):
            z = dataframe.iloc[9,j:k]
            avg.append(z.mean())
        for k in jan_range:
            jan.append(dataframe.iloc[9,k])
        for k in dec_rangeReg:
            dec.append(dataframe.iloc[9,k])

def comb_data(start, end, x, month1=None, month2=None, average=None):
    """

    """
    if(month1 is None):
        month1 = []
    if(month2 is None):
        month2 = []
    if(average is None):
        average

    first_year(x, month1, month2, average)

    for i in range(start, end+1):
        y = pd.read_csv("ftp://ftp.cpc.ncep.noaa.gov/htdocs/degree_days/weighted/daily_data/{}/Population.Heating.txt".format(i), delimiter="|", skiprows=[0,1,2])
        y = y.set_index('Region')
        result = pd.concat([x,y], axis=1)
        x = result

        avgInput(i, y, month1, month2, average)
    return(x)
