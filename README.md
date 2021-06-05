# mCodingYouTube

This repository contains the code I use to automatically update my videos' metadata on YouTube, including: titles, descriptions, tags, etc.

[mCoding YouTube channel](https://www.youtube.com/c/mCodingWithJamesMurphy)

The code in this repository is MIT licensed, see the file named LICENSE.

### Disclaimer
The code is for educational purposes, not production use.
Do not run any code that you do not understand.
I am not responsible if you end up deleting or otherwise irreparably damaging your YouTube account,
or getting banned from YouTube/Google services by using/misusing this code.

If you do decide to play with the code, I recommend using a dummy YouTube account so that you don't put your real account in danger.
Pay close attention to the amount of quota that you use in order to avoid YouTube/Google thinking you are abusing their API.

I do not condone using or modifying the code in this API to do anything that violates YouTube/Google terms of service or any applicable laws.

### Official code and docs from Google/YouTube
If you would like an official set of samples for how to use the YouTube Data API in Python, see https://github.com/youtube/api-samples/tree/master/python.

The official YouTube Data API documentation (not language specific) can be found at: https://developers.google.com/youtube/v3/docs.

### Trying to follow my YouTube video?
Video: [I Used the YouTube API to Update My Video Descriptions](https://youtu.be/0F9sdRtbwkE)

Install dependencies (execute this from the directory containing requirements.txt):

```shell
pip install -r requirements.txt
```

Here are the important files:

- app_config.py: In order to avoid publishing my secret client data, I use this config to read a non-uploaded file containing the location of my secret file. 
  If you want to modify the code to work for yourself, you can hard-code the location of your client secret file here, or use dotenv like I did.
   
- youtube.py: Contains the code to make an authenticated YouTube service object.
  You shouldn't need to change anything in this file.
  
- download_single_video_data.py: Script to download the snippet metadata to a file for a video with known video id.
  I recommend making a data directory and putting all your downloaded data there to avoid clutter.
  
- download_my_uploads.py: Script to download the playlist item snippets for all your uploads and save each page of results to a file. 

- update_description_on_youtube.py: Functions for updating a single video description.

- simple_prepend_to_descriptions.py: Script to load data saved using download_my_uploads.py and prepend text read from a file to all your uploaded videos
  by using functions from update_description_on_youtube.py in a loop.