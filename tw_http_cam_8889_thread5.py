import android  
import os  
import time  
import BaseHTTPServer  
from SocketServer import ThreadingMixIn  
  
HOST_NAME = ''  
PORT_NAME = 8888  
  
PAGE_SOURCE = ''''' 
<html> 
<head> 
<title>MJPEG</title> 
</head> 
<body> 
<h1>Camera</h1> 
<img height=300 width=400 src=/stream /> 
</body> 
</html> 
'''  
  
class ThreadServer(ThreadingMixIn, BaseHTTPServer.HTTPServer):  
    pass  
  
class StreamerHandler(BaseHTTPServer.BaseHTTPRequestHandler):  
    def do_GET(self):  
        if (self.path == '/' or not self.path):  
            self.send_response(200)  
            self.send_header('Content-Type', 'text/html')  
            self.end_headers()  
            self.wfile.write(PAGE_SOURCE)  
  
        elif (self.path == '/stream'):  
            self.send_response(200)  
            self.send_header('Connection', 'close')  
            self.send_header('Expires', '0')  
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, pre-check=0, post-check=0, max-age=0')  
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=BOUNDARYSTRING')  
            self.end_headers()  
  
            while True:  
                image = get_image()  
                self.send_header('Content-Type', 'image/jpeg')  
                self.send_header('Content-Length', str(len(image)))  
                self.end_headers()  
                self.wfile.write(image)  
                self.wfile.write("\r\n--BOUNDARYSTRING\r\n")  
                time.sleep(0.5)  
  
def get_image():  
    android.Android().cameraCapturePicture('/sdcard/sl4a/latest.jpg', True)  
    f = open('/sdcard/sl4a/latest.jpg')  
    image = f.read()  
    f.close()  
    os.remove('/sdcard/sl4a/latest.jpg')  
    return image  
  
if __name__ == '__main__':  
    server = ThreadServer((HOST_NAME, PORT_NAME), StreamerHandler)  
    server.serve_forever()