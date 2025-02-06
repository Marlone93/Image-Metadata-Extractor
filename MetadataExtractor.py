from PIL import Image
import exifread

def extract_metadata(image_path):
    metadata = {}
    try:
        with Image.open(image_path) as img:
            metadata["Format"] = img.format
            metadata["Mode"] = img.mode
            metadata["Size"] = img.size
    except Exception as e:
        metadata["PIL_Error"] = str(e)

    try:
        with open(image_path, "rb") as img_file:
            tags = exifread.process_file(img_file)
            for tag, value in tags.items():
                metadata[tag] = str(value)
    except Exception as e:
        metadata["EXIF_Error"] = str(e)

    return metadata

if __name__ == "__main__":
    image_path = input("Enter the path to the image: ")
    metadata = extract_metadata(image_path)

    print("\nExtracted Metadata:")
    for key, value in metadata.items():
        print(f"{key}: {value}")
