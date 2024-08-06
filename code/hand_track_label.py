import cv2
import sys

# Create a VideoCapture object and read from input file
video_name="sleeping"
cap = cv2.VideoCapture("C:/Users/buikh/OneDrive/Documents/ET1_BKH/NCKH/Action recognition in video/CODE/dataset/sleeping/video_test/sleeping.mp4")
# Check if camera opened successfully
if (cap.isOpened()== False):
	print("Error opening video file " + video_name)
width_img = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width_img)
height_img = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height_img)  

# read text
result_track = []
with open ("C:/Users/buikh/OneDrive/Documents/ET1_BKH/NCKH/Action_recognition_in_video/CODE/dataset/sleeping/result_track/sleeping.txt", "r") as file:
    file = file.read()
    file = file.split("\n")

for result in file:
    result = result.split(" ")
    result_track.append(result)
print(len(result_track))
count = 0
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        count += 1
        if count < 10:
            s = "_00"
        else:
            if count < 100:
                s = "_0"
            else:
                if count <= 295:
                    s = "_"
                else:
                    sys.exit("exit")
              
        for box in result_track:
            if box[0] == str(count):
                id = int(box[2])
                x1 = int(box[3])
                y1  = int(box[4])
                wbb= int(box[5])
                hbb = int(box[6])

                x_center = (x1+wbb/2)/width_img
                y_center = (y1+hbb/2)/height_img
                w_norm   = wbb/width_img
                h_norm   = hbb/height_img
                #print(str(id) + " "+ str(x_center)+" "+str(y_center)+" "+str(w_norm)+" "+str(h_norm))
                with open ("C:/Users/buikh/OneDrive/Documents/ET1_BKH/NCKH/Action recognition in video/CODE/dataset/sleeping/" + video_name+"_label_image/labels/"+video_name+s+str(count)+".txt", "a+") as f:
                    
                    f.write(str(id) + " "+ str(x_center)+" "+str(y_center)+" "+str(w_norm)+" "+str(h_norm)+"\n")
                # Draw box
        
        cv2.imwrite("C:/Users/buikh/OneDrive/Documents/ET1_BKH/NCKH/Action recognition in video/CODE/dataset/sleeping/" +video_name+"_label_image/images/" + video_name+s+str(count)+".jpg", frame)

    # Break the loopqq
    else:
        break
print("Done")
# When everything done, release
# the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()