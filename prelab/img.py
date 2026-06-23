import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    # 1. Image Loading
    # OpenCV loads images in BGR format by default, not RGB!
    img_path = 'sample.jpg' 
    img = cv2.imread(img_path)
    
    if img is None:
        print(f"Error: Could not load image from '{img_path}'. Check the filename.")
        return

    # 2. Image Properties
    print("--- Image Properties ---")
    print(f"Data Type: {img.dtype}")
    # shape returns (height, width, channels)
    height, width, channels = img.shape
    print(f"Dimensions: {width}x{height}")
    print(f"Number of Channels: {channels}")
    print(f"Total Pixels: {img.size}\n")

    # 3. Color Channels (Splitting)
    # Remember OpenCV is BGR
    b, g, r = cv2.split(img)

    # 4. Image Display (Using Matplotlib & OpenCV)
    # Because OpenCV uses BGR, we must convert to RGB for Matplotlib to display correct colors
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img_rgb)
    plt.title("Original Image (RGB)")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(g, cmap='gray')
    plt.title("Green Channel (Grayscale)")
    plt.axis('off')
    
    print("Displaying Matplotlib window... Close it to proceed to webcam test.")
    plt.show()

    # 5. Webcam Access & Video Capture
    print("Opening Webcam... Press 'q' to exit the video stream.")
    # '0' is usually the built-in webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to grab frame.")
            break

        # Display the live video stream in an OpenCV window
        cv2.imshow('Startup Vision System - Live Feed', frame)

        # Break the loop when 'q' key is pressed
        # 0xFF ensures compatibility across different OS/keyboards
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup: Release the camera and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
    print("Environment test complete!")

if __name__ == "__main__":
    main()