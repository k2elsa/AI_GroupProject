import os
import sys
import cv2
import numpy as np
import random
import tensorflow as tf

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import layers, models

import matplotlib.pyplot as plt

IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def load_data(data_dir):
    images = []
    labels = []

    print(f"Reading data from: {data_dir}")

    for category in os.listdir(data_dir):
        category_path = os.path.join(data_dir, category)

        if not os.path.isdir(category_path):
            continue

        try:
            label = int(category)
        except:
            continue

        count = 0  # optional limit per class

        for img_name in os.listdir(category_path):
            img_path = os.path.join(category_path, img_name)

            img = cv2.imread(img_path)
            if img is None:
                continue

            img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))

            img = img.astype("float32") / 255.0

            images.append(img)
            labels.append(label)

            count += 1
            if count >= 1500:
                break

    return np.array(images, dtype="float32"), np.array(labels)


def get_model():
    model = models.Sequential()
    model.add(layers.Conv2D(
        32, (3, 3), activation='relu',
        input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
    ))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(NUM_CATEGORIES, activation='softmax'))

    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    return model


def plot_confusion_matrix(model, X_test, y_test):
    y_pred = model.predict(X_test)
    y_pred_classes = np.argmax(y_pred, axis=1)
    y_true = np.argmax(y_test, axis=1)

    cm = confusion_matrix(y_true, y_pred_classes)

    plt.figure()
    plt.imshow(cm)
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.colorbar()
    plt.show()


def test_random_image(model, X_test):
    index = random.randint(0, len(X_test) - 1)
    sample = X_test[index]

    prediction = model.predict(np.array([sample]))
    predicted_class = np.argmax(prediction)

    plt.imshow(sample)
    plt.title(f"Predicted Class: {predicted_class}")
    plt.axis('off')
    plt.show()


def main():

    if len(sys.argv) < 2:
        sys.exit("Usage: python traffic.py gtsrb [model.h5]")

    base_dir = sys.argv[1]
    data_dir = os.path.join(base_dir, "Train")

    model_filename = sys.argv[2] if len(sys.argv) == 3 else None

    print("Loading data...")
    images, labels = load_data(data_dir)

    if len(images) == 0:
        sys.exit("ERROR: No images loaded. Check dataset path.")

    print(f"Loaded {len(images)} images.")

    labels = to_categorical(labels, NUM_CATEGORIES)

    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        images, labels, test_size=TEST_SIZE
    )

    print("Building model...")
    model = get_model()

    print("Training model...")
    model.fit(X_train, y_train, epochs=10, batch_size=16)

    print("Evaluating model...")
    loss, accuracy = model.evaluate(X_test, y_test, verbose=2)

    print(f"Model accuracy: {accuracy:.4f}")

    if model_filename:
        model.save(model_filename)
        print(f"Model saved to {model_filename}")

    print("Generating confusion matrix...")
    plot_confusion_matrix(model, X_test, y_test)

    print("Testing random image...")
    test_random_image(model, X_test)


if __name__ == "__main__":
    main()