# Oukaimeden Observatory - Web Scraping

Web-Scraping Script to collect images from Oukaimeden Observatory website's live camera and create a TimeLapse of each day.


## Usage
### Creation of a Timelapse from each folder (every day)

``` Python
import os
os.system("ffmpeg -framerate 25 -i SkyCam_%03d.jpg -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4")
```
