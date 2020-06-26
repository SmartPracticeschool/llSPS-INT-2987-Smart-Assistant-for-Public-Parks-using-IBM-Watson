from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from playsound import playsound

authenticator = IAMAuthenticator('Pc_DQ6-9smnDQJT7BFO_46Bq2qLfBWjQ8iaa2Rfn6DmE')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/21aca69a-86fe-4c6e-8a03-ed1b60eae6be')

with open('q6.mp3', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'All the eating facilities are going to be provided by the accommodation facilities which is included in the booking fee of the hotel.',
            voice='en-US_AllisonV3Voice',
            accept='audio/mp3'        
        ).get_result().content)
playsound('q6.mp3')
