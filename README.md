# Job submission package for stomboot cluster at Nikhef

Carlo Fuselli

cfuselli@nikhef.nl
----------------

Adapted from utilix package XENONnT

Very general use, main function is defined in `batch_stbc.py`, the rest is to be configured based on analysis. 

Usage: 

source an environment (or cvmfs) and then: 

```python submmitter.py```


set configs in the `configs/` directory.



Set up `submitter.py` to define what do do for every run etc.. 

Set up `process.py` to do what you need (st.make etc). 
