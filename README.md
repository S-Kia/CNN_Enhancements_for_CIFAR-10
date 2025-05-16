# CNN-Enhancements-for-CIFAR-10

This project presents an optimized convolutional neural network (CNN) image classifier for the CIFAR-10 dataset, enhanced with techniques such as data augmentation, residual connections, Squeeze-and-Excitation (SE) blocks, vision transformers, and RDNet architecture. Each enhancement was benchmarked to evaluate its impact on performance and generalization. The final model was deployed on a NAO humanoid robot to demonstrate real-world robotic vision.

> Inspired by state-of-the-art approaches from [PapersWithCode CIFAR-10 Leaderboard](https://paperswithcode.com/sota/image-classification-on-cifar-10).

## CNN Enhancements

* Run and experiment using the provided `.ipynb` notebooks.
* Each method (e.g., RES, SE, ViT, RDNet) includes training results and explanation within the notebook or report.

## NAO Robot Integration

**Requirements:**

* **Python 2.7** (for NAOqi):

  ```bash
  pip install opencv-python numpy
  ```

  Download NAOqi SDK:
  [https://aldebaran.com/en/support/kb/nao6/downloads/nao6-software-downloads/](https://aldebaran.com/en/support/kb/nao6/downloads/nao6-software-downloads/)

* **Python 3** (for CNN model):

  ```bash
  pip install opencv-python numpy tensorflow
  ```

## How to Run

1. Change the robot IP in:

   * `get_camera_deep_vision.py`
   * `speak_deep_vision.py`
2. Run the main server:

   ```bash
   python3 server_deep_vision.py
   ```

## Demonstration

Watch the project in action: [https://youtu.be/LkIkpS1hw5o](https://youtu.be/N8_Houm--WY)
