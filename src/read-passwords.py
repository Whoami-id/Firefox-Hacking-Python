import firefox_decrypt  #https://github.com/unode/firefox_decrypt
import collections

from helper import get_firefox_path

path = get_firefox_path("places.sqlite")



def encrypt():
    A = collections.namedtuple("Arguments", ["verbose"])
    firefox_decrypt.setup_logging(A(2))
    nss = firefox_decrypt.NSSInteraction()

    
encrypt()