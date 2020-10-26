import cv2
def video_details(inputFile,outputFile):
    try :
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

      resized =  cv2.resize(frame, dim, interpolation = cv2.INTER_AREA) 
      resizedResolution = resized.shape
      
      fourcc = cv2.VideoWriter_fourcc(*'MP4V')
      out = cv2.VideoWriter(outputFile,fourcc, cap.get(cv2.CAP_PROP_FPS),dim)
      counter = 0

      while (cap.isOpened()): 
          ret, frame = cap.read()

          if ret:
            frame = cv2.resize(frame,dim, fx = 0, fy = 0, 
                                interpolation = cv2.INTER_CUBIC) 
            out.write(frame)
          else:
            break


          # define q as the exit button 
          if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
      cap.release() 
      out.release()
      # Closes all the windows currently opened. 
      cv2.destroyAllWindows() 
                  

      details = [totalFrames,durationOfEachFrame,originalResolution,resizedResolution]
      error = [False]
      return details,error

    except Exception as e:
        error = [True,e]
        return None ,error
    
    
def image_details(inputFile_img,outputFile_img,image):
    try:
        if image:
          img = cv2.imread(inputFile_img) 
          resized_image = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)
          cv2.imwrite(outputFile_img, resized_image)  
          cv2.waitKey(0) 
          cv2.destroyAllWindows() 
          error = [False]   
        return outputFile_img, error
     
    except Exception as e:
        error = [True,e]
        return None, error
    
def resize_video(inputFile,outputFile):

    videoDetails,error= video_details(inputFile,outputFile)
    #print(videoDetails,error)

    if not error[0]:
      print("Success!!! output saved as",outputFile)
      print("\nDetails:")
      print("Total frames:",videoDetails[0])
      print("Duration of each frame {:.3f} ms".format(videoDetails[1]))
      print("original Resolution:",videoDetails[2])
      print("resized Resolution:",videoDetails[3]) 
    else:
        print("Error while saving video :",error[1])

        
def resize_img(inputFile_img,outputFile_img,image):
    
    resized_output_image,error = image_details(inputFile_img,outputFile_img,image)
    
    if not error[0]:
        print("\nImage details:")
        print("Success!!! Image output saved as",outputFile_img)
    else:
      print("\nImage details:")
      print("Error while saving image : ",error[1])
        
        
if __name__ == "__main__":
    

    inputFile = "D:\Git\Baby crying alert application\VID_20190611_100612.mp4"
    outputFile = "Output.mp4"
    image = True
    inputFile_img = "D:\Git\Baby crying alert application\Cute-baby.jpg"
    outputFile_img = "Output.jpg"
    
    resize_video(inputFile,outputFile)
    resize_img(inputFile_img,outputFile_img,image)
        





