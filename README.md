# **ELA Mate**

## **Error Level Analysis**
Digitally editing photos can quickly diminish the original image's contrast, lighting, sharpness, color & gradation. By comparison, unedited versions of the same photo maintain these touchstone characteristics of fidelity, and thereby reflect the accuracy of a digital photo's composition. This cohesion of content at lower resolution, or the lack thereof, can also be observable when an image is compressed to only a fraction of it's original fidelity.

**Error Level Analysis (ELA)** is a tool that identifies 'noise' that doesn't reflect a normal compression of the image in question, wherein portions of a photo that do not accurately reflect the expected output of the composition can quickly become noticeable and apparent. These artifacts are often left behind in an image that has signs of distortion (warping, facetuning, filtering, cloning, etc.), and therefore only become more difficult to separate from the image or any future iterations of it over time. In addition, many beauty filters, editing tools, and similar manipulations warp across large bands that leave ripples in the image that don't match the signifiers of the original, and therefore become tell-tale signs of manipulation when coupled with any evidence of forced perspective, dysmorphic proportion, or the sight of an uncanny face.

These artifacts, whether big or small, won't easily disappear when one resizes the image, or when converting it into another different format. Any additional manipulations will only compound the artifacts that were already left behind, and reduce the overall image quality & fidelity even further with each passing. This loss in fidelity is often indicative of a greater distance between the image in question and its point of origin, digitally speaking. 

A more thorough explanation of ELA can be [found here](https://fotoforensics.com/tutorial-ela.php).

## **v2 UPDATES** (3.6.25)
I've added some features that streamline processing different images, paramaters that are within a more useful range for detection, and more references, including one  that is widely known and acknowledged to be manipulated by both the public, via publications like The New York Times, and the original author. These examples are to show the scope and range that the settings ELA_Mate_v2 can provide upon output, as well aswhat a examples of known distortion look like within the capabilities of this version's script. 

*Future considerations: 
- option to convert image to JPG from PNG, WEBP, etc. before analysis.
- integrating _Noise Analysis_ as a secondary detection method.*

### Example: Self-Analysis

_Edited screencap:_
![two podcast hosts](https://github.com/maxedonia/ela_mate/blob/update-ela-script/example2/Plot_Ex1.png)

_Hotspot overlay 40% opacity:_
![without ears](https://github.com/maxedonia/ela_mate/blob/update-ela-script/example2/Plot_Ex2.png)

_ELA hotspot analysis only:_
![image overlay](https://github.com/maxedonia/ela_mate/blob/update-ela-script/example2/Plot_Ex4.png)

_Circled hotspots with ELA analysis at 40% opacity:_
![circled hotspots](https://github.com/maxedonia/ela_mate/blob/update-ela-script/example2/Plot_Ex3.png)

_Animated GIF composite of JPEG degrading under Error Level Analysis_
![PLOT ELA](https://github.com/maxedonia/ela_mate/blob/main/example2/ELA_EXAMPLE2.gif)

*This example shows where edits have been made explicitly with the intention of being known. The hotspots indicating manipulation are circled and can be observed under ELA. I removed the ears of both subjects, as well as attempted to cover up tattoos on the right biceps of each individual using Photoshop. Additional evidence shows that I cropped the image at some point due to the lighter banding along the top border that appears in the images during analysis).*

### Example: The Royal Family
_Source Image:_

![royal](https://github.com/user-attachments/assets/111aaff5-b0a8-4570-9753-0717c889a747)

_ELA Hotspots Only:_

![ela_90](https://github.com/user-attachments/assets/29e6bdf8-0755-4ff6-b124-128b00ee23d8)

_ELA at Half-Fidelity:_

![ela_98](https://github.com/user-attachments/assets/ecee2a0e-8fe8-48cd-9dd9-16713282a4a0)

_Areas observed by naked eye:_

![Source NYT](https://github.com/user-attachments/assets/c3284033-5d77-4225-b0dc-a72a76ff52de)
Source: [nytimes.com](https://www.nytimes.com/2024/03/11/world/europe/kate-middleton-photo-princess-wales.html)

_Animated GIF composite of JPEG degrading under Error Level Analysis_
![ELA ANIMATED](https://github.com/maxedonia/ela_mate/blob/main/example/ELA_Animation.gif)

*This image is only used as a reference due to its unique nature of origin, and done so only after confirmation from parties involved of their inauthentic qualities. This tool and these images are not meant to bully or force one's perspective or opinion in any way, shape, or form.*



## **ELA Mate & Forensic Analysis**

_**ELA Mate**_ works by compressing and filtering an image at incremental stages of decreased resolution. These results are then compiled into an animated GIF. The options for GIF output also includes the speed at which the frames of each image are referenced, the scale of error analysis shown, and the ability to blend the ELA output with the original reference image for comparison.

That said, ELA is just one of [_many_ tools](https://29a.ch/photo-forensics/#forensic-magnifier) that can be used in forensics. All of them require insight, experience, digital literacy, and an attention to detail in order to be used properly. If someone has a reason to doubt an image's authenticity, then the onus is on them to make a strong enough statement for that to be the case. In an age where finding authenticity in our social feeds is getting harder to find, the case for creating tools like this one has only gotten stronger. Taking a photo without AI filtering on iOS in 2024 is already a [very difficult process](https://support.apple.com/guide/iphone/take-apple-proraw-photos-iphae1e882a3/ios). AI trained by our pervasive and willful use only grows exponentially unrealistic. And if reality is on pace to favor the fake, then this tool is just one small attempt to confront that notion in some way.

***Note: This script was written with digital literacy in mind. It is not meant for legal or forensic use. Any conclusions or assessements made from using ELA Mate are not reflective nor endorsed by those of the author. Please use tools like this one responsibly.***



## Installation
To run the script, which includes image processing and manipulation functionalities, you'll need Python installed along with specific libraries that the script depends upon:

1. **Python**
  Ensure that Python is installed on your system. The script was written for Python 3, so make sure you have a compatible version (Python 3.6 or newer is recommended). You can download Python from [python.org](https://www.python.org/downloads/). Additionally, you can verify any prior installation and/or upgrade python using: 

   `python -m pip install --upgrade pip`

2. **Pillow (PIL Fork)**
  The script uses the Pillow library, which is a fork of the Python Imaging Library (PIL). It provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities. To install Pillow, run:

   `pip install Pillow`

3. **Optional Libraries** _(these libraries are not required, but are worth mentioning)_
  If your script extends to handling metadata extraction or other specialized image processing tasks, you might also consider installing:

    - **pyexiv2**: For metadata handling, especially if you plan to manipulate or read EXIF data.
  
      `pip install pyexiv2`

    - **NumPy**: Sometimes used in image processing for more complex numerical operations.
  
      `pip install NumPy`



## Start **ELA Mate**
Navigate to the directory containing _**ELA Mate**_ and run it as a .py file or by using the following console command:

  `python ELA Mate_v1.py`


  <sup> _**Note**: Ensure any paths to files and output directories are correct and accessible to the script, including writing permissions when applicable._</sup> 

## File Selection & Directory Allocation
If all conditions have been met, the terminal will open and the following prompt will appear:


**'Enter the path to the image file (JPG, PNG, or WEBP):'**

  Input the file address of the image to be used, or simply drag and drop directly into terminal window. Then press enter.

  <sup> _**Note**: At this time, **only JPG, PNG, or WEBP** files are applicable. The script will convert any other format it can support into a JPG before initiating analysis._</sup> 


**'Enter the base output directory:'**

  Input the directory address of the folder you wish to use, or simply drag and drop the folder directly into terminal window. Then press enter.


## Parameter Selection
![settingsscrop](https://github.com/maxedonia/animate_ela/assets/47838472/55563472-d8df-45bf-93e3-911733498a25)


**'Enter the ELA analysis scale factor (usual range 1-20):'**

   Input the amount of ELA presence in the GIF output. A higher number means more prominent ELA, a lower number will be more subtle. Whether a higher or lower scale is more useful depends upon attenuating this input with the other parameters you select.

**'Enter the image alpha value (0.0 to 1.0):**

  Input the degree of opacity the original image will have in output GIF. A lower value will output less ELA in the blended GIF and a higher value will output more ELA by comparison. Entering 0.0 will show almost no ELA in the GIF output whatsoever. Entering 1.0 will result in almost only the ELA in the GIF output. 
  
  <sup> _**Note**: If the output GIF is exceedingly bright, consider using a lower alpha value, or attenuating the ELA scale factor differently to achieve a more desired result._</sup>
     

**Enter the GIF frame duration in milliseconds:**

  The value input in this parameter is a general sliding scale for the speed between changes in each reference frame. A lower value will produce a shorter GIF, a higher value a longer one. For example, entering in a value of '100' will output a GIF approximately 10 seconds long. Adjust as needed.



## Running **ELA Mate**
Your console window should look similar to the one below before you execute.
![settings](https://github.com/maxedonia/animate_ela/assets/47838472/02261365-1f04-459f-8278-480b0f218869)

Upon pressing enter, the script will do the following actions in sequence: 
  - Create a new folder in the selected output directory that is timestamped and labeled with the parameters you selected. 
  - Generate two sets of images
    - A total of 99 images generated with the length and width of the reference image, and with each image in the set having a higher incremental degree of compression relative to the original reference image.
    - A total of 99 error level analysis images generated from the set of compressed images with the user defined _ELA scale factor parameter_ upon output.
  - A GIF of the ELA generated images in sequence from highest to lowest quality and in a interval of time based upon the user defined _frame duration parameter_.
  - The GIF output compiled with the reference image that has a visibility that is determined by the _user defined alpha value parameter_ upon final output.

<sup>_**Note**: Though the file size of images generated by the script will vary, keep in mind that the original image's resolution/aspect ratio will remain the same for each instance. Therefore, the contents of a folder that is generated from a 6000x4000 image will be significantly larger and take longer to generate than an reference image that is 600x400._</sup>



## Basic Operation

The following image was taken on a Canon EOS Rebel T7i with an ultra-wide lens:
![ELA example1](https://github.com/maxedonia/animate_ela/assets/47838472/d32815d6-8af6-4593-9ea4-457518cf5181)

  After starting the script a new folder in the output directory appears and will begin to populate itself with the two image sets...
  
  ![output example1 cropped](https://github.com/maxedonia/animate_ela/assets/47838472/3b791001-2029-4447-a91a-7bfc1c9147fe)


  ![output example1 small size](https://github.com/maxedonia/animate_ela/assets/47838472/adc31e6a-8135-4e8e-b0cc-e46be682a62c)

  ... followed by the compiled GIF with the user defined parameters applied to it in the destination folder.
![ELA_Original_Blended_Animation_resized_1](https://github.com/maxedonia/animate_ela/assets/47838472/e2c1213d-9753-4351-a552-cc505c4e90de)


  A final prompt should appear when the script has completed.

  ![settings2](https://github.com/maxedonia/animate_ela/assets/47838472/d2d1d5cf-e0e8-4e07-8c03-ef5df44cd0f3)

  **Do you want to process another image? (yes/no/repeat):**
  - Typing '**yes**' _or_ '**y**' allows for a different image to be used in a new analysis.
  - Typing '**no**' _or_ '**n**' will shut down the script and exit the terminal window.
  - Typing '**repeat**' _or_ '**r**' will _automatically re-select the last reference image and base output directory_, allowing for quick tweaking of settings of the output using the same image as the previous analysis.

    <sup>_**Note**: The console window should close automatically if **no** is selected._

## Examples of Differentiated Output
**Reference Photo**

_Here are some side-by-side [comparison GIFs](https://giphy.com/channel/maxedonia/ela) of the same source image as before. Each one is labelled with the parameters used during generation:_

![gid example A](https://github.com/maxedonia/animate_ela/assets/47838472/0ea0edb1-0093-419d-a533-77e81dc6b9b1)
![gid example B](https://github.com/maxedonia/animate_ela/assets/47838472/a2bcf51a-5023-43b1-8086-086910033a9a)
![gid example C](https://github.com/maxedonia/animate_ela/assets/47838472/589ac347-b800-4635-b024-ae286cfdce24)
![gid example D](https://github.com/maxedonia/animate_ela/assets/47838472/fb8abc3c-c8ea-4c7a-835c-5f1d38a3c3d0)

**Touch Up Artifacts in Windows Photos App**

_Here we have is the same photograph, but one picture has had the Edison Bulbs at the top of the image edited out using AI assisted touch-ups possible within the Photos app in Windows 10._

![gid example2 A](https://github.com/maxedonia/animate_ela/assets/47838472/65e476b2-3c83-4ee3-a116-b9e7856ad6fe)
![gid example2 B](https://github.com/maxedonia/animate_ela/assets/47838472/43db3528-8759-41b0-b435-2881d8591935)

  <sup>_**Note**: parameters have been added to example GIFs for clarity and are **not currently featured** in **ELA Mate**'s output at this time._</sup>



