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
      return details,False,_

    except Exception as e:
      return _,True,e 


if __name__ == "__main__":

    inputFile = "/content/file_example_MP4_480_1_5MG.mp4"
    outputFile = "Output.mp4"

    videoDetails,error,errorMsg = video_details(inputFile,outputFile)

    if not error:
      print("Success!!! output saved as",outputFile)
      print("\nDetails:")
      print("Total frames:",videoDetails[0])
      print("Duration of each frame {:.3f} ms".format(videoDetails[1]))
      print("original Resolution:",videoDetails[2])
      print("resized Resolution:",videoDetails[3]) 
    else:
      print("Error: \n",errorMsg)
