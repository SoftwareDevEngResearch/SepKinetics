import sys
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objs as go

'''# TODO:
-comment the code more  DONE
-use argv in __main__ or hardcode .csv for testing? DONE
-import .xlsx instead of .csv (comes from clarity as .xlsx)
-save 3D plots as HTML
-fix double importing
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


filename = 'kintest.csv'     # hardcoded for testing; overidden in __main__


# pandas approach [third try]
def main(filename):
    df = pd.read_csv(filename, index_col=0, header = 0) # set column 1 as index; first row as header
    return df


# Make an overlapping 2D plot of wavelength vs. kinetics @ all timepoints
def two_dplot():
    #filename = sys.argv[1]          # reads in again; MUST FIX
    df = pd.read_csv(filename, header = 0)      # reads in again; MUST FIX
    wavelength = df.iloc[1:,0]      # set firts column as wavelength
    absorb = df.iloc[1:,1:]     # set column as absorbances
    plt.plot(wavelength,absorb)
    return plt.show()
two_dplot()


# Make a 3D surface plot with histogram
def three_dplot():
    #filename = sys.argv[1]          # reads in again; MUST FIX
    df = pd.read_csv(filename, index_col=0, header = 0)     # reads in again; MUST FIX
    data = [go.Surface(z=df.as_matrix(), colorscale='Viridis')]     # transform to matrix for surface plot
    fig = go.Figure(data=data)      # make figure
    return py.plot(fig)             # plot figure
three_dplot()


if __name__ == '__main__':

    filename = sys.argv[1]
