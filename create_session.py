import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('pYqN3C1pQM3PdLSWPsAzfOuaLh_OBfPJLack9Mnm8_YF')
assistant = AssistantV2(
    version='2020-04-01',
    authenticator = authenticator
)

assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/4f1e8f08-3416-4773-a53e-c4208ae518ef')

response = assistant.create_session(
    assistant_id='91e2db9a-09c0-4db0-95a2-4165ab98b7a9',
).get_result()

print(json.dumps(response, indent=2))
