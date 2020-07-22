'''
Instructions
- Load the trained file from the data module.
- Initialize the detector cascade with the trained file.
- Detect the faces in the image, setting the minimum size of the searching window to 10 pixels and 200 pixels for the maximum.
'''

# Load the trained file from data
trained_file = data.lbp_frontal_face_cascade_filename()

# Initialize the detector cascade
detector = Cascade(trained_file)

# Detect faces with min and max size of searching window
detected = detector.detect_multi_scale(img = night_image,
                                       scale_factor=1.2,
                                       step_ratio=1,
                                       min_size=(10, 10),
                                       max_size=(200, 200))

# Show the detected faces
show_detected_face(night_image, detected)
