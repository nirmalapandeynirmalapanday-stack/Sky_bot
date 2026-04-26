from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types.input_stream.audio_parameters import AudioParameters
from clients import source_calls, target_calls
from audio import get_filter, get_ffmpeg_cmd
from config import SOURCE_GROUP
from rom_state import set_source_joined, add_target, remove_target

async def source_join():
    try:
        f = get_filter()
        cmd = get_ffmpeg_cmd(f)
        await source_calls.join_group_call(
            SOURCE_GROUP,
            AudioPiped(
                cmd,
                AudioParameters(bitrate=320, channels=2, sample_rate=48000)
            )
        )
        set_source_joined(True)
        return True
    except Exception as e:
        print(f"Source error: {e}")
        return False

async def target_join(group_id):
    try:
        f = get_filter()
        cmd = get_ffmpeg_cmd(f)
        await target_calls.join_group_call(
            group_id,
            AudioPiped(
                cmd,
                AudioParameters(bitrate=320, channels=2, sample_rate=48000)
            )
        )
        add_target(group_id, {"active": True})
        return True
    except Exception as e:
        print(f"Target error: {e}")
        return False

async def target_leave(group_id):
    try:
        await target_calls.leave_group_call(group_id)
        remove_target(group_id)
        return True
    except Exception as e:
        print(f"Leave error: {e}")
        return False

async def leave_all_targets():
    from rom_state import get_targets
    count = 0
    for gid in list(get_targets().keys()):
        try:
            await target_calls.leave_group_call(gid)
            count += 1
        except:
            pass
    return count
