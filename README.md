# **ELA Animate**

## **Error Level Analysis**
Digitally editing photos, whether through AI filtering, Photoshop, Facetune, etc., can quickly diminish the original composition's contrast, lighting, sharpness, color & gradation. By comparison, unedited images maintain these characteristics, and thereby reflect the accuracy of a digital photo's composition. This cohesion is also observable when an unaltered image is compressed to only a fraction of it's original fidelity. **Error Level Analysis (ELA)** is a tool that can be used in forensic analysis of a digital image by identifying portions of a photo that do not accurately reflect the expected output of the composition when compressed. A more thorough explanation of ELA can be [found here](https://fotoforensics.com/tutorial-ela.php).


The artifacts left behind in an image that has signs of distortion (warping, facetuning, filtering, cloning, etc.) are difficult to separate from the image or any future iterations of it. In addition, the distortion that is often the most important or worth noting are the results of portions of the photo that were indirectly impacted by morphing, but not the focus or intended. These artifacts, whether big or small, won't easily disappear by resizing the image or by converting it to a different format. Any additional manipulations will only compound and reduce the overall image quality & fidelity further, and increase its distance from the image origin and/or authorship.

ELA Animate works by compressing and filtering the image at incremental stages of decreased resolution. These results are then compiled into an animated GIF. The options for GIF output also includes the speed at which the frames of each image are referenced, tuning the scale of the error level analysis, and the ability to blend the ELA output with the original reference image.

_Note: This tool was made with digital literacy in mind and is not meant for legal or forensic use. Any conclusions or assessements made using ELA Animate are not endorsed by its creator. Please use responsibly._

## Installation
To run the script, which includes image processing and manipulation functionalities, you'll need Python installed along with specific libraries that the script depends upon:

1. **Python**
Ensure that Python is installed on your system. The script was written for Python 3, so make sure you have a compatible version (Python 3.6 or newer is recommended). You can download Python from [python.org](https://www.python.org/downloads/). Additionally, you can verify any prior installation and/or upgrade python using: 

`python -m pip install --upgrade pip`

3. **Pillow (PIL Fork)**
The script uses the Pillow library, which is a fork of the Python Imaging Library (PIL). It provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities. To install Pillow, run:

`pip install Pillow`

3. **Optional Libraries** _(these libraries are not required, but are worth mentioning)_
If your script extends to handling metadata extraction or other specialized image processing tasks, you might also consider installing:

**pyexiv2**: For metadata handling, especially if you plan to manipulate or read EXIF data.
`pip install pyexiv2`

**NumPy**: Sometimes used in image processing for more complex numerical operations.
`pipinstall NumPy`

## Running ELA Animate
Navigate to the directory containing ELA Animate and run it as a .py file or by using the following console command:

`python ELA_ALLY_v1.py`

_**Note**: Ensure any paths used in the script (e.g., for loading images) are correct and accessible from your script's running directory or are appropriately absolute._

## File Selection & Directory Allocation
If all conditions have been met, the terminal will open and the following prompt will appear:

**'Enter the path to the image file (JPG, PNG, or WEBP):'**

Input the file address of the image to be used, or simply drag and drop directly into terminal window. Then press enter.
_((**Note**: Only JPG, PNG, or WEBP files are currently recognized and tested for this script.))_

**'Enter the base output directory:'**

Input the directory address of the folder you wish to use, or simply drag and drop the folder directly into terminal window. Then press enter.

## Parameter Selection
**'Enter the ELA analysis scale factor (usual range 1-20):'**

Input the amount of ELA presence in the GIF output. A higher number means more prominent ELA, a lower number will be more subtle. Whether a higher or lower scale is more useful depends upon attenuating this input with the other parameters you select.

**'Enter the image alpha value (0.0 to 1.0):**

Input the degree of opacity the original image will have in output GIF. A lower value will output less ELA in the blended GIF and a higher value will output more ELA by comparison. Entering 0.0 will show almost no ELA whatsoever, and 1.0 almost only the ELA output. _((**Note**: If the output GIF is exceedingly bright, consider using a lower alpha value, or attenuating the ELA scale factor differently to achieve a more desired result.))_

**Enter the GIF frame duration in milliseconds:**

The value input in this parameter is a general sliding scale for the speed between changes in each reference frame. A lower value will produce a shorter GIF, a higher value a longer one. Determine a ballpark number that works for you and adjust as needed. 

## Running ELA Animate
The script should begin running after you have entered in frame duration. To tell if it is, look in the directory you selected for output. There should be a new sub-folder in the destination directory that has a timestamped name with the parameters selected and all the files generated from running the script. A total of 99 compressed images of decreasing fidelity and 99 ELA filtered images representing each increment as it is analyzed should be present. You will know the script has finished when the GIF has been rendered and can be found in the same folder you initially selected for output.

A final prompt should appear when the GIF has finished rendering.

**Do you want to process another image? (yes/no/repeat):**
Typing '**yes**' _or_ '**y**' will restart the script, allowing you to select a new image to process, the desired destination directory, as well as new parameters for the rendering.
Typing '**no**' _or_ '**n**' will shut down the script and exit the terminal window.
Typing '**repeat**' _or_ '**r**' _will automatically re-select the last reference image and base output directory_, allowing you to quickly try new parameters with the same source to compare with the previous settings you chose.

## _((**Note**: All images generated from the script will reference the original image's pixel resolution. Keep file size in mind when rendering your GIF, as a 1000x1000  image will generate 198 more processed images of the same pixel width and height!))_ 
