import time
import android
from wsgiref.simple_server import make_server

droid=android.Android()
pic='/sdcard/DCIM/100MEDIA/snapshot.jpg'

def camera(env,res):
  if env['PATH_INFO']=='/':
    droid.cameraCapturePicture(pic)
    res('200 OK',[('Content-type','image/jpeg')])
    return [file(pic).read()]

while 1:
  httpd=make_server('',8080,camera)
  httpd.serve_forever()    # handle_request, serve_forever
  time.sleep(1)  # 1 second