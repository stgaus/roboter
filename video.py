class Video():
    
    webCam = True
    path = ''
    buffer = 64
    
    def __init__(self, webCam, path, buffer):
        self.webCam = webCam
        self.path = path
        self.buffer = buffer
