import speech_recognition as sr
import wave


def recognize_and_save_voice():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)

        # Print the recognized text
        print("Recognized Text: ", text)

        # Save the audio recording as a WAV file
        with wave.open("../recorded_audio.wav", "wb") as wav_file:
            wav_file.setnchannels(1)
            print(audio.sample_width, audio.sample_rate)
            wav_file.setsampwidth(audio.sample_width)
            wav_file.setframerate(audio.sample_rate)
            wav_file.writeframes(audio.get_raw_data())

        print("Audio recording saved as 'recorded_audio.wav' successfully.")

        # Write the recognized text to a text file
        with open("../recognized_text.txt", "w") as file:
            file.write(text)

        print("Text written to 'recognized_text.txt' successfully.")

    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("Error occurred while requesting results from Google Speech Recognition service; {0}".format(e))


if __name__ == "__main__":
    recognize_and_save_voice()
