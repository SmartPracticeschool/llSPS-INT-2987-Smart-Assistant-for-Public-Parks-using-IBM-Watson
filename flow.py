[
    {
        "id": "878c37c4.502cc8",
        "type": "tab",
        "label": "Flow 7",
        "disabled": false,
        "info": ""
    },
    {
        "id": "20b9e5f.7d5471a",
        "type": "ui_button",
        "z": "878c37c4.502cc8",
        "name": "",
        "group": "bb616a8f.6034f8",
        "order": 0,
        "width": 0,
        "height": 0,
        "passthru": false,
        "label": "button",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "Hey!",
        "payloadType": "str",
        "topic": "Smart Park",
        "x": 1310,
        "y": 360,
        "wires": [
            [
                "d38fea3e.515118",
                "6a001fec.ce8f2",
                "8eccd86c.9eb3f8",
                "fff80e37.58c9b",
                "84ea0a2d.d39708"
            ]
        ]
    },
    {
        "id": "d38fea3e.515118",
        "type": "debug",
        "z": "878c37c4.502cc8",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "targetType": "msg",
        "x": 1490,
        "y": 420,
        "wires": []
    },
    {
        "id": "6a001fec.ce8f2",
        "type": "ui_text",
        "z": "878c37c4.502cc8",
        "group": "bb616a8f.6034f8",
        "order": 1,
        "width": 0,
        "height": 0,
        "name": "",
        "label": "CLICK HERE TO CONNECT WITH US THROUGH CHAT",
        "format": "{{msg.payload}}",
        "layout": "row-spread",
        "x": 1660,
        "y": 380,
        "wires": []
    },
    {
        "id": "84ea0a2d.d39708",
        "type": "watson-conversation-v1",
        "z": "878c37c4.502cc8",
        "name": "",
        "workspaceid": "91e2db9a-09c0-4db0-95a2-4165ab98b7a9",
        "multiuser": false,
        "context": true,
        "empty-payload": false,
        "service-endpoint": " https://api.eu-gb.assistant.watson.cloud.ibm.com/instances/4f1e8f08-3416-4773-a53e-c4208ae518ef",
        "timeout": "",
        "optout-learning": false,
        "x": 1840,
        "y": 520,
        "wires": [
            []
        ]
    },
    {
        "id": "fff80e37.58c9b",
        "type": "ui_toast",
        "z": "878c37c4.502cc8",
        "position": "top right",
        "displayTime": "3",
        "highlight": "",
        "sendall": true,
        "outputs": 0,
        "ok": "OK",
        "cancel": "",
        "raw": false,
        "topic": "",
        "name": "",
        "x": 1510,
        "y": 460,
        "wires": [],
        "info": "<html>\n<head>\n<head>\n<body>\n## **connecting through chat**\n</body>\n</html>"
    },
    {
        "id": "8eccd86c.9eb3f8",
        "type": "ui_audio",
        "z": "878c37c4.502cc8",
        "name": "",
        "group": "bb616a8f.6034f8",
        "voice": "en-US",
        "always": "",
        "x": 1520,
        "y": 340,
        "wires": []
    },
    {
        "id": "17a0d5f7.7004ca",
        "type": "http in",
        "z": "878c37c4.502cc8",
        "name": "",
        "url": "smartpark",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 1190,
        "y": 300,
        "wires": [
            [
                "b0b3290e.4b01c8"
            ]
        ]
    },
    {
        "id": "b0b3290e.4b01c8",
        "type": "template",
        "z": "878c37c4.502cc8",
        "name": "",
        "field": "payload",
        "fieldType": "msg",
        "format": "handlebars",
        "syntax": "mustache",
        "template": "Connect with us through chat",
        "output": "str",
        "x": 1360,
        "y": 300,
        "wires": [
            [
                "1edc1574.80983b"
            ]
        ]
    },
    {
        "id": "1edc1574.80983b",
        "type": "http response",
        "z": "878c37c4.502cc8",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 1520,
        "y": 300,
        "wires": []
    },
    {
        "id": "bb616a8f.6034f8",
        "type": "ui_group",
        "z": "",
        "name": "button",
        "tab": "5cc16102.e9d39",
        "order": 1,
        "disp": true,
        "width": "6",
        "collapse": false
    },
    {
        "id": "5cc16102.e9d39",
        "type": "ui_tab",
        "z": "",
        "name": "1",
        "icon": "dashboard",
        "disabled": false,
        "hidden": false
    }
]
