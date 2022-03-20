from .._fake_builtin import *  # Use in development, will be ignored in production


def main(text):
    thisamo.mixin_messenger.send_me_text_message(text)
    thisamo.mixin_messenger.send_me_post_message("# test post\n" + "- [x] Hello world")


main(thisamo.args["what"])
