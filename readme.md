## Add Xiaomi-like EXIF watermark to your photo

Hope you guys enjoy it!

### Quick start
1. First you should install all the packages. You cd to the workfolder, and open Windows Powershell or CMD as administrator, and run
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
3. By default the RAW photos are saved in `tmp`. If you don't need them, use
   ```bash
   python showexif.py -nocache
   ```
   This will remove all files in `tmp` dir.
4. You can specify those params at the same time.

### TODO
- [X] Accept RAW file and JPEG file as input.
- [X] Adaptable for any width and height images.
- [X] Can be run by CLI.
- [X] Fix the bug when convert RAW to JPEG, the Exif data somehow get lost.

