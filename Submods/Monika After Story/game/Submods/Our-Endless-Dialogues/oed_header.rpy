{
    "header_version": 1,
    "author": "NiskoDT",
    "name": "Our Endless Dialogues",
    "version": "0.0.1-incomplete",
    "modules": [
        "main"
    ],
    "description": "This mod allows A.I. capabilities to talk to your Monika. Make sure the backend is already running.",
    "priority": 0
}

init -990 python in mas_submod_utils:
    Submod(
        author="NiskoDT",
        name="Our Endless Dialogues",
        description="This mod allows A.I. capabilities to talk to your Monika. Make sure the backend is already running."
        version="0.0.1-incomplete",
        settings_pane="oed_chat_settings",
    )