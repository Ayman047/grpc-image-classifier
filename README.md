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

   pip install -r requirements.txt

# Running Server

python -m server.server


# Running the Client

python -m client.client



