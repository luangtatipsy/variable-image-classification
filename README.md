# Variable Image Classification
A repository to demonstrate handling variable input shapes for image classification

## Datasets
Datasets using on this demonstration are listed by following...
- Fixed-shape Image Classification
  - [Iris Computer Vision](https://www.kaggle.com/jeffheaton/iris-computer-vision)
- Variable-shape Image Classification
  - [Imagenette](https://github.com/fastai/imagenette) (160px)

## Prerequisites
- Python 3.8
- Kaggle account
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
### [Iris Computer Vision](https://www.kaggle.com/jeffheaton/iris-computer-vision)  
In order to download the dataset, it is recommended to use [`kaggle`](https://github.com/Kaggle/kaggle-api) official API for downloading the dataset.
  1. Visit your Kaggle account page (url should be like `https://www.kaggle.com/<your_kaggle_username>/account`)
  2. Scroll to API section, click `Create New API Token` button. After that a `kaggle.json` should be downloaded to your computer
  3. Relocate the `kaggle.json` file to `~/.kaggle/kaggle.json`
For now, you should be able to using kaggle cli
  4. Download the dataset via `kaggle` cli 
  ```sh
  kaggle datasets download -d jeffheaton/iris-computer-vision
  ```
  5. Unzip the downloaded ZIP file to the `datasets` directory
  ```sh
  unzip iris-computer-vision.zip -d datasets/iris-computer-vision
  ```
  6. (Optional) Remove the ZIP file
  ```sh
  rm -f iris-computer-vision.zip
  ```
  7. Split the dataset into training and test sets
  ```sh
  python split_dataset.py
  ```

### [Imagenette](https://github.com/fastai/imagenette)  
  1. Download the dataset
  ```sh
  wget https://s3.amazonaws.com/fast-ai-imageclas/imagenette2-160.tgz
  ```
  2. Extract the downloaded `tgz` file
  ```sh
  tar zxvf imagenette2-160.tgz -C ./datasets
  ```
  3. Rename the directory
  ```sh
  mv ./datasets/imagenette2-160/ ./datasets/imagenette2/
  ```
  4. (Optional) Remove the `tgz` file
  ```sh
  rm -f imagenette2-160.tgz
  ```