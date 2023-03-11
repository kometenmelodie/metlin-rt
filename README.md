# METLIN in Python 🐍

The METLIN retention time prediction was first
introduced [here](https://pubmed.ncbi.nlm.nih.gov/31862874/).
Accompanying the paper, the MELTIN data set was published, containing ~80 000
small molecules including retention time.
Using this data, the authors created a neural net to predict the retention
time. The `R` code to create the model proposed in the paper was published
as well.

This is a recreation of the neural net in `Python`. The folder [model](model)
contains the already trained `Keras` model.

## Usage

If you wish to train the model by yourself install
[`poetry`](https://python-poetry.org/docs/#installing-with-pipx) for package
management. `Python = ">=3.10, <3.11"` is recommended for this project.
Install the environment using:

```shell
poetry install
```

Next, execute `get_data.py` which downloads the METLIN data set.
Subsequently, run `calc_fp.py` to calculate the
Morgan fingerprints (the predictors).
Lastly, `train_model.py` trains and saves the neural net.

