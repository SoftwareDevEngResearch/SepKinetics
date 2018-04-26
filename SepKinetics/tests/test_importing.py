"""Test scipts for importing.py"""
#from sepkinetics.importing import main, two_dplot, three_dplot
from .. import importing as im
import os

def test_main():
    fn = os.path.join(os.path.dirname(__file__), 'kintest.csv')
    df = im.main(fn)
    assert 0 < df.iloc[0,0] < 1

    timepoints = [float(i) for i in list(df)]
    assert len(timepoints) == 2
#assert test_main.timepoint == 0.004224

def test_three_dplot():
    pass
