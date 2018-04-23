"""Test scipts for importing.py"""
from sepkinetics.importing import main, two_dplot, three_dplot

def test_main():
    df = main()
    assert 0 < df.iloc[0,0] < 1

    timepoints = [float(i) for i in list(df)]
    assert len(timepoints) == 2
#assert test_main.timepoint == 0.004224

def test_three_dplot():
    pass
