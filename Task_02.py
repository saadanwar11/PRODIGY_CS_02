import cv2 as cv2
import numpy as np

def encrypt_image(image, method):
  """Encrypts an image using a specified method.

  Args:
    image: The image to be encrypted.
    method: The encryption method to use.

  Returns:
    The encrypted image.
  """

  if method == "swap_pixels":
    rows, cols, _ = image.shape
    for i in range(0, rows, 2):
      for j in range(0, cols, 2):
        image[i, j], image[i+1, j+1] = image[i+1, j+1], image[i, j]
  elif method == "add_constant":
    image += 50
  elif method == "multiply_constant":
    image *= 0.8

  return image

def decrypt_image(image, method):
  """Decrypts an image using a specified method.

  Args:
    image: The encrypted image.
    method: The decryption method to use.

  Returns:
    The decrypted image.
  """

  if method == "swap_pixels":
    rows, cols, _ = image.shape
    for i in range(0, rows, 2):
      for j in range(0, cols, 2):
        image[i, j], image[i+1, j+1] = image[i+1, j+1], image[i, j]
  elif method == "add_constant":
    image -= 50
  elif method == "multiply_constant":
    image /= 0.8

  return image

def main():
  while True:
    print("Image Encryption/Decryption")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
      image_path = input("Enter the path to the image: ")
      image = cv2.imread(image_path)
      print("Available encryption methods:")
      print("1. Swap pixels")
      print("2. Add constant")
      print("3. Multiply constant")
      method = int(input("Enter the encryption method: "))
      encrypted_image = encrypt_image(image, method)
      cv2.imwrite("encrypted_image.jpg", encrypted_image)
      print("Image encrypted successfully.")
    elif choice == 2:
      image_path = input("Enter the path to the encrypted image: ")
      image = cv2.imread(image_path)
      print("Available decryption methods:")
      print("1. Swap pixels")
      print("2. Add constant")
      print("3. Multiply constant")
      method = int(input("Enter the decryption method: "))
      decrypted_image = decrypt_image(image, method)
      cv2.imwrite("decrypted_image.jpg", decrypted_image)
      print("Image decrypted successfully.")
    elif choice == 3:
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()