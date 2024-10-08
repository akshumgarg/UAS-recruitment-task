# This program is to calculate the priority of houses in photos clicked by UAV

import cv2
import numpy as np


# The following function will help to find the required details(as asked in the task) so that it can be stored in list later.
def image_triangles(image):

    # Within this function, we are making another function which will calculate the number of triangles in the given image(img)
    def getTriangles(img):
        
        canny = cv2.Canny(img, 30, 150, 3)

        blur = cv2.GaussianBlur(canny, (11,11), 0)

        dilated = cv2.dilate(blur, (1, 1), iterations=0)

        i = 0
        (cnt, hierarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for cnt in cnt:
            area = cv2.contourArea(cnt)
            if area >= 1500 and area <= 1800:
                i = i + 1

        return i


    # To complete the task, we will calculate the triangles in burnt area and green area separately.
    # To do this, we need separate masks of burnt part and green part both.
    hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # We will need lower and upper limit of both brown and green color so that they can be separated out completely.
    # We are taking limits of red color also because we will separate red triangles as well so that other required data can be calculated easily. It will be clear further.
    lower_brown = np.array([2, 0, 0])                       
    upper_brown = np.array([30, 255, 255])

    lower_green = np.array([33, 0, 0])
    upper_green = np.array([110, 255, 255])

    lower_red = np.array([0, 255, 255])
    upper_red = np.array([0, 255, 255])

    # Masks for the image are formed below.
    mask_brown = cv2.inRange(hsvImage, lower_brown, upper_brown)
    mask_green = cv2.inRange(hsvImage, lower_green, upper_green)
    mask_red = cv2.inRange(hsvImage, lower_red, upper_red)

    # Hb and Hg are number of burnt and green triangles respectively.
    Hb = getTriangles(mask_brown)
    Hg = getTriangles(mask_green)

    '''A new variable image_ is made. As done below, brown mask and red mask are added. The number of triangles in this image
    is equal to number of burnt blue houses + green red houses'''
    image_ = mask_brown + mask_red

    burnt_blue_green_red = getTriangles(image_)
    total_red = getTriangles(mask_red)

    # Here, we are calculating all the required data by solving the simple mathematical equations.
    # The formulas used below were calculated using mathematical equations on paper.
    burnt_red = (Hb - burnt_blue_green_red + total_red)/2
    burnt_blue = Hb - burnt_red
    green_red  = total_red - burnt_red
    green_blue = Hb + Hg - (burnt_red + burnt_blue + green_red)

    Pb = (2 * burnt_blue) + burnt_red                   # Pb refers to priority of burnt houses
    Pg = (2 * green_blue) + green_red                   # Pg refers to priority of green houses
    Pr = Pb/Pg                                          # Pr is the priority ratio

    # The following part will change brown and green color to different colors (as asked in the task)
    image[mask_brown > 0] = (230, 216, 173)             
    image[mask_green > 0] = (0, 255, 255)

    return Hb, Hg, Pb, Pg, Pr, image


# We have made our required functions, now we will store all the images in the variables as done below.
img1 = cv2.imread("test images/1.png")
img2 = cv2.imread("test images/2.png")
img3 = cv2.imread("test images/3.png")
img4 = cv2.imread("test images/4.png")
img5 = cv2.imread("test images/5.png")
img6 = cv2.imread("test images/6.png")
img7 = cv2.imread("test images/7.png")
img8 = cv2.imread("test images/8.png")
img10 = cv2.imread("test images/10.png")
img11 = cv2.imread("test images/11.png")

# The values returned by the image_triangles() function are stored inseparate variables for each image.
Hb1, Hg1, Pb1, Pg1, Pr1, image1 = image_triangles(img1)
Hb2, Hg2, Pb2, Pg2, Pr2, image2 = image_triangles(img2)
Hb3, Hg3, Pb3, Pg3, Pr3, image3 = image_triangles(img3)
Hb4, Hg4, Pb4, Pg4, Pr4, image4 = image_triangles(img4)
Hb5, Hg5, Pb5, Pg5, Pr5, image5 = image_triangles(img5)
Hb6, Hg6, Pb6, Pg6, Pr6, image6 = image_triangles(img6)
Hb7, Hg7, Pb7, Pg7, Pr7, image7 = image_triangles(img7)
Hb8, Hg8, Pb8, Pg8, Pr8, image8 = image_triangles(img8)
Hb10, Hg10, Pb10, Pg10, Pr10, image10 = image_triangles(img10)
Hb11, Hg11, Pb11, Pg11, Pr11, image11 = image_triangles(img11)

# All the list asked in the task are formed below.
n_houses = [[Hb1, Hg1], [Hb2, Hg2], [Hb3, Hg3], [Hb4, Hg4], [Hb5, Hg5], [Hb6, Hg6], [Hb7, Hg7], [Hb8, Hg8], [Hb10, Hg10],[Hb11, Hg11]]

priority_houses = [[Pb1, Pg1], [Pb2, Pg2], [Pb3, Pg3], [Pb4, Pg4], [Pb5, Pg5], [Pb6, Pg6], [Pb7, Pg7], [Pb8, Pg8], [Pb10, Pg10],[Pb11, Pg11]]

priority_ratio = [Pr1, Pr2, Pr3, Pr4, Pr5, Pr6, Pr7, Pr8, Pr10, Pr11]

print("n_houses = ", n_houses)
print("priority_houses = ",priority_houses)
print("priority_ratio = ", priority_ratio)

# We will sort the priority_ratio list in descending order by the following
priority_ratio.sort(reverse = True)


print("priority_order = ", priority_ratio)

i=0
while (i < len(priority_ratio)):
    if priority_ratio[i] == Pr1:
        priority_ratio[i] = "image1"

    elif priority_ratio[i] == Pr2:
        priority_ratio[i] = "image2"

    elif priority_ratio[i] == Pr3:
        priority_ratio[i] = "image3"

    elif priority_ratio[i] == Pr4:
        priority_ratio[i] = "image4"

    elif priority_ratio[i] == Pr5:
        priority_ratio[i] = "image5"

    elif priority_ratio[i] == Pr6:
        priority_ratio[i] = "image6"

    elif priority_ratio[i] == Pr7:
        priority_ratio[i] = "image7"

    elif priority_ratio[i] == Pr8:
        priority_ratio[i] = "image8"

    elif priority_ratio[i] == Pr10:
        priority_ratio[i] = "image10"

    elif priority_ratio[i] == Pr11:
        priority_ratio[i] = "image11"

    else:
        break

    i = i + 1

print("image_by_rescue_ratio = ", priority_ratio)

# As asked in the task, the required output is shown below.
cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
cv2.imshow("image3", image3)
cv2.imshow("image4", image4)
cv2.imshow("image5", image5)
cv2.imshow("image6", image6)
cv2.imshow("image7", image7)
cv2.imshow("image8", image8)
cv2.imshow("image10", image10)
cv2.imshow("image11", image11)
cv2.waitKey(0)
