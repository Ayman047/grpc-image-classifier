# gRPC Image Classifier

A Python gRPC service that classifies images using a pretrained MobileNet model.  
Demonstrates **client-server communication** via gRPC and real-time **ML inference**.

---

## Features

- Upload images from client → server classifies them.
- Uses TensorFlow MobileNet pretrained on ImageNet.
- Shows predictions (label + confidence) on client terminal.
- Demonstrates the power of gRPC for remote procedure calls.

---

## Directory Structure

grpc-image-classifier/
├── proto/
│   └── classifier.proto        # gRPC service definition
├── server/
│   └── server.py               # gRPC server
├── client/
│   └── client.py               # gRPC client
├── model/
│   └── cnn_model.py            # Pretrained MobileNet loader
├── requirements.txt            # Python dependencies
├── README.md
└── .gitignore

---

## Installation

1. Clone the repo:

```bash
git clone https://github.com/Ayman047/grpc-image-classifier.git
cd grpc-image-classifier
```

2. Install Independencies
```bash
   pip install -r requirements.txt
```
# Running Server

```bash
python -m server.server
```

# Running the Client

```bash
python -m client.client
```

# Testing with Images

1. Place your images in a folder, e.g., test_images/ (optional).
2. Supported formats: JPG, PNG.
3. When running the client, provide the full path to any image you want to classify.
4. The server will handle the ML inference and return the prediction to the client.

# Example
``` bash
Client input: dog.jpg
Prediction: golden_retriever
Confidence: 0.89
```
