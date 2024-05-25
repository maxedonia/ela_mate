# **ELA Mate**

## **Error Level Analysis**
Digitally editing photos, whether through AI filtering, Photoshop, Facetune, etc., can quickly diminish the original composition's contrast, lighting, sharpness, color & gradation. By comparison, unedited images maintain these characteristics, and thereby reflect the accuracy of a digital photo's composition. This cohesion is also observable when an unaltered image is compressed to only a fraction of it's original fidelity. **Error Level Analysis (ELA)** is a tool that can be used in forensic analysis of a digital image by identifying portions of a photo that do not accurately reflect the expected output of the composition when compressed. A more thorough explanation of ELA can be [found here](https://fotoforensics.com/tutorial-ela.php).


The artifacts left behind in an image that has signs of distortion (warping, facetuning, filtering, cloning, etc.) are difficult to separate from the image or any future iterations of it. In addition, the distortion that is often the most important or worth noting are the results of portions of the photo that were indirectly impacted by morphing, but not the focus or intended. These artifacts, whether big or small, won't easily disappear by resizing the image or by converting it to a different format. Any additional manipulations will only compound and reduce the overall image quality & fidelity further, and increase its distance from the image origin and/or authorship.

ELA Mate works by compressing and filtering the image at incremental stages of decreased resolution. These results are then compiled into an animated GIF. The options for GIF output also includes the speed at which the frames of each image are referenced, tuning the scale of the error level analysis, and the ability to blend the ELA output with the original reference image.

***Note: This tool was made with digital literacy in mind and is not meant for legal or forensic use. Any conclusions or assessements made when using ELA Mate are not reflective of the opinions nor endorsed by its creator. Please use these tools responsibly.***

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

## Start ELA Mate
Navigate to the directory containing ELA Mate and run it as a .py file or by using the following console command:

`python ELA_ALLY_v1.py`

_**Note**: Ensure any paths used in the script (e.g., for loading images) are correct and accessible from your script's running directory or are appropriately absolute._

## File Selection & Directory Allocation
If all conditions have been met, the terminal will open and the following prompt will appear:

**'Enter the path to the image file (JPG, PNG, or WEBP):'**

Input the file address of the image to be used, or simply drag and drop directly into terminal window. Then press enter.
_**Note**: At this time, **only JPG, PNG, or WEBP** files have been tested with this script._

**'Enter the base output directory:'**

Input the directory address of the folder you wish to use, or simply drag and drop the folder directly into terminal window. Then press enter.

## Parameter Selection
**'Enter the ELA analysis scale factor (usual range 1-20):'**

Input the amount of ELA presence in the GIF output. A higher number means more prominent ELA, a lower number will be more subtle. Whether a higher or lower scale is more useful depends upon attenuating this input with the other parameters you select.

**'Enter the image alpha value (0.0 to 1.0):**

Input the degree of opacity the original image will have in output GIF. A lower value will output less ELA in the blended GIF and a higher value will output more ELA by comparison. Entering 0.0 will show almost no ELA in the GIF output whatsoever. Entering 1.0 will result in almost only the ELA in the GIF output. _**Note**: If the output GIF is exceedingly bright, consider using a lower alpha value, or attenuating the ELA scale factor differently to achieve a more desired result._

**Enter the GIF frame duration in milliseconds:**

The value input in this parameter is a general sliding scale for the speed between changes in each reference frame. A lower value will produce a shorter GIF, a higher value a longer one. Determine a ballpark number that works for you and adjust as needed. 

## Running ELA Mate
The script should look similar in your console to the one seen below.
![settings](https://github.com/maxedonia/animate_ela/assets/47838472/02261365-1f04-459f-8278-480b0f218869)

Upon enter, the script will do the following actions in order: 
- Create a new folder in the selected output directory that is timestamped and labeled with the parameters you selected. 
- Generate two sets of images
  - A total of 99 images generated with the length and width of the reference image, and with each image in the set having a higher incremental degree of compression relative to the original reference image.
  - A total of 99 error level analysis images generated from the set of compressed images with the user defined _ELA scale factor parameter_ upon output.
- A GIF of the ELA generated images in sequence from highest to lowest quality and in a interval of time based upon the user defined _frame duration parameter_.
- The GIF output compiled with the reference image that has a visibility that is determined by the _user defined alpha value parameter_ upon final output.

## _**Note**: Though the file size of images generated by the script will vary, keep in mind that the original image's resolution/aspect ratio will remain the same for each instance. Therefore, the contents of a folder that is generated from a 6000x4000 image will be significantly larger and take longer to generate than an image that is 600x400._ 

## Examples & Case Usage

The following image was taken on a Canon EOS Rebel T7i with an ultra-wide lens:
![ELA example1](https://github.com/maxedonia/animate_ela/assets/47838472/d32815d6-8af6-4593-9ea4-457518cf5181)

After starting the script a new folder appears in the output directory appears and will populate with the two image sets...

![output example1 cropped](https://github.com/maxedonia/animate_ela/assets/47838472/e38c596f-97e1-4ff1-8e9b-90bf1314d2b6)

![output example1 small size](https://github.com/maxedonia/animate_ela/assets/47838472/adc31e6a-8135-4e8e-b0cc-e46be682a62c)

... followed by the compiled GIF containing the user defined parameters in destination folder.

![GIF example 1](https://github.com/maxedonia/animate_ela/assets/47838472/7d488347-9822-43b2-a820-191bcbfae618)

_**Note**: parameters have been added to example GIFs sepately and are not currently included in ELA Mate's output_

A final prompt should appear when the script has completed.

![settings2](https://github.com/maxedonia/animate_ela/assets/47838472/d2d1d5cf-e0e8-4e07-8c03-ef5df44cd0f3)

**Do you want to process another image? (yes/no/repeat):**
- Typing '**yes**' _or_ '**y**' allows for a different image to be used in a new analysis.
- Typing '**no**' _or_ '**n**' will shut down the script and exit the terminal window.
- Typing '**repeat**' _or_ '**r**' will _automatically re-select the last reference image and base output directory_, allowing you to quickly adjust parameters while maintaining the same reference image.

_**Note**: The console window should close automatically if **no** is selected, or in the event that running an analysis causes the script to fail. An empty folder that is timestamped is typically more indicative of an unrecognized parameter. If the script fails and no new folders are present, double-check that your file and output path directories are correct and that you have the proper permissions to execute the script the destination chosen._
![ELA_Original_Blended_Animation_resized_1](https://github.com/maxedonia/animate_ela/assets/47838472/50d8142a-9997-4763-a6f2-7e5f7068da2c)






