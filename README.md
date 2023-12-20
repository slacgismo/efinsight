# Electrification Futures Insight  <a href="https://zenodo.org/doi/10.5281/zenodo.10413366"><img src="https://zenodo.org/badge/734045844.svg" alt="DOI"></a>

The Electrification Futures Insight project aims to provide the impact of electrification on the load shapes of residential, commercial, industrial, public, and transportation sectors across all U.S. states, for variable electrification adaptation rates for different end-uses, and variable full electrification target years that depend on state and federal policies.

## North American Electrification Loadshape Forecasting
Current EFInsight work is supporting the development of the North American Electrification Loadshape Forecasting tool which can be found [here](https://marimo.io/@gismo/na-electrification-loadshape-forecasting). The tool can also be run locally using [marimo](https://github.com/marimo-team/marimo). 

This tool currently performs loadshape forecasting for residential and commercial buildings using publicly available datasets. Building loadshapes are generated using NREL [ResStock](https://resstock.nrel.gov/) and [ComStock](https://comstock.nrel.gov/) data sets. 

### Methodology 
Coming soon.

### Environment Setup
To run the marimo notebook locally, you'll need to install the dependencies. 

~~~
python3 -m venv .
. bin/activate
pip install -r requirements.txt
~~~

### Run
The app can be run with the simple command
~~~
marimo run app.py
~~~

For more information on editing a marimo notebook, please refer to the marimo documentation.

## How to cite this work
Please see the "Cite this repository" link on the landing page of this repository in the right sidebar for the citation in APA and BibTeX formats.
