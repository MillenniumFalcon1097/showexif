## Add Xiaomi-like EXIF watermark to your photo

![demo pic](outputs/DCZ_5326.jpg)

:laughing: Hope you guys enjoy it!

:triangular_flag_on_post: Click here for [English Readme file](https://github.com/MillenniumFalcon1097/showexif)  
:triangular_flag_on_post: Click here for [Simplified Chinese version](https://github.com/MillenniumFalcon1097/showexif/blob/master/readmeCN.md)


### Features
- [X] Accept RAW file and JPEG file as input.
- [X] Adaptable for any width and height images.
- [X] Can be run by CLI.

### Quick start
1. First you should install all the packages. But before we start, make sure your PC has a [python 3.x environment](https://www.python.org/downloads/windows/) installed. Then you cd to the workfolder, and open Windows Powershell or CMD as administrator, and run
   ```bash
   pip install -r requirements.txt
   ```
2. Put your photos into the `imgs` folder.
3. Run `python showexif.py`. That's all!

### Demo
1. To specify the folder where the generated images will be stored, use
   ```bash
   python showexif.py -svdir [SAVE_DIR]
   ```
2. To specify the folder where the photos will be read, use
   ```bash
   python showexif.py -imgdir [YOUR_PHOTO_DIR]
   ```
3. By default the JPEG files converted from RAW photos are saved in `tmp`. If you don't need them, use
   ```bash
   python showexif.py -nocache
   ```
   :warning:This will remove all files in `tmp` dir after generating new JPEG images.
4. You can specify those params mentioned above at the same time.



### TODO

- [X] Fix the bug when convert RAW to JPEG, the Exif data somehow gets lost.
- [ ] Supports more brands...

