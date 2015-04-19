import json

def build_identity_message(name, handle, number):
    return json.dumps({
        "type": "identity",
        "data": {
            "name": name,
            "handle": handle,
            "number": number
        }
    })

def build_target_message(handle):
    return json.dumps({
        "type": "target",
        "data": {
            "handle": handle
        }
    })

def build_video_frame_message(targetHandle, senderHandle, width, height, data):
    return json.dumps({
        "type": "videoframe",
        "data": {
            "content": data,
            "width": width,
            "height": height,
            "to": targetHandle,
            "from": senderHandle
        }
    })

def build_chat_message(handle, text):
    return json.dumps({
        "type": "chat",
        "data": {
            "text": text,
            "to": targetHandle,
            "from": senderHandle
        }
    })

def build_audio_snippet_message(targetHandle, senderHandle, snippet):
    return json.dumps({
        "type": "audiosnippet",
        "data": {
            "snippet": snippet,
            "to": targetHandle,
            "from": senderHandle
        }
    })