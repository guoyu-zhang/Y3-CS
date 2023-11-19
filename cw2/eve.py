import sys
import os

from common import *
from const import *

if len(sys.argv) != 2:
    print("Please choose a flag: --relay, --break-heart, --custom")
    sys.exit(1)
    
flag = sys.argv[1]

dialog = Dialog('print')

# Connection setup
print("CONNECTING... Alice to 'Bob' (Eve)")
player_bob = "bob"
socket_bob, aes_bob = setup(player_bob, BUFFER_DIR, BUFFER_FILE_NAME)
print("CONNECTED Alice to 'Bob' (Eve)")

os.rename(BUFFER_DIR + BUFFER_FILE_NAME, BUFFER_DIR + "buffer2")

print("CONNECTING Bob to 'Alice' (Eve)")
player_alice = "alice"
socket_alice, aes_alice = setup(player_alice, BUFFER_DIR, BUFFER_FILE_NAME)
print("CONNECTED Bob to 'Alice' (Eve)")


# Receiving and sending messages
received_from_bob = receive_and_decrypt(aes_alice, socket_alice)

if flag == "--relay":
    dialog.chat('Bob said: "{}"'.format(received_from_bob))
    encrypt_and_send(received_from_bob, aes_bob, socket_bob)

    received_from_alice = receive_and_decrypt(aes_bob, socket_bob)
    dialog.chat('Alice said: "{}"'.format(received_from_alice))
    encrypt_and_send(received_from_alice, aes_alice, socket_alice)
    
elif flag == "--break-heart":
    corrupted_from_bob = BAD_MSG[player_bob]
    dialog.chat('Bob said: "{}"'.format(corrupted_from_bob))
    encrypt_and_send(corrupted_from_bob, aes_bob, socket_bob)
    
    received_from_alice = receive_and_decrypt(aes_bob, socket_bob)
    dialog.chat('Alice said: "{}"'.format(received_from_alice))
    encrypt_and_send(received_from_alice, aes_alice, socket_alice)
    
elif flag == "--custom":
    message_to_alice = input("Enter message to send to Alice from 'Bob': ")
    dialog.chat('Bob said: "{}"'.format(message_to_alice))
    encrypt_and_send(message_to_alice, aes_bob, socket_bob)
    
    received_from_alice = receive_and_decrypt(aes_bob, socket_bob)
    dialog.info("Real message received from Alice: {}".format(received_from_alice))
    
    message_to_bob = input("Enter message to send to Bob from 'Alice': ")
    dialog.chat('Alice said: "{}"'.format(message_to_bob))
    encrypt_and_send(message_to_bob, aes_alice, socket_alice)

# Tear down sockets
tear_down(socket_alice, BUFFER_DIR, BUFFER_FILE_NAME)
tear_down(socket_bob, BUFFER_DIR, "buffer2")