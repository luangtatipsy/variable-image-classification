# Variable Image Classification
A repository to demonstrate handling variable input shapes for image classification

## Dataset
[Imagenette](https://github.com/fastai/imagenette) dataset with 160px version is used to demonstrated in this repository.
## Prerequisites
- Python 3.8
- wget
## Setup
0. Clone the repository
```sh
git clone https://github.com/luangtatipsy/variable-image-classification.git
cd variable-image-classification
```
1. Create and activate a virtual environment for Python _(recommended)_. If you do not prefer using a virtual environment, skip to step 4.
```sh
python -m venv env
source env/bin/activate
```
2. Update pip to latest version
```sh
python -m pip install --upgrade pip
```
3. Install requirements
```sh
python -m pip install -r requirements.txt
```

## Dataset Preparation
### [Imagenette](https://github.com/fastai/imagenette)  
  1. Download the dataset
  ```sh
  wget https://s3.amazonaws.com/fast-ai-imageclas/imagenette2-160.tgz
  ```
  2. Extract the downloaded `tgz` file
  ```sh
  mkdir datasets && tar zxvf imagenette2-160.tgz -C ./datasets
  ```
  3. Rename the directory
  ```sh
  mv ./datasets/imagenette2-160/ ./datasets/imagenette2/
  ```
  4. (Optional) Remove the `tgz` file
  ```sh
  rm -f imagenette2-160.tgz
  ```
  
 ## Training an Image Classification Model
[`01-train.ipynb`](https://github.com/luangtatipsy/variable-image-classification/blob/main/01-train.ipynb) notebook is used to train the fixed and variable input shape image classification model with the downloaded data. 

## Pre-trained Model
Pre-trained models can be download by the following... 
- [fixed-imagenette2.h5](https://www.dropbox.com/s/na4pn0wggcdbjjb/fixed-imagenette2.h5)
- [variable-imagenette2.h5](https://www.dropbox.com/s/mbw0jdb86s0xw1a/variable-imagenette2.h5)

Place the models to `models` directory or run the commands below..
```sh
wget https://www.dropbox.com/s/na4pn0wggcdbjjb/fixed-imagenette2.h5 -O models/fixed-imagenette2.h5
wget https://www.dropbox.com/s/mbw0jdb86s0xw1a/variable-imagenette2.h5 -O models/variable-imagenette2.h5
```
  
  ## License
This repository is distributed under [MIT License](https://github.com/luangtatipsy/variable-image-classification/blob/main/LICENSE)
