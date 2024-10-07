from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path):
    # Load the image
    img = Image.open(image_path)
    data = np.array(img)

    # Perform encryption by swapping pixels and applying a basic operation
    height, width, channels = data.shape
    
    # Create a copy of the data for manipulation
    encrypted_data = data.copy()
    
    for i in range(height):
        for j in range(width):
            # Simple operation: Add a constant to pixel values
            encrypted_data[i, j] = (data[i, j] + 50) % 256
            
            # Swap pixel with a simple pattern
            if (i + j) % 2 == 0 and i < height - 1 and j < width - 1:
                encrypted_data[i, j], encrypted_data[i + 1, j + 1] = encrypted_data[i + 1, j + 1], encrypted_data[i, j]
    
    # Save the encrypted image
    encrypted_image = Image.fromarray(encrypted_data)
    encrypted_image.save(output_path)

def decrypt_image(image_path, output_path):
    # Load the image
    img = Image.open(image_path)
    data = np.array(img)

    # Perform decryption
    height, width, channels = data.shape
    decrypted_data = data.copy()

    for i in range(height):
        for j in range(width):
            # Reverse the operation: Subtract the same constant
            decrypted_data[i, j] = (data[i, j] - 50) % 256
            
            # Swap back the pixels according to the same pattern
            if (i + j) % 2 == 0 and i < height - 1 and j < width - 1:
                decrypted_data[i, j], decrypted_data[i + 1, j + 1] = decrypted_data[i + 1, j + 1], decrypted_data[i, j]
    
    # Save the decrypted image
    decrypted_image = Image.fromarray(decrypted_data)
    decrypted_image.save(output_path)

# Example usage
if __name__ == "__main__":
    encrypt_image('input_image.jpg', 'encrypted_image.jpg')
    decrypt_image('encrypted_image.jpg', 'decrypted_image.jpg')
