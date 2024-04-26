# SIGNLINGO

## Description
SignLingo is an innovative web application designed for individuals who are mute or communicate primarily through sign language. Similar to popular language learning platforms like DuoLingo, SignLingo aims to provide an interactive and engaging way for users to learn and practice sign language.

## Requirements

Apart from having Django installed, the following steps are required to set up the environment for this project:

1. **Create Virtual Environment:**
   ```bash
   conda create -n py310 python=3.10
   ```

2. **Activate Virtual Environment:**
   ```bash
   conda activate py310
   ```

3. **Install CUDA for TensorFlow-GPU:**
   ```bash
   conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
   ```
   *(This step is necessary if you intend to use TensorFlow with GPU acceleration.)*

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

## Usage
To start the application, run the following command:
 ```bash
  python manage.py runserver
   ```
Once the server is running, you can access SignLingo at http://localhost:8000 in your web browser.
