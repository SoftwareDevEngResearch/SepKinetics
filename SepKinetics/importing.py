import sys
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objs as go

""" 04-22-18 - David j Bettinardi - SepKinetics software
This script (so far) imports .csv kinetic data from the Olis CLARiTY
Spectrophotometer and outputs a 3-dimentional visualizerself.
Three datastructure approaches were attempted, current approach
is through -m pandas"""


'''call in terminal with $ python importing.py filename.csv'''


# pandas approach
def main():
    filename = sys.argv[1]
    df = pd.read_csv(filename, index_col=0, header = 0)
    #print df.head(n=1)
    #print df

    #df.iloc[0,0] = 'nm'      # sets first value to wavelength (nm)
    #wavelength = df.ix[:]['0']      # designates first column as wavelength
    #timepoint = [float(i) for i in list(df)]   # set dictionary titles = float of timepoints

    #print df.iloc[:,1]      # prints first spectrum
    #print timepoint
    return df
df = main()


# Make a 2D plot of first spectrum
def two_dplot():
    x = df.iloc[1:,0]
    y = df.iloc[1:,1:]
    print x,y
    plt.plot(x,y)
    plt.show()
#two_dplot()
#print df.iloc[0,1:]
#z = df.iloc[0,1:]
#z = df.head(n=1)
#print z


# Make a 3D plot    # Must goto: Edit in Chart Studio > delete z[0]
def three_dplot():
    data = [go.Surface(z=df.as_matrix(), colorscale='Viridis')]
    #data = [go.Surface(x=x, y=y, z=z)]
    #print data
    fig = go.Figure(data=data)
    py.plot(fig)
three_dplot()


# numpy approach
'''
filename = sys.argv[1]      # read filename.csv from command line
data = np.loadtxt(filename, delimiter=',', skiprows = 1, unpack=True)     # unpack = rows -> columns
wavelength = data[0]        # assigns first column of data = lambda
header = [item[0] for item in data]    # assigns first item in column as header
header[0] = 'wavelength (nm)'

print data
print header

plt.plot(wavelength, data[1, 1:])
'''


# dictionary approach
'''
filename = sys.argv[1]
f = csv.DictReader(open(filename))
f.fieldnames[0] = 'nm'  # makes the first field name represent wavelentgh
timepoint = {x: [] for x in f.fieldnames}   # makes dictionary listed by the collection timepoint starting t=0

for row in f:   # defines the dictionary with each spectrum
    for name in row:
        val = row[name]
        try:                # duck typing to catch input errors
            val = float(val)
            timepoint[name].append(val)
        except ValueError:
            continue

print timepoint     # checks output
'''
