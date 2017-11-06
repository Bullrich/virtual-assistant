from grey_matter import log


def get_recording_devices():
    import speech_recognition as sr
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        log("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
