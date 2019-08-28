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

def first_year(data, jan = None, dec = None, average = None):
    if(jan is None):
        jan = []
    if(dec is None):
        dec = []
    if(average is None):
        average = []

    for k in jan_range:
        jan.append(data.iloc[9,k])
    for k in dec_rangeReg:
        dec.append(data.iloc[9,k])

    for j, k in zip(regYrStart, regYrEnd):
        z = data.iloc[9,j:k]
        average.append(z.mean())

    return(jan, dec, average)

def avgInput(year, dataframe, month, month2, average):
    """

    """

    if(calendar.isleap(year)):
        for j, k in zip(leapYrStart, leapYrEnd):
            z = dataframe.iloc[9,j:k]
            average.append(z.mean())
        for k in jan_range:
            month.append(dataframe.iloc[9,k])
        for k in dec_rangeLeap:
            month2.append(dataframe.iloc[9,k])
    else:
        for j, k in zip(regYrStart, regYrEnd):
            z = dataframe.iloc[9,j:k]
            average.append(z.mean())
        for k in jan_range:
            month.append(dataframe.iloc[9,k])
        for k in dec_rangeReg:
            month2.append(dataframe.iloc[9,k])

    return(month, month2, average)

def comb_data(start, end, dataframe, month1=None, month2=None, average=None):
    """

    """
    jan, dec, avgMonth = first_year(dataframe, month1, month2, average)

    for i in range(start+1, end+1):
        y = pd.read_csv("ftp://ftp.cpc.ncep.noaa.gov/htdocs/degree_days/weighted/daily_data/{}/Population.Heating.txt".format(i), delimiter="|", skiprows=[0,1,2])
        y = y.set_index('Region')
        result = pd.concat([dataframe,y], axis=1)
        dataframe = result

        avgInput(i, y, jan, dec, avgMonth)
    return(dataframe, np.asarray(jan), np.asarray(dec), np.asarray(avgMonth))
