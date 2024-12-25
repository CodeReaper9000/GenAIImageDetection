from PIL import Image, ImageChops, ImageEnhance
import os

def compute_ela_for_image(image_path, output_path, jpeg_quality=95, amplify_factor=20):
    """
    Computes and saves the ELA map for a single image.
    
    Parameters:
        image_path (str): Path to the original image.
        output_path (str): Path to save the ELA map.
        jpeg_quality (int): Quality level for JPEG recompression (default is 95).
        amplify_factor (int): Factor to amplify differences in ELA maps (default is 20).
    """
    try:
        # Open the original image
        img = Image.open(image_path).convert('RGB')
        
        # Save as a high-quality JPEG to recompress
        compressed_path = "compressed_temp.jpeg"
        img.save(compressed_path, 'JPEG', quality=jpeg_quality)
        
        # Reopen the recompressed image
        compressed_img = Image.open(compressed_path)
        
        # Compute ELA map
        ela_map = ImageChops.difference(img, compressed_img)
        
        # Amplify the differences
        ela_map = ImageEnhance.Brightness(ela_map).enhance(amplify_factor)
        
        # Save the ELA map
        ela_map.save(output_path)
        
        # Cleanup temporary file
        os.remove(compressed_path)
        
        print(f"ELA map saved: {output_path}")
        
    except Exception as e:
        print(f"Failed to process {image_path}: {e}")

# Example usage
image_path = r"D:\downloads\real1.jpg"  # Input image path
output_path = r"D:\downloads\example_ela4.jpg"  # Output ELA map path

compute_ela_for_image(image_path, output_path)
