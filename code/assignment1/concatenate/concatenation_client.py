import sys
import random
import string

RAND_STR_LEN = 10

# TODO: Import socket library


# Random alphanumeric string. Do not change
def rand_str():
    ret = ""
    for i in range(RAND_STR_LEN):
        ret += random.choice(
            string.ascii_lowercase + string.ascii_uppercase + string.digits
        )
    return ret


NUM_TRANSMISSIONS = 10


def client_socket_setup(server_port):
    pass
    # TODO: Create and return the socket for the client

    # TODO:  Connect this socket to the server


def transmit_using_socket(client_socket):
    # Transmit NUM_TRANSMISSIONS number of times
    for i in range(NUM_TRANSMISSIONS):
        pass
        # TODO: Generate a random string of length 10 using rand_str function

        # TODO: Send random string to the server

        # TODO: Print data for debugging

        # TODO: Receive concatenated data back from server as a byte array

        # TODO: Print out concatenated data for debugging

        # TODO: Close socket


if __name__ == "__main__":
    if len(sys.argv) > 4 or len(sys.argv) < 3:
        print("Usage: python3 " + sys.argv[0] + " server_address server_port [random_seed]")
        sys.exit(1)

    if len(sys.argv) == 4:
        random_seed = int(sys.argv[3])
        random.seed(random_seed)

    server_address = sys.argv[1]
    server_port = int(sys.argv[2])

    client_socket = client_socket_setup(server_port)
    transmit_using_socket(client_socket)
