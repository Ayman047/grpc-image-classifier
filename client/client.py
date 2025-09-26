# client/client.py
import grpc
import classifier_pb2
import classifier_pb2_grpc

def run():
    # Connect to the server
    channel = grpc.insecure_channel("localhost:50051")
    stub = classifier_pb2_grpc.ImageClassifierStub(channel)

    # Read image file
    image_path = "test_images/trial3.jpg"  # path to your image
    with open(image_path, "rb") as f:
        image_bytes = f.read()

    # Create request
    request = classifier_pb2.ImageRequest(image_data=image_bytes)

    # Call gRPC service
    response = stub.ClassifyImage(request)
    print(f"Predicted label: {response.label}")
    print(f"Confidence: {response.confidence:.2f}")

if __name__ == "__main__":
    run()
