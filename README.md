# ```HEADpy``` Library
A frequency-based anomaly detection library for homomorphically encrypted IoT data.

The ```HEADpy``` library offers support build equi-width histograms and to detect anomalies within HE IoT sensor data, based on the distribution of the data, using ```Concrete``` circuits.  


## Structure of the repository
The repository is structured as follows:
- "src/data_preprocessing": includes data preprocessing functionalities and the configuration which allows setting the data source
- "src/histo_building": includes the onfiguration for building the histogram and the histogram building module (```builder```) which is responsible for building both clear and cryptographic equi-width histograms
- "src/anomaly_detection": implements the anomaly detection functionalities within the ```detector``` module and allows setting the anomaly detection configuration parameters
- "src/concrete_aux": includes function-agnostic ```Concrete``` circuits compilation, tesing and checking the results against the results of the corresponding clear function on the same data sample
- "src/examples": includes some code examples of calling the functions within the library on specific data samples
- "doc": includes the library documentation
- "LICENSE"
- "README.md": this file

## Instalation guideline
The framework requires ```Python3``` (version >= 3.8).

Other packages that ```HEADpy``` depends on are ```pandas```, ```matplotlib``` and ```concrete-python```. Therefore, these packagase have to be installed before ```HEADpy``` is installed.

### Installing ```pandas```
```pandas``` can be easily installed using the following command:

```$ pip install pandas```

### Installing ```matplotlib```
The same command can be used to install ```matplotlib```:
```$ pip install matplotlib```

### Installing Concrete
Concrete can be also installed from PyPI:

```pip install -U pip wheel setuptools```

```pip install concrete-python```

After all needed packages are installed, the public repository containing the framework code is cloned in a local directory of user's choice:

```git clone https://github.com/dragoslazea/HEADpy.git```

After installation, all the functionalities provided by the framework are available within the working directory where the user cloned the code of the software.

## References
Hangan, A., Lazea, D., & Cioara, T. (2024). Privacy Preserving Anomaly Detection on Homomorphic Encrypted Data from IoT Sensors. arXiv preprint arXiv:2403.09322. 