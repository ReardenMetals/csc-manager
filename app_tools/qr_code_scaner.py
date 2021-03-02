import cv2
from pyzbar import pyzbar


class QrCodeScanner:

    def __init__(self):
        self.barcode_info = None
        self.barcode_increment = 0  # Timestamp at the moment of the last barcode info callback
        self.increment = 0  # Current timestamp

    def read_barcodes(self, frame, callback=None):
        if frame is None:
            return frame
        barcodes = pyzbar.decode(frame)
        if len(barcodes) == 0:
            return frame
        barcode = barcodes[0]

        x, y, w, h = barcode.rect
        # 1
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (0, 0, 0), 1)

        if callback is not None:
            self.increment += 1
            if (self.barcode_info != barcode_info) or (self.increment - self.barcode_increment > 5):
                self.barcode_info = barcode_info
                self.barcode_increment = self.increment
                callback(barcode_info)

        return frame
