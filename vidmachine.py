from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
client = speech.SpeechClient()

from textblob import TextBlob
from duckscrape import *
import io
from moviepy.editor import *

speech_file = "file.wav"

# Read bytes from audio file
with io.open(speech_file, 'rb') as audio_file:
    content = audio_file.read()

print("file read successfully")

audio = types.RecognitionAudio(content=content)

# Speech recognition config
config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en-US',
    enable_word_time_offsets=True)

operation = client.long_running_recognize(config, audio)

print('Waiting for operation to complete...')
result = operation.result(timeout=90)

# Variables for the transcript
full_transcript = None
transcript_tuples = []

# Result handling config
for result in result.results:
    alternative = result.alternatives[0]
    print(u'Transcript: {}'.format(alternative.transcript))
    print('Confidence: {}'.format(alternative.confidence))

    full_transcript = alternative.transcript

    for word_info in alternative.words:
        word = word_info.word
        start_time = word_info.start_time
        end_time = word_info.end_time
        num_start_time = start_time.seconds + start_time.nanos * 1e-9
        num_end_time = end_time.seconds + end_time.nanos * 1e-9
        print('Word: {}, start_time: {}, end_time: {}'.format(
            word,
            num_start_time,
            num_end_time))

        transcript_tuples.append((word, num_end_time - num_start_time, num_start_time, num_end_time))

print("transcription completed boii")

blob = TextBlob(full_transcript)
noun_phrases = blob.noun_phrases
nouns = [n for n,t in blob.tags if t == 'NN']

print(nouns)

image_tuples = []
for noun in nouns:
    for thing in transcript_tuples:
        if thing[0].lower() == noun.lower():
            obj = search(noun, True)
            with open(urllib.parse.quote_plus(image_tuple[0]["url"]), 'wb') as handle:
                response = requests.get(pic_url, stream=True)
                if not response.ok:
                    print(response)
                    exit(0)
                for block in response.iter_content(1024):
                    if not block:
                        break

                handle.write(block)
            
            image_tuples.append((obj[0], thing[1], thing[2], thing[3]))

audio = AudioFileClip(speech_file)
audio_length = audio.duration
my_images = []

import urllib.parse

for i, image_tuple in enumerate(image_tuples):
    if len(image_tuples) - 1 != i:
        my_images.append(mp.ImageClip(urllib.parse.quote_plus(image_tuple[0]["url"]))
            .set_duration(image_tuples[i + 1][2] - image_tuple[2])
            .resize(( 1920, 1080 )) # if you need to resize...
            .set_pos(("center","center")))
    else:
        my_images.append(mp.ImageClip("logo.png")
            .set_duration(audio_length - image_tuple[2])
            .resize(( 1920, 1080 )) # if you need to resize...
            .set_pos(("center","center")))

concat_clip = mp.concatenate_videoclips(my_images, method="compose")
concat_clip.write_videofile("out.mp4", fps=30, audio=speech_file)
