#import android
#from wsgiref.simple_server import make_server

#droid=android.Android()
#pic='/sdcard/DCIM/100MEDIA/snapshot.jpg'

#def camera(env,res):
#  if env['PATH_INFO']=='/':
#    droid.cameraCapturePicture(pic)
#    res('200 OK',[('Content-type','image/jpeg')])
#    return [file(pic).read()]

#httpd=make_server('',9002,camera)
#httpd.serve_forever()

import android

droid = android.Android()

droid.wakeLockAcquireBright()
droid.webcamStart(0,10,9090)
droid.webcamAdjustQuality(0,10)