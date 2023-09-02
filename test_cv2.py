import cv2


image = cv2.imread('path_to_your_image.jpg')


if image is not None:

    cv2.imshow('Test Image', image)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()  

else:
    print('Error: Unable to load the image.')


print('OpenCV version:', cv2.__version__)
