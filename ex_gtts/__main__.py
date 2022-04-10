import sys
import time
from gtts import gTTS
from io import BytesIO
from lamedec import decode
from openal import oalQuit, AL_PLAYING, WaveFile, Source, Buffer


def usage():
    print(f"usage: %s <Lang> <Text>" % sys.argv[0])
    sys.exit()


def main(lang, text):
    with (
        BytesIO() as mp3_fp,
        BytesIO() as wav_fp,
    ):
        tts = gTTS(text=text, lang=lang)
        tts.write_to_fp(mp3_fp)

        mp3_fp.seek(0)
        decode(mp3_fp, wav_fp)

        wav_fp.seek(0)
        buf = Buffer(WaveFile(wav_fp))
        source = Source(buf)
        source.play()

        while source.get_state() == AL_PLAYING:
            time.sleep(1)

        oalQuit()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()
    main(sys.argv[1], sys.argv[2])
