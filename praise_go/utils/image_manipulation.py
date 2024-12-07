import base64
import mimetypes
import io
from PIL import Image

def get_img_mime_type(image_path: str):
    type = mimetypes.guess_type(image_path)
    return type[0]

def get_img_format(image_path: str):
    mime = get_img_mime_type(image_path)
    slash = mime.index('/')
    return mime[(slash + 1):]
    
def from_image_to_base64_url(image_path: str) -> str:
    # Get the mime type based on file extension
    mime_type, _ = mimetypes.guess_type(image_path)
    if not mime_type or not mime_type.startswith('image/'):
        raise ValueError("File must be an image")
        
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return f"data:{mime_type};base64,{encoded_string}"

def compress_image(image_path, max_size=(1000, 1000)):
    # Open image
    img = Image.open(image_path)
    
    # Convert to RGB if necessary (e.g., for PNG with transparency)
    if img.mode in ('RGBA', 'P'): 
        img = img.convert('RGB')
    
    # Check if image is already smaller than max_size
    if img.size[0] <= max_size[0] and img.size[1] <= max_size[1]:
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG', optimize=True)
        return buffer.getvalue()
        
    # Calculate new dimensions maintaining aspect ratio
    ratio = min(max_size[0]/img.size[0], max_size[1]/img.size[1])
    new_size = tuple(int(dim * ratio) for dim in img.size)
    img = img.resize(new_size, Image.Resampling.LANCZOS)
    
    buffer = io.BytesIO()
    img.save(buffer, format='JPEG', optimize=True)
    
    return buffer.getvalue()
    
def from_image_to_compressed_base64(img_local_path: str) -> str:
    binary = compress_image(img_local_path)
    
    encoded_string = base64.b64encode(binary).decode('utf-8')

    compressed_img = f"data:image/jpeg;base64,{encoded_string}"
    return compressed_img