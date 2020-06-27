from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from playsound import playsound

authenticator = IAMAuthenticator('api_key')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('url')

with open('file_name.mp3', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'text',
            voice='en-US_AllisonV3Voice',
            accept='audio/mp3'        
        ).get_result().content)
playsound('file_name.mp3')
