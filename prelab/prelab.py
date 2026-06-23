import cv2
import numpy as np
import matplotlib.pyplot as plt

def demonstrate_image_basics(image_path):
    print("--- 1. Loading Image & Checking Properties ---")
    # Load an image (Replace with a path to an actual image on your laptop)
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Could not load image. Check the file path.")
        return

    # Image Properties
    # Structure of shape: (Height, Width, Channels)
    dimensions = img.shape
    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2] if len(img.shape) > 2 else 1
    dtype = img.dtype
    
    print(f"Image Shape: {dimensions}")
    print(f"Height: {height}px, Width: {width}px, Channels: {channels}")
    print(f"Data Type: {dtype}\n")

    print("--- 2. Color Channels Split ---")
    # OpenCV loads images in BGR format by default, not RGB!
    b, g, r = cv2.split(img)
    
    # Displaying images using Matplotlib (Requires converting BGR to RGB)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.title("Original (RGB)")
    plt.imshow(img_rgb)
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.title("Red Channel (Grayscale)")
    plt.imshow(r, cmap='gray')
    plt.axis('off')
    
    print("Displaying Matplotlib window... Close it to proceed to live video.")
    plt.show()

def demonstrate_webcam():
    print("\n--- 3. Live Webcam Access & Video Capture ---")
    print("Press 'q' on your keyboard to exit the video stream.")
    
    # 0 is usually the default built-in webcam
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
            
        # Let's do a quick real-time modification (convert to grayscale)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frames in separate windows
        cv2.imshow('Live Webcam (Color)', frame)
        cv2.imshow('Live Webcam (Grayscale Processing)', gray_frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture and destroy windows
    cap.release()
    cv2.closeAllWindows()

if __name__ == "__main__":
    # TODO: Place a sample 'test.jpg' in your folder or update this path
    sample_image = "test.jpg" 
    
    # Run the image analysis
    demonstrate_image_basics(sample_image)
    
    # Run the live webcam demo
    demonstrate_webcam()