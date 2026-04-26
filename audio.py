from chat_state import current_volume, current_bass, current_eq

def get_filter(volume=None, bass=None, eq=None):
    v = volume or current_volume
    b = bass or current_bass
    e = eq or current_eq

    vol = v / 100.0
    bass_filter = f"equalizer=f=60:width_type=o:width=2:g={b}"

    if e == "bass":
        eq_filter = f"{bass_filter},equalizer=f=170:width_type=o:width=2:g=8"
    elif e == "treble":
        eq_filter = f"equalizer=f=3000:width_type=o:width=2:g=8,equalizer=f=8000:width_type=o:width=2:g=10"
    elif e == "clear":
        eq_filter = f"equalizer=f=1000:width_type=o:width=2:g=5,equalizer=f=3000:width_type=o:width=2:g=3"
    elif e == "vocal":
        eq_filter = f"equalizer=f=800:width_type=o:width=2:g=6,equalizer=f=2500:width_type=o:width=2:g=5"
    else:
        eq_filter = bass_filter

    return (
        f"volume={vol},"
        f"{eq_filter},"
        f"aresample=48000,"
        f"aformat=sample_fmts=s16:channel_layouts=stereo,"
        f"highpass=f=20,"
        f"lowpass=f=20000,"
        f"dynaudnorm=f=150:g=15"
    )

def get_ffmpeg_cmd(filter_str):
    return (
        f"ffmpeg -f pulse -i default "
        f"-af '{filter_str}' "
        f"-f s16le -ac 2 -ar 48000 "
        f"-acodec pcm_s16le pipe:1"
    )
