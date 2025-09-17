# 🚗DS-Number-Plate-Recognition📃

#### In this project, we have build a system that can detect and recognize license plate numbers from images or real-time video feeds. This system can be applied to automate toll collection, monitor traffic violations, and enhance public security

### Skills take away From This Project

    Image Preprocessing (grayscale, thresholding, edge detection)

    Contour Detection & Morphology

    Optical Character Recognition (OCR) with Tesseract

    Real-Time Object Detection (OpenCV)

    Region of Interest (ROI) Detection

### Approach:
    
    1 Data Collection
      
      ●	We can use publicly available license plate datasets
      
      ●	Can also simulate with a custom image dataset

    2. Image Preprocessing
      
      ●	Converted to grayscale
      
      ●	Used Canny edge detection and morphological operations
      
      ●	Extracted contours and identify rectangular regions likely to be license plates

    3. Region of Interest (ROI)
      
      ●	Detected bounding box with aspect ratio filtering
      
      ●	Cropped the image to the plate area

    4. Character Recognition
      
      ●	Used Tesseract OCR to extract alphanumeric characters

    5. Real-Time Detection
      
      ●	Used OpenCV to process video frames in real time
      
      ●	Annotate frames with bounding boxes and recognized plate numbers

    6. Deployment
      
      ●	Built a simple GUI using a web app with Streamlit

### Results: 
    
    Successfully recognized plate numbers with 85–90% character accuracy in standard lighting


    
