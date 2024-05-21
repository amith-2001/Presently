import base64
import json

def image_to_base64(image_path):
    """Convert an image to a base64 encoded string."""
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

def save_image_to_json(image_base64, json_path):
    """Save a base64 encoded string to a JSON file."""
    data = {"image": image_base64}
    with open(json_path, 'w') as json_file:
        json.dump(data, json_file)

# Example usage:
image_path = 'uploaded_images/left_slide_2.png'
json_path = 'image_data.json'

# Convert image to base64 string
image_base64 = image_to_base64(image_path)

# Save the base64 string in a JSON file
save_image_to_json(image_base64, json_path)

print(f"Image saved to {json_path} as base64 string.")


def load_image_from_json(json_path, output_image_path):
    """Load a base64 encoded string from a JSON file and decode it to an image."""
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)
    image_base64 = data['image']
    image_data = base64.b64decode(image_base64)
    with open(output_image_path, 'wb') as image_file:
        image_file.write(image_data)

# Example usage:
output_image_path = 'output_image.jpg'
load_image_from_json(json_path, output_image_path)

print(f"Image loaded from {json_path} and saved to {output_image_path}.")
