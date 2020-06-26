from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from playsound import playsound

authenticator = IAMAuthenticator('Pc_DQ6-9smnDQJT7BFO_46Bq2qLfBWjQ8iaa2Rfn6DmE')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/21aca69a-86fe-4c6e-8a03-ed1b60eae6be')

with open('q3.mp3', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'The national park is accessible from Delhi, Moradabad, Nainital, Lucknow, Bareilly, and Dehradun by road through regular bus and taxi services. Delhi, Lucknow and Bareilly are connected to major cities in the country by road and rail.',
            voice='en-US_AllisonV3Voice',
            accept='audio/mp3'        
        ).get_result().content)
playsound('q3.mp3')
