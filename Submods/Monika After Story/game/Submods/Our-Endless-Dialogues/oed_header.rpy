# Main header for the mod
init -990 python in mas_submod_utils:
    Submod(
        author="NiskoDT",
        name="Our Endless Dialogues",
        description="This mod allows A.I. capabilities to talk to your Monika. Make sure the backend is already running."
        version="0.0.1-incomplete",
        settings_pane="oed_chat_settings",
    )
    
# Submod Updater Plugin
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Your Submod Name",
            user_name="Your_GitHub_Login",
            repository_name="Name_of_the_Repository_for_Your_Submod"
        )