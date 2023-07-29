# FishBreedPrediction
# FishBreedPrediction

FishBreedPrediction is a machine learning project that aims to predict the species of fish based on various features. This repository contains the code and resources for building and evaluating the fish breed prediction model.

## Dataset

The dataset used for this project can be accessed from the following link: [Fish Dataset](https://raw.githubusercontent.com/niravpatidar37/Data/main/Fish.csv)

The dataset contains the following features:
- Weight: Weight of the fish (numeric)
- Length1: Vertical length of the fish (numeric)
- Length2: Diagonal length of the fish (numeric)
- Length3: Cross length of the fish (numeric)
- Height: Height of the fish (numeric)
- Width: Width of the fish (numeric)
- Species: The target variable indicating the species of the fish (categorical)

## Installation

To run the code, you need to have the following libraries installed:

- Python (version 3.9.13)
- Numpy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

You can install the required libraries using pip:

```bash
pip install -r requirements.txt

### Model
For the fish breed prediction, a Random Forest Classifier is used. The model is trained on the training data to predict the species of fish based on the provided features.
