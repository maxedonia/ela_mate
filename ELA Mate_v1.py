import os
from PIL import Image, ImageChops, ImageEnhance
from datetime import datetime

def ela_image(original_path, compressed_path, output_path, scale):
    original = Image.open(original_path).convert('RGB')
    compressed = Image.open(compressed_path).convert('RGB')
    
    ela = ImageChops.difference(original, compressed)
    extrema = ela.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    scale_factor = 255 / max_diff * scale  # Adjusted scaling for visibility
    
    ela = ImageEnhance.Brightness(ela).enhance(scale_factor)
    # Save as JPEG instead of PNG
    ela_output_path = output_path.replace('.png', '.jpg')  # Change the file extension in the path
    ela.save(ela_output_path, 'JPEG', quality=95)  # Specify JPEG format and adjust quality as needed
    
    ela = ImageEnhance.Brightness(ela).enhance(scale_factor)
    ela.save(output_path)

def blend_images(original_path, ela_image_path, alpha):
    original = Image.open(original_path).convert('RGBA')
    ela = Image.open(ela_image_path).convert('RGBA')
    
    # Use user-provided alpha for blending
    blended = Image.blend(original, ela, alpha=alpha)  
    return blended

def create_animated_gif(original_path, ela_image_paths, output_gif_path, alpha, duration):
    blended_images = [blend_images(original_path, ela_path, alpha) for ela_path in ela_image_paths]
    blended_images[0].save(output_gif_path, save_all=True, append_images=blended_images[1:], optimize=False, duration=duration, loop=0)

def compress_image_with_ela(original_path, output_dir_base, scale, alpha, duration, start_quality=99, end_quality=1):
    # Format the timestamp and parameters into the directory name
    params = f"scale_{scale}_alpha_{alpha}_duration_{duration}"
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_dir = os.path.join(output_dir_base, f"ELA_{timestamp}_{params}")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    original_image = Image.open(original_path)
    ela_image_paths = []
    
    for quality in range(start_quality, end_quality - 1, -1):
        compressed_filename = f"compressed_{quality}.jpg"
        compressed_path = os.path.join(output_dir, compressed_filename)
        original_image.save(compressed_path, 'JPEG', quality=quality)
        
        ela_filename = f"ela_{quality}.jpg"
        ela_path = os.path.join(output_dir, ela_filename)
        ela_image(original_path, compressed_path, ela_path, scale)
        ela_image_paths.append(ela_path)
    
    gif_output_path = os.path.join(output_dir, "ELA_Original_Blended_Animation.gif")
    create_animated_gif(original_path, ela_image_paths, gif_output_path, alpha, duration)
    print(f"Animated GIF created at {gif_output_path}")

def main():
    last_image_path = None
    last_output_dir = None

    while True:
        if not last_image_path:  # If it's the first run or user wants new input
            original_image_path = input("Enter the path to the image file (JPG, WEBP, or PNG): ").strip().strip('"')
            output_directory_base = input("Enter the base output directory: ").strip().strip('"')
        else:  # Use last used paths only
            original_image_path = last_image_path
            output_directory_base = last_output_dir

        scale = float(input("Enter the ELA analysis scale factor (usual range 1-20): "))
        alpha = float(input("Enter the image blend alpha value (0.0 to 1.0): "))
        duration = int(input("Enter the GIF frame duration in milliseconds: "))

        compress_image_with_ela(original_image_path, output_directory_base, scale, alpha, duration)

        # Save paths
        last_image_path = original_image_path
        last_output_dir = output_directory_base

        response = input("Do you want to process another image? (yes/no/repeat): ").strip().lower()
        if response == 'no' or response == 'n':
            print("Exiting the program. Thank you for using the tool!")
            break
        elif response == 'yes' or response == 'y':
            # Reset last paths to force new input
            last_image_path = None
            last_output_dir = None
        elif response == 'repeat' or response == 'r':
            # Keep last paths, ask for new scale, alpha, and duration
            continue
        else:
            print("Invalid input. Please type 'yes', 'no', or 'repeat'.")

if __name__ == "__main__":
    main()