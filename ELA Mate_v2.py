#!/usr/bin/env python3
"""
ELA_Mate_v3.py

A tool for Error Level Analysis (ELA) on images to help visualize digital compression artifacts,
which can hint at image manipulation. This version generates multiple ELA images at varying JPEG quality
levels, creates an animated GIF of the ELA progression, and produces a hotspot image based on the 
"darkest" ELA iteration (assumed to share the reference image's quantization table). The hotspot image
is produced by blending the original image with the darkest ELA image.

Usage:
    Run the script and follow the interactive prompts to provide the image path, output directory, and
    processing parameters.

Requirements:
    Pillow (Python Imaging Library)
    numpy
"""

import os
import io
from datetime import datetime
from PIL import Image, ImageChops, ImageEnhance
import numpy as np
import shutil  # Added to enable copying the reference image

def generate_ela(original, compressed, enhancement_factor):
    """
    Generate an Error Level Analysis (ELA) image from the original and its compressed version.

    Args:
        original (PIL.Image.Image): The original image.
        compressed (PIL.Image.Image): The compressed version of the original image.
        enhancement_factor (float): Brightness multiplier to amplify differences.

    Returns:
        PIL.Image.Image: The enhanced ELA image.
    """
    ela = ImageChops.difference(original, compressed)
    extrema = ela.getextrema()
    max_diff = max(val[1] for val in extrema)
    if max_diff == 0:
        max_diff = 1
    scale_factor = (255 / max_diff) * enhancement_factor
    return ImageEnhance.Brightness(ela).enhance(scale_factor)

def blend_images(original, ela, overlay_strength):
    """
    Blend the original image with its ELA version.

    Args:
        original (PIL.Image.Image): The original image.
        ela (PIL.Image.Image): The ELA image.
        overlay_strength (float): A value between 0.0 (only the original) and 1.0 (only the ELA image).

    Returns:
        PIL.Image.Image: The blended image.
    """
    return Image.blend(original.convert('RGBA'), ela.convert('RGBA'), overlay_strength)

def create_animated_gif(original, ela_images, output_path, overlay_strength, frame_duration):
    """
    Create an animated GIF by blending the original image with each ELA image.

    Args:
        original (PIL.Image.Image): The original image.
        ela_images (list): A list of ELA images.
        output_path (str): The file path to save the animated GIF.
        overlay_strength (float): The blend strength for each frame.
        frame_duration (int): Duration (in milliseconds) for each frame.
    """
    frames = [blend_images(original, ela, overlay_strength) for ela in ela_images]
    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=frame_duration, loop=0)

def generate_hotspot_image(original, ela_images, hotspot_overlay_strength=0.5):
    """
    Generate a hotspot image by selecting the darkest ELA image (i.e. the one with the lowest overall brightness)
    and blending it with the original image. The assumption is that the darkest ELA image corresponds to the 
    quantization table of the reference image, highlighting edited regions.

    Args:
        original (PIL.Image.Image): The original image.
        ela_images (list): List of ELA images generated at various JPEG quality levels.
        hotspot_overlay_strength (float): Blending strength (0.0 to 1.0) for overlaying the hotspot image.

    Returns:
        PIL.Image.Image: The final hotspot image.
    """
    # Initialize with a very high darkness sum
    darkest_ela = None
    lowest_sum = float('inf')
    
    # Evaluate each ELA image in grayscale
    for img in ela_images:
        gray = img.convert("L")
        total = np.array(gray, dtype=np.float32).sum()
        if total < lowest_sum:
            lowest_sum = total
            darkest_ela = img

    # Blend the original with the darkest ELA image using a fixed overlay strength
    hotspot = Image.blend(original.convert("RGBA"), darkest_ela.convert("RGBA"), hotspot_overlay_strength)
    return hotspot.convert("RGB")

def process_image(original_path, output_base, enhancement_factor, overlay_strength, frame_duration, start_quality=99, end_quality=1):
    """
    Process an image by generating multiple ELA images, creating an animated GIF, and producing
    a hotspot image from the darkest ELA iteration.

    Args:
        original_path (str): File path to the original image.
        output_base (str): Directory where outputs will be saved.
        enhancement_factor (float): Factor to enhance ELA differences.
        overlay_strength (float): Blend strength for images in the animated GIF.
        frame_duration (int): Frame duration for the animated GIF (milliseconds).
        start_quality (int): Starting JPEG quality level for processing.
        end_quality (int): Ending JPEG quality level for processing.
    """
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_dir = os.path.join(output_base, f"ELA_{timestamp}_enhance{enhancement_factor}_overlay{overlay_strength}_duration{frame_duration}")
    os.makedirs(output_dir, exist_ok=True)
    
    ela_images = []
    
    with Image.open(original_path) as img:
        original = img.convert('RGB')
        for quality in range(start_quality, end_quality - 1, -1):
            # Compress the image in-memory at the specified JPEG quality.
            buffer = io.BytesIO()
            original.save(buffer, format='JPEG', quality=quality)
            buffer.seek(0)
            with Image.open(buffer) as compressed:
                compressed = compressed.convert('RGB')
                ela = generate_ela(original, compressed, enhancement_factor)
                ela_images.append(ela)
                ela.save(os.path.join(output_dir, f"ela_{quality}.jpg"), 'JPEG', quality=95)
    
    # Create animated GIF from ELA images.
    gif_path = os.path.join(output_dir, "ELA_Animation.gif")
    create_animated_gif(original, ela_images, gif_path, overlay_strength, frame_duration)
    print(f"Animated GIF created at {gif_path}")
    
    # Generate hotspot image using the darkest ELA image.
    if ela_images:
        hotspot = generate_hotspot_image(original, ela_images)
        hotspot_path = os.path.join(output_dir, "ELA_Hotspots.jpg")
        hotspot.save(hotspot_path, 'JPEG', quality=95)
        print(f"Hotspot image created at {hotspot_path}")
    
    # Copy the reference image file (without any processing) to the output directory.
    reference_image_destination = os.path.join(output_dir, os.path.basename(original_path))
    shutil.copy(original_path, reference_image_destination)
    print(f"Reference image copied to {reference_image_destination}")

def main():
    """
    Main interactive loop for processing an image.
    """
    original_path = input("Enter the full path to your image file: ").strip().strip('"')
    output_base = input("Enter the folder where you want to save the results: ").strip().strip('"')
    
    while True:
        print("\nEnter new settings for ELA processing:")
        try:
            enhancement_factor = float(input("Enter the brightness enhancement factor (e.g. 10): "))
            overlay_strength = float(input("Enter the overlay strength (0.0 for original only, 1.0 for full ELA overlay): "))
            frame_duration = int(input("Enter frame duration (in milliseconds) for the animated GIF: "))
        except ValueError:
            print("Invalid input. Please enter numerical values for the settings.")
            continue
        
        process_image(original_path, output_base, enhancement_factor, overlay_strength, frame_duration)
        
        print("\nWhat would you like to do next?")
        print("1. Process the same image with new parameters")
        print("2. Process a new image with new parameters")
        print("3. Quit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == '1':
            # Continue processing the same image.
            continue
        elif choice == '2':
            # Prompt for new image file and output folder.
            original_path = input("Enter the full path to your new image file: ").strip().strip('"')
            output_base = input("Enter the folder where you want to save the results: ").strip().strip('"')
        elif choice == '3':
            break
        else:
            print("Invalid choice. Exiting.")
            break

    input("Processing complete. Press Enter to exit.")

if __name__ == "__main__":
    main()
