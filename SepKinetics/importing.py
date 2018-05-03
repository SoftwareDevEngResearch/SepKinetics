import sys
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objs as go
import peakutils

'''# TODO:
-add autobaseline correction
-check Martin's disseration for deconvolution
-add more tests
-add google style comments to code
-import .xlsx instead of .csv (comes from clarity as .xlsx)?
-save 3D plots as HTML?
-fix double importing -- FIXED
-fix peakfinding x-axis
-add 2D peak labels
-fix 3D y-axis
-add monocolor histogram for 2D plot  -- ADDED
-add peak finding function -- ADDED
-add plotting series of histograms (see PythonProject folder in chrome)
'''

""" 04-22-18 - David j Bettinardi - SepKinetics software
The script imports .csv kinetic data from the Olis CLARiTY
spectrophotometer and outputs 2D and 3D visualizers.
Three datastructure approaches were attempted; current approach
uses dataframes in -m pandas"""

'''call in terminal using $ python importing.py filename.csv'''

filename = 'kintest.csv'    # for test_functions, overridden in main

# pandas approach [third try]
def main(file):
    """Creates dataframe with top row and first column as headers"""
    df = pd.read_csv(file, header = 0) # first row as header
    return df


def two_dplot():
    """Makes an overlapping 2D plot of wavelength vs. kinetics @ all timepoints"""
    try:        # duck typing to allow test_function exceptions
        filename = sys.argv[1]
    except:
        filename = 'kintest.csv'
    df = main(filename)
    df.set_index('0', inplace = True)   #reset index as time-series
    df.plot(legend=False, colormap = 'coolwarm')
    return plt.show()
#two_dplot()


def three_dplot():
    """Makes a 3D surface plot"""
    try:        # duck typing to allow test_function exceptions
        filename = sys.argv[1]
    except:
        filename ='kintest.csv'
    df = main(filename)
    df2 = df.set_index('0')

    y = df.iloc[:,0].tolist()   # attempt to overwrite y-axis

    '''Working plotter, wrong y-axis!'''
    data = [go.Surface(z=df2.as_matrix(), y=y, colorscale='Viridis')]     # transform to matrix for surface plot

    layout = go.Layout(
                    scene = dict(
                    xaxis = dict(
                        title='Time (s)'),
                    yaxis = dict(
                        title='Wavelength (nm)'),
                    zaxis = dict(
                        title='Abs'),),
                    width=700,
                  )
    fig = go.Figure(data=data, layout=layout)
    return py.plot(fig)
#three_dplot()


def peakfind():
    """Finds major/minor peaks"""
    try:        # duck typing to allow test_function exceptions
        filename = sys.argv[1]
    except:
        pass
    df = main(filename)
    df.set_index('0', inplace = True)   # reset index as time-series
    midpoint = (len(df.iloc[0,:]))/2    # find the mid-timepoint
    midpoint_spectrum = df.iloc[:, midpoint]    # find the midpoint spectrum
    # deploy peak findning on this spectrum
    indices = peakutils.indexes(midpoint_spectrum, thres=0.02/max(midpoint_spectrum))
    return indices, midpoint_spectrum


def peakshow():
    indices, midpoint_spectrum = peakfind() # obtain peak data

    # trace the midpoint spectrum
    spectrum = go.Scatter(
        x=[j for j in range(len(midpoint_spectrum))],
        y=midpoint_spectrum,
        mode='lines',
        name='Abs spectrum of the midpoint-time in kinetic series'
    )

    # mark the peaks
    peaks = go.Scatter(
        x=indices,
        y=[midpoint_spectrum.iloc[j] for j in indices],
        mode='markers',
        marker=dict(
            size=8,
            color='rgb(255,0,0)',
            symbol='cross'
        ),
        name='Detected Peaks'
    )

    data = [spectrum, peaks]
    py.plot(data)
    return plt.show()
#peakshow()

#def peakkinetics():



if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except:
        raise ValueError('Specify the .csv you wish to import')
