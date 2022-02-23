import requests
import shutil
from datetime import datetime
import time
import os

# sky camera url
sky_cam_url = "http://www.astroclaudine.fr/oukaimeden/Data/ImageLastFTP_AllSKY.jpg"
# Mt. Oukaimden camera url
mt_oukaimden_cam_url = "http://www2.orca.ulg.ac.be/TRAPPIST/Camera/images/TNcamera.jpg"
# Initialisation of image count
inc = 0

while inc < 400:
    # current date and time
    now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    # filenames
    sky_cam_filename = 'SkyCam_'+str(inc)+'.jpg'
    mt_oukaimden_filename = 'MtOukaimden_'+str(inc)+'.jpg'

    # create new directories
    if inc % 100 == 0:
        sky_cam_current_dir = 'SkyCam_'+now
        mt_oukaimden_current_dir = 'MtOukaimden_'+now
        os.mkdir('SkyCam/'+sky_cam_current_dir)
        os.mkdir('MtOukaimden/'+mt_oukaimden_current_dir)

    sky_cam_request = requests.get(sky_cam_url, stream=True)
    mt_oukaimden_request = requests.get(mt_oukaimden_cam_url, stream=True)

    # Check if sky_cam_request was successful
    if sky_cam_request.status_code == 200:
        sky_cam_request.raw.decode_content = True
        # Save sky_cam image
        with open('SkyCam/'+sky_cam_current_dir+'/'+sky_cam_filename, 'wb') as f:
            shutil.copyfileobj(sky_cam_request.raw, f)
        print(sky_cam_filename)
    else:
        print('SkyCam Image couldn\'t be downloaded')

    # Check if mt_oukaimden_request was successful
    if mt_oukaimden_request.status_code == 200:
        mt_oukaimden_request.raw.decode_content = True
        # Save mt_oukaimden image
        with open('MtOukaimden/'+mt_oukaimden_current_dir+'/'+mt_oukaimden_filename, 'wb') as f:
            shutil.copyfileobj(mt_oukaimden_request.raw, f)
        print(mt_oukaimden_filename)
    else:
        print('Mt. Oukaimden Image couldn\'t be downloaded')

    # Wait time before next request
    time.sleep(360)
    inc = inc + 1

print('Finished the Operation!')

# os.system("ffmpeg -framerate 25 -i SkyCam_%03d.jpg -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4")
