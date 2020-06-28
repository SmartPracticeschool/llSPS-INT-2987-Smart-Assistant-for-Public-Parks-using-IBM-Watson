import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson import AssistantV2
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from playsound import playsound

#Speech to text credentials:

authenticator = IAMAuthenticator('3q46ytQO4ftl2pFmunP1VoNWyK-EyAjGjOhlgmkt-GOv')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/fe05bc36-660d-4330-bc0e-bc6c9c7a53a2')

#IBM Watson Assistant credentials:

authenticator = IAMAuthenticator('pYqN3C1pQM3PdLSWPsAzfOuaLh_OBfPJLack9Mnm8_YF')
assistant = AssistantV2(
    version='2020-04-01',
    authenticator = authenticator
)

assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/4f1e8f08-3416-4773-a53e-c4208ae518ef')

#Creating Session id:

response = assistant.create_session(
    assistant_id='0b8b59bb-23b1-485e-9da0-f6cccbe5e053',
).get_result()


#Text to Speech credentials:

authenticator = IAMAuthenticator('wsDPlrLmNuqTX-zHJbxeUshfblaBOEB9zOGCzh4KX9Mu')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/6265cfe4-5ac9-4783-8da6-84ca4ea07091')


with open(join(dirname(__file__), './.', 'file.mp3'),
               'rb') as audio_file:
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/mp3',
        
    ).get_result()
print(speech_recognition_results)
print(speech_recognition_results['results'][0]['alternatives'][0]['transcript'])



response1 = assistant.message(
    assistant_id='0b8b59bb-23b1-485e-9da0-f6cccbe5e053',
    session_id=response["session_id"],
    input={
        'message_type': 'text',
        'text': speech_recognition_results["results"][0]["alternatives"][0]["transcript"]
    }
).get_result()
print(response1)
print(json.dumps(response1, indent=2))
print(response1['output'][2]['generic'][1]['text'])

with open('file.mp3', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'response["output"][0]["generic"][1]["text"]',
            voice='en-US_AllisonV3Voice',
           accept='audio/mp3'        
        ).get_result().content)

playsound("file.mp3")
