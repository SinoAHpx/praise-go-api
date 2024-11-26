import base64
import mimetypes
import io
from pathlib import Path
from PIL import Image

def getImgMimeType(image_path: str):
    type = mimetypes.guess_type(image_path)
    return type[0]

def getImgFomat(image_path: str):
    mime = getImgMimeType(image_path)
    slash = mime.index('/')
    return mime[(slash + 1):]
    
def imgToBase64Url(image_path: str) -> str:
    # Get the mime type based on file extension
    mime_type, _ = mimetypes.guess_type(image_path)
    if not mime_type or not mime_type.startswith('image/'):
        raise ValueError("File must be an image")
        
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return f"data:{mime_type};base64,{encoded_string}"

def getCompressedSize(width, height) -> float:
    max_dimension = 1368

    if width <= max_dimension and height <= max_dimension:
        return 1.0

    if width > height:
        return max_dimension / width
    else:
        return max_dimension / height

def compressImg(img_local_path: str) -> bytes:
    img = Image.open(img_local_path)
    compress_ratio = getCompressedSize(img.width, img.height)
    
    new_width = int(img.width * compress_ratio)
    new_height = int(img.height * compress_ratio)
    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    output_buffer = io.BytesIO()
    
    img_format = getImgFomat(img_local_path)
    
    img.save(output_buffer, format=img_format, optimize=True, quality=50)
    output_buffer.seek(0)
    
    compressed = output_buffer.getvalue()
    
    return compressed
    
def compressImgToBase64(img_local_path: str) -> str:
    b64 = compressImg(img_local_path)
    compressed_img = base64.b64encode(b64).decode('utf-8')
    
    return compressed_img