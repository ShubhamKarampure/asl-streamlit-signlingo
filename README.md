# SignLingo

## Description
SignLingo is an innovative web application designed for individuals who are mute or communicate primarily through sign language. Similar to popular language learning platforms like DuoLingo, SignLingo aims to provide an interactive and engaging way for users to learn and practice sign language.

## Requirements

To set up the environment for this project, follow these steps:

1. **Create Virtual Environment:**  
   ```bash
   conda create -n py310 python=3.10
   ```

2. **Activate Virtual Environment:**  
   ```bash
   conda activate py310
   ```

3. **Install CUDA for TensorFlow-GPU (Optional):**  
   If you intend to use TensorFlow with GPU acceleration, install CUDA and cuDNN:
   ```bash
   conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
   ```

## Install Dependencies

Install the following dependencies using `pip`:

1. **TensorFlow:**  
   ```bash
   python -m pip install "tensorflow<2.11"
   ```

2. **OpenCV:**  
   ```bash
   pip install opencv-python
   ```

3. **Mediapipe:**  
   ```bash
   pip install mediapipe==0.8.11
   ```

4. **Scikit-Learn:**  
   ```bash
   pip install scikit-learn
   ```

5. **Matplotlib:**  
   ```bash
   pip install matplotlib
   ```

5. **Pandas**  
   ```bash
   pip install pandas
   
   ```

5. **MySQL Connector**
   ```bash
   pip install mysql-connector-python

   ```

## Usage

To start the application, run the following command in your terminal:
```bash
streamlit run Homepage.py
```
