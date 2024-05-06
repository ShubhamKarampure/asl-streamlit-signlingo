## Overview
Signlingo is a web application designed to help individuals learn and practice ASL sign alphabets. Powered by cutting-edge technology, Signlingo utilizes OpenCV for image processing and MediaPipe for action detection, ensuring an accurate and seamless learning experience. It provides interactive lessons, real-time feedback, engaging practice sessions, and progress tracking.

## Features
- Interactive lessons
- Real-time feedback
- Engaging practice sessions
- Progress tracking

## Requirements
- Python version 3.10.0

## Installation
1. Clone the repository.
2. Navigate to the project directory.
3. Install dependencies from `requirements.txt` using:
   ```
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```
   streamlit run Signlingo.py
   ```

## Contribution
Contributions are welcome! Feel free to submit pull requests or open issues.

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
