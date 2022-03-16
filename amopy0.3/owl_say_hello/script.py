from ..._fake_builtin import *  # Use in development, will be ignored in production


def main():
    owl = extensions.owl
    msg = owl.mixin_messenger.pack_message("text", thisamo.args["what"])
    owl.mixin_messenger.send_me_messages([msg])


main()
