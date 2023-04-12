import cloudinary
from cloudinary.uploader import upload

def get_url_for_image(img_path:str):
    cloudinary.config(
        cloud_name = "ddm2qblsr",
        api_key = "728261189895959",
        api_secret = "D2s02RirwY-AwEIuohbsYqLJYsM"
    )

    result = upload(img_path)
    return result['url']

def main():
    img_path = 'images/test5.jpg'
    img_url = get_url_for_image(img_path)
    
    print(img_url)

if __name__ == '__main__' : 
    main()