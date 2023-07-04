import banana_dev as banana
import json
import argparse
import base64 #
import skimage.io #
from PIL import Image #
from utils import Timer,encodeBase64Image
TODO = None
def main(args):
    #===============================================
    # SECRETS
    with open('secrets.json','r') as f:
        secrets = json.load(f)
    api_key = secrets['API_KEY']
    model_key = secrets['MODEL_KEY']
    #===============================================
    if TODO:
        # REQUEST
        image  = skimage.io.imread(args.img_path)
        image = Image.fromarray(image)
        image_base64 = encodeBase64Image(image)
        # https://stackoverflow.com/questions/30224729/convert-wav-to-base64
        audio_base64 = base64.b64encode(open(args.audio_path, "rb").read())

        request_json = {
            'image':image_base64,
            'audio':audio_base64}
        model_inputs = request_json
        # model_inputs = {YOUR_MODEL_INPUT_JSON} # anything you want to send to your model
    #===============================================
    # RESPONSE
    with Timer('api call'):
        out = banana.run(api_key, model_key, model_inputs)
    # assert False,'from here'
    # import pdb;pdb.set_trace()
    model_outputs = out['modelOutputs']
    assert isinstance(model_outputs,list),f'expecting response["modelOutputs"] to be a list, found {model_outputs.__class__}'
    assert len(model_outputs) == 1, f'length of response["modelOutputs"] be 1, found {len(response["modelOutputs"])}'
    model_outputs = model_outputs[0]
    print(f'status:{model_outputs["message"]}')
    if TODO:
        video_base64 = model_outputs['result']
        with open(args.save_path,'wb') as f:
            f.write(base64.b64decode(video_base64))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--audio_path",default=r"./demo/audio/intro.wav",help="audio file sampled as 16k hz")
    parser.add_argument("--img_path",default=r"./demo/img/paint.jpg", help="reference image")
    parser.add_argument("--save_path",default=r"./results.mp4", help="save path")
    # parser.add_argument('--video',type=str,default='driving.mp4',help='name of the driving video (on the banana server)')
    args = parser.parse_args()
    main(args)
