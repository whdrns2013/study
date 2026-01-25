from core.image_explanation_api import image_explanation

def image_explanation_test_url():
    image_url = "https://images.unsplash.com/photo-1768185595109-18aded979f9d?q=80&w=1064&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    response = image_explanation(image_url=image_url)
    print(response)

def image_explanation_test_file():
    image_file_path = "data/image/sample_image.jpg"
    response = image_explanation(image_file_path=image_file_path)
    print(response)

def main():
    image_explanation_test_file()

if __name__ == "__main__":
    main()
