from importing import main, two_dplot, three_dplot
import sys
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objs as go
import peakutils


def baseline(specdata):
    """For a single spectrum: Performs a baseline-identifying algorithm
    from -m peakutils, corrects, and plots"""
    #indices, midpoint_spectrum = peakfind() # obtain midpoint peak data

    # execute the baseline-identifier on this spectrum
    baseline_values = peakutils.baseline(specdata)

    # print the correction for validation
    original_spectrum = go.Scatter(      # show original spectrum
        x=[j for j in range(len(specdata))],
        y=specdata,
        mode='lines',
        name='Abs spectrum of the midpoint-time in kinetic series'
    )

    baseline = go.Scatter(      # show baseline
        y=baseline_values,
        x=[j for j in range(len(specdata))],
        mode='markers',
        marker=dict(
            size=3,
            color='rgb(255,0,0)',
            symbol='ope-circle'
        ),
        name='Basline values'
    )

    corrected_spectrum = go.Scatter(        # show baseline correction
        y=specdata - baseline_values,
        x=[j for j in range(len(specdata))],
        mode='lines',
        marker=dict(
            color='rgb(155,100,0)',
        ),
        name='Basline subtracted'
    )

    data = [original_spectrum, baseline, corrected_spectrum]     # overlay all three
    return py.plot(data)


def series_baseline(seriesdata):
    """For a spectral series: Performs a baseline-identifying algorithm
    from -m peakutils, and corrects"""

    df = main(seriesdata)
    df.set_index('0', inplace = True)
    baseline_series = df.copy()     # make a deep copy to the dataframe
    corrected_spectra = df.copy()   # make a deep copy to the dataframe

    for i in xrange(len(df.iloc[0,:])):     # execute baseline-identifier algorithm by column
        baseline_series.iloc[:,i] = peakutils.baseline(df.iloc[:,i])
    corrected_spectra = df - baseline_series    # subtract from original spectra to find correction

    return baseline_series, corrected_spectra


def midpoint_spectrum(specdata):
    """Finds the midpoint-in-time spectrum from a spectral series"""
    midpoint = (len(specdata.iloc[0,:]))/2    # find the mid-timepoint
    midpoint_spectrum = specdata.iloc[:, midpoint]    # find the midpoint spectrum
    return midpoint_spectrum


def peakfind(specdata, threshold = 0.02):
    """Finds major/minor peaks according to threshold values; Threshold
    value is divided by max peak height"""

    if not isinstance(specdata, pd.DataFrame):  # check datatype
        specdata = main(specdata)
        specdata.set_index('0', inplace = True)   #reset index as time-series
    else:
        pass

    # exectue the peak finding on this spectrum
    indices = peakutils.indexes(midpoint_spectrum, thres=threshold/max(midpoint_spectrum))
    return indices


def peakshow():
    """Plots peaks found in peakfind"""
    indices, midpoint_spectrum = peakfind() # obtain midpoint peak data

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
    return py.plot(data)


def series_peakfind(specdata, threshold = 0.05):
    if not isinstance(specdata, pd.DataFrame):  # check datatype
        specdata = main(specdata)
        specdata.set_index('0', inplace = True)   #reset index as time-series
    else:
        pass

    indexes=[]
    for i in xrange(len(specdata.iloc[0,:])):     # execute baseline-identifier algorithm by column
        individual_spectrum = specdata.iloc[:,i]
        indexes.append(peakutils.indexes(individual_spectrum, thres = threshold/max(individual_spectrum)))
    # exectue the peak finding on this spectrum
    #indexes = peakutils.indexes(midpoint_spectrum, thres=threshold/max(midpoint_spectrum))
    return indexes


#def series_peakshow(specdata, indexes):    # Next step
    """Plots peaks found in peakfind"""





if __name__ == '__main__':
    #indices, midpoint_spectrum = peakfind()
    #baseline(midpoint_spectrum)
    baseline_series, corrected_spectra = series_baseline(sys.argv[1])

    #two_dplot(sys.argv[1]), two_dplot(baseline_series), two_dplot(corrected_spectra)
    #plt.show()


    #fig = series_peakfind(sys.argv[1])
    #two_dplot(fig)
    #plt.show()
