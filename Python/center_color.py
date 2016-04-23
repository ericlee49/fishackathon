import cv2

def calculate():

    center_height = 2
    center_width = 2
        
	image = cv2.imread('sample.jpg')
	center_height = image.shape[0]/2
	center_width = image.shape[1]/2
	
	#center_left=image[center_width-10,center_height]
	#center_right=image[center_width+10,center_height]
	#center_top=image[center_width,center_height+10]
	#center_bottom=image[center_width,center_height-10]

	#avg_red = (center_left[2] + center_right[2] + center_top[2] + center_bottom[2])/4
	#avg_green =  (center_left[1] + center_right[1] + center_top[1] + center_bottom[1])/4
	#avg_blue = (center_left[0] + center_right[0] + center_top[0] + center_bottom[0])/4
	
	color = image[center_width,center_height]

	#color = [avg_red, avg_green, avg_blue]
	
	return color
