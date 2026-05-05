# ARI711S Group Project – Part 3: Traffic Sign Recognition

## How to Run
pip install tensorflow opencv-python scikit-learn
python traffic.py gtsrb model.h5

## Dataset
German Traffic Sign Recognition Benchmark (GTSRB)
- 43 subfolders
- Images resized to 30×30 pixels, normalised to [0,1]

## Hyperparameters
- Epochs: 10
- Batch size: 16
- Optimiser: Adam
- Loss: categorical_crossentropy
- Test size: 40%

## Results
- Final test accuracy: 0.9906
- Confusion matrix: strong diagonal, few misclassifications

## What Worked
- Two conv blocks with max pooling captured spatial features well
- Dropout(0.5) reduced overfitting
- Normalising pixels to [0,1] stabilised training

## What Didn't Work
- Single conv layer underfitted the 43-class problem
- Large batch sizes slowed convergence

## Experimental Notes
- Limiting to 1500 images per class prevented RAM crashes on low-memory machines
- Using float32 instead of uint8 prevented memory issues