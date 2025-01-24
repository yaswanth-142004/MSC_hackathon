from google.cloud import vision
import io

print("Script started")

# Initialize the client
try:
    client = vision.ImageAnnotatorClient.from_service_account_file('./key.json')
    print("Client initialized successfully.")
except Exception as e:
    print(f"Failed to initialize client: {e}")
    exit()

# Path to the image
image_path = 'im.jpg'
print(f"Image path: {image_path}")

# Read the image file
try:
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    print("Image file read successfully.")
except FileNotFoundError:
    print(f"Error: The file '{image_path}' was not found.")
    exit()
except Exception as e:
    print(f"Error reading the image file: {e}")
    exit()

# Create the vision.Image object
image = vision.Image(content=content)

# Perform text detection
try:
    response = client.text_detection(image=image)
    print("Text detection completed.")

    # Check for API errors
    if response.error.message:
        print(f"API Error: {response.error.message}")
        exit()

    # Print detected text
    if response.text_annotations:
        print("Detected text:")
        for text in response.text_annotations:
            print(f"- {text.description}")
    else:
        print("No text detected in the image.")
except Exception as e:
    print(f"Error during text detection: {e}")
