## 在你的照片上添加类似小米的EXIF水印

:laughing: 希望你们喜欢！

### 特点
- [X] 接受 RAW 文件和 JPEG 文件作为输入。
- [X] 可以适应任何宽度和高度的图像。
- [X] 可以通过CLI运行。



### 快速启动
1. 首先你应该安装所有的软件包。但是在我们开始之前，请确保你的电脑已经安装了[python 3.x环境](https://www.python.org/downloads/windows/)。然后你cd到工作目录，以管理员身份打开Windows Powershell或CMD，并运行
   ```bash
   pip install -r requirements.txt
   ```
2. 把你的照片放到`imgs`文件夹中。
3. 运行`python showexif.py`。That's all！

### 样例
1. 要指定生成的图像的存放文件夹，请使用
   ```bash
   python showexif.py -svdir [SAVE_DIR]
   ```
2. 要指定读取照片的文件夹，请使用
   ```bash
   python showexif.py -imgdir [YOUR_PHOTO_DIR]
   ```
3. 默认情况下，RAW照片生成的JPEG文件被保存在`tmp`中。如果你不需要它们，可以使用
   ```bash
   python showexif.py -nocache
   ```
   这将在带水印的图片生成后删除`tmp`目录下的所有文件。
4. 你可以同时指定以上这些参数。

### TODO

- [X] 修复在RAW图片转JPEG图片时，Exif数据不知何故丢失的问题。

