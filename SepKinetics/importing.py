import sys
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objs as go

'''# TODO:
-use argv in __main__ or hardcode .csv for testing?
-fix 2D plotting re: import
-fix 3D y-axis
-add axis labels
-add monocolor histogram for 2D plot
-add plotting series of histograms (see PythonProject folder in chrome)
'''

""" 04-22-18 - David j Bettinardi - SepKinetics software
The script imports .csv kinetic data from the Olis CLARiTY
spectrophotometer and outputs 2D and 3D visualizers.
Three datastructure approaches were attempted; current approach
uses dataframes in -m pandas"""


'''call in terminal using $ python importing.py filename.csv'''

filename = 'kintest.csv'        # not overwritten in __main__

# pandas approach [third try]
def main():
    #filename = sys.argv[1]      # command prompt argument 1

    df = pd.read_csv(filename, index_col=0, header = 0) # set column 1 as index; first row as header
    #t = df.head(n=1)
    #print df.iloc[0,0]
    #timepoint = [float(i) for i in list(df)]
    # df

    #df.iloc[0,0] = 'nm'      # sets first value to wavelength (nm)
    #wavelength = df.ix[:]['0']      # designates first column as wavelength
    #timepoint = [float(i) for i in list(df)]   # set dictionary titles = float of timepoints

    #print df.iloc[:,1]      # prints first spectrum
    #print timepoint
    return df
df = main()



# Make an overlapping 2D plot of all spectra
def two_dplot():        # BROKEN FUNCTION
    #filename = sys.argv[1]
    #df = pd.read_csv(filename, header = 0)
    wavelength = df.iloc[1:,0]
    absorb = df.iloc[1:,1:]
    #print wavelength, abs

    plt.plot(wavelength,absorb)
    return plt.show()
#two_dplot()
#print df.iloc[0,1:]
#z = df.iloc[0,1:]
#z = df.head(n=1)
#print z


# Make a 3D plot
def three_dplot():
    data = [go.Surface(z=df.as_matrix(), colorscale='Viridis')]
    #data = [go.Surface(x=x, y=y, z=z)]
    #print data
    fig = go.Figure(data=data)

    #return py.plot(fig)
three_dplot()



# numpy approach [second try]
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


# dictionary approac [first try]
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

if __name__ == '__main__':

    filename = sys.argv[1]
