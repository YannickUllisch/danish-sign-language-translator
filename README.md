# Danish Sign Language Translation
## Overview
This project aims to translate Danish Sign Language into text by analyzing video data. We explore and compare the effectiveness of different data extraction techniques, specifically MediaPipe and Unity-VR, and various machine learning models to determine the most accurate setup for sign language translation.

## Key Features
- Data Extraction: Utilizes MediaPipe and Unity-VR for landmark representation from video data.
- Machine Learning Models: Employs models including k-nearest neighbors, Random Forest, and neural networks (RNNs and LSTMs) for sign language translation.
- Data Smoothing: Applies low-pass filters and interpolation for data preprocessing.
- Dimensionality Reduction: Utilizes PCA and UMAP for efficient data analysis.


## Dataset
The dataset comprises professional-grade videos collected from tegnsprog.dk and matcen.dk, along with additional videos recorded to cover a subset of 9 signs from Danish Sign Language.
