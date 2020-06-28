import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('1yEZDDiwh78CPP9xkj_7rVqcfrP5H-I7C7t_rh4MXbfj')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/95d74b13-c57b-446c-84fc-35ef2b94b0d0')

with open(join(dirname(__file__), './.', 'q2.mp3'),
               'rb') as audio_file:
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/mp3',
      
    ).get_result()

print(json.dumps(speech_recognition_results, indent=2))
print(speech_recognition_results["results"][0]["alternatives"][0]["transcript"])
