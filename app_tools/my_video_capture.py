import cv2


class MyVideoCapture:
    def __init__(self, video_source=0):
        self.video_source = video_source
        self.vid = None
        self.width = None
        self.height = None
        self.init()

    def init(self):
        # Open the video source
        self.vid = cv2.VideoCapture(self.video_source)
        if not self.vid.isOpened():
            print("Unable to open video source")
            raise ValueError("Unable to open video source", self.video_source)

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                print("Ret not found")
                return (ret, None)
        else:
            print("get_frame Not opened")
            return (None)

    # Release the video source when the object is destroyed
    def __del__(self):
        print("Camera capture released")
        if self.vid.isOpened():
            self.vid.release()

    def release_camera(self):
        print("Camera capture released")
        if self.vid.isOpened():
            self.vid.release()


DEFAULT_VIDEO_CAPTURE = MyVideoCapture(0)
