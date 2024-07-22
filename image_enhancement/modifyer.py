import cv2

image= cv2.imread('//home//jose//Downloads//image_enhancement//images//image1.jpg')

cv2.line(image, (0,0),(3500,4500),(0,255,0),30)

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)


resized = ResizeWithAspectRatio(image, width=500) 
cv2.imshow('image2',resized)
cv2.imwrite('image2.jpg',image)
cv2.waitKey(0)
cv2.destroyAllWindows()