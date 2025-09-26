# server/server.py
import grpc
from concurrent import futures
import classifier_pb2
import classifier_pb2_grpc
from model.cnn_model import predict  # import our ML model function

class ImageClassifierServicer(classifier_pb2_grpc.ImageClassifierServicer):
    def ClassifyImage(self, request, context):
        # request.image_data is raw bytes, we need to save temporarily
        with open("temp.jpg", "wb") as f:
            f.write(request.image_data)

        label, confidence = predict("temp.jpg")
        return classifier_pb2.ImageReply(label=label, confidence=confidence)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    classifier_pb2_grpc.add_ImageClassifierServicer_to_server(
        ImageClassifierServicer(), server
    )
    server.add_insecure_port("[::]:50051")  # listens on port 50051
    server.start()
    print("Server running on port 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
