
import PIL.Image
import PIL.ImageTk

from app_tools.qr_code_scaner import QrCodeScanner
from app_tools.my_video_capture import MyVideoCapture, DEFAULT_VIDEO_CAPTURE
import tkinter
import imutils


class CameraWidget:
    def __init__(self, camera_frame, width, height, on_qr_scanned_callback=None, paused=False):
        self.camera_frame = camera_frame
        self.qr_code_scanner = QrCodeScanner()
        self.width = width
        self.height = height
        self.on_qr_scanned_callback = on_qr_scanned_callback
        self.photo = None
        self.paused = paused

        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(self.camera_frame, width=self.width, height=self.height)
        self.canvas.pack()

        self.vid = DEFAULT_VIDEO_CAPTURE
        self.delay = 40

        self.camera_frame.after(1000, self.update_barcode_frame)

    def update_barcode_frame(self):
        if self.paused:
            return
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if frame is not None:
            frame = self.qr_code_scanner.read_barcodes(frame, callback=self.on_qr_scanned_callback)

        if frame is not None:
            frame = imutils.resize(frame, width=self.width, height=self.height)

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
            self.camera_frame.after(self.delay, self.update_barcode_frame)
        else:
            self.camera_frame.after(self.delay * 100, self.update_barcode_frame)

    def pause(self):
        DEFAULT_VIDEO_CAPTURE.release_camera()
        self.paused = True

    def resume(self):
        if self.paused:
            DEFAULT_VIDEO_CAPTURE.init()
            self.paused = False
            if self.camera_frame is not None:
                self.camera_frame.after(100, self.update_barcode_frame)
