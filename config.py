import os

SOURCE_API_ID = int(os.environ.get("SOURCE_API_ID"))
SOURCE_API_HASH = os.environ.get("SOURCE_API_HASH")
SOURCE_PHONE = os.environ.get("SOURCE_PHONE")
TARGET_API_ID = int(os.environ.get("TARGET_API_ID"))
TARGET_API_HASH = os.environ.get("TARGET_API_HASH")
TARGET_PHONE = os.environ.get("TARGET_PHONE")
SOURCE_GROUP = int(os.environ.get("SOURCE_GROUP"))
OWNER_ID = int(os.environ.get("OWNER_ID"))
DEFAULT_VOLUME = int(os.environ.get("DEFAULT_VOLUME", 1000))
DEFAULT_BASS = int(os.environ.get("DEFAULT_BASS", 5))
DEFAULT_EQ = os.environ.get("DEFAULT_EQ", "normal")
