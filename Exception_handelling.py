import cv2
def video_details(inputFile,outputFile):
    cap = cv2.VideoCapture(inputFile)
    ret, frame = cap.read()
    totalFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frames_per_second = cap.get(cv2.CAP_PROP_FPS)  
    duration_of_video = float(totalFrames) / float(frames_per_second)
    durationOfEachFrame = duration_of_video/totalFrames
    originalResolution = frame.shape
    width = int(frame.shape[1] * 0.5)
    height = int(frame.shape[0] * 0.5)
    dim = (width,height)
    print(dim)
    resized =  cv2.resize(frame, dim, interpolation = cv2.INTER_AREA) 
    resizedResolution = resized.shape
    
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    out = cv2.VideoWriter(outputFile,fourcc, cap.get(cv2.CAP_PROP_FPS),dim)
    counter = 0
    #try:
    while (cap.isOpened()): 
        ret, frame = cap.read()
        counter += 1
        #print("Counter : ",counter)
        #print(ret)
        if ret:
            #Resizing the frame
            frame = cv2.resize(frame,dim, fx = 0, fy = 0, 
                                interpolation = cv2.INTER_CUBIC) 
            out.write(frame)
            # Display the resulting frame 
            #cv2.imshow('Frame', frame)  
        else:
            #print("Failure")
            break   

        # define q as the exit button 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    cap.release() 
    out.release()
    # Closes all the windows currently opened. 
    cv2.destroyAllWindows() 
                
    #except Exception as e:
     #   print (str(e)) 
    
    return totalFrames,durationOfEachFrame,originalResolution,resizedResolution

def main():
    totalFrames,durationOfEachFrame,originalResolution,resizedResolution = video_details("VID_20190611_100612.mp4",'output_1.mp4')
    path = "D:\Git\Baby crying alert application"
    print("Success. output saved:",path)
    print(totalFrames)
    print(durationOfEachFrame)
    print(originalResolution)
    print(resizedResolution)  



if __name__ == "__main__":
    main()
