import cv2

# List of image paths
image_paths = [
    "/Users/rhea/MLPR_Lab5/Plaksha_Faculty.jpg",
    "/Users/rhea/MLPR_Lab5/Dr_Shashi_Tharoor.jpg"
]

# Loop through each image path and check if it's loading
for path in image_paths:
    image = cv2.imread(path)  # Load the image

    if image is None:
        print(f"Error: Could not load image at {path}")
    else:
        print(f"Successfully loaded: {path}")
        cv2.imshow("Loaded Image", image)  
        cv2.waitKey(1000)  # Show each image for 1 second
        cv2.destroyAllWindows()

print("Image verification complete.")

