import cv2
import os

def detect_faces_in_image(image_path, output_dir="output"):
    """Detect faces in a static image using OpenCV Haar Cascades"""
    
    # Load the cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image at {image_path}")
        return
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    print(f"Detected {len(faces)} face(s) in the image!")
    
    # Draw rectangles around faces
    for i, (x, y, w, h) in enumerate(faces):
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 3)
        cv2.putText(image, f'Face {i+1}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Save the result
    output_path = os.path.join(output_dir, "detected_" + os.path.basename(image_path))
    cv2.imwrite(output_path, image)
    print(f"Result saved to: {output_path}")
    
    # Display the result
    cv2.imshow('Face Detection Result', image)
    print("Press any key to close the window...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return output_path

if __name__ == "__main__":
    # Process the group photo
    image_file = "group photo.jpeg"
    if os.path.exists(image_file):
        detect_faces_in_image(image_file)
    else:
        print(f"Error: {image_file} not found!")
