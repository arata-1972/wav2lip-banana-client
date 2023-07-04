import time
from io import BytesIO
class Timer():
    def __init__(self,name):
        self.name = name
    def __enter__(self,):
        self.tic = time.time()
        pass
    def __exit__(self,*args,**kwargs):
        self.toc = time.time()
        self.elapsed = self.toc - self.tic
        print(f'time taken for {self.name} is {self.elapsed}')
        pass
def encodeBase64Image(image: Image) -> str:
    # https://stackoverflow.com/questions/31826335/how-to-convert-pil-image-image-object-to-base64-string
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_str

