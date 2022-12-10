import os


class Config:

    BOT_TOKEN = os.environ.get("5430633602:AAHtrxIIIRbxalvrbTmWaUFY07lS_J5yHJo")

    SESSION_NAME = os.environ.get("SESSION_NAME", ":memory:")

    API_ID = int(os.environ.get("18581427"))

    API_HASH = os.environ.get("8910dd19c92a4c5a95530b73d1708944")

    CLIENT_ID = os.environ.get("862415355319-50ncp1tqt0s2m2tvqp24hjejtlcr9v5r.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("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")

    BOT_OWNER = int(os.environ.get("@ashmitjaiswal"))

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER, 374321319] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("public") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
