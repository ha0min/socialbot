#!/usr/bin/env python  
# -*- coding:utf-8 _*-


"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech, storage
import io


class TextToSpeech:
    client = None
    storage_client = None
    bucket = None
    blob = None
    baseurl = 'https://storage.googleapis.com/yours_gcp_bucket/'

    def __init__(self):
        self.client = texttospeech.TextToSpeechClient()
        self.storage_client = storage.Client(project='your_gcp_project_id')
        self.bucket = self.storage_client.bucket('your_gcp_bucket_name')
        pass

    def text_to_speech(self, text, name):
        # Set the text input to be synthesized
        synthesis_input = texttospeech.SynthesisInput(
            text=text)

        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Neural2-G",
        )

        # Select the type of audio file you want returned
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16
        )

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
        audio_content_length = len(response.audio_content)
        audio_length_seconds = round(audio_content_length / (2 * 16000))  # Assuming LINEAR16 encoding and 16 kHz sample rate

        url = self.upload_blob_from_memory(response.audio_content, name)

        return url, audio_length_seconds

    def upload_blob_from_memory(self, contents, name):
        """Uploads a file to the bucket."""

        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"

        # The contents to upload to the file
        # contents = "these are my contents"

        # The ID of your GCS object
        # destination_blob_name = "storage-object-name"
        self.blob = self.bucket.blob(name + '.wav')
        wav_data = io.BytesIO()
        wav_data.write(contents)
        wav_data.seek(0)

        # Upload the WAV data to the blob
        self.blob.upload_from_file(wav_data, content_type='audio/wav')
        print('File {} uploaded to {}.'.format(name + '.wav', 'newsclip'))

        return self.baseurl + name + '.wav'


if __name__ == '__main__':
    text_to_speech = TextToSpeech()
    text_to_speech.text_to_speech(
        'At 10:05, President Joe Biden and top Republican Kevin McCarthy are nearing a deal to avoid a U.S. debt default, with both sides expressing the possibility of reaching an agreement by the end of the week.',
        'test')
