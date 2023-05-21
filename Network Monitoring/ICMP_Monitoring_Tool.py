import socket
import struct
import os
import time
from datetime import date


# I did not write below code and take it from pyping
def calculate_checksum(source_string):
    sum = 0
    max_count = (len(source_string) / 2) * 2
    count = 0
    while count < max_count:
        # To make this program run with Python 2.7.x:
        # val = ord(source_string[count + 1])*256 + ord(source_string[count])
        # ### uncomment the above line, and comment out the below line.
        val = source_string[count + 1] * 256 + source_string[count]
        # In Python 3, indexing a bytes object returns an integer.
        # Hence, ord() is redundant.

        sum = sum + val
        sum = sum & 0xffffffff
        count = count + 2

    if max_count < len(source_string):
        sum = sum + ord(source_string[len(source_string) - 1])
        sum = sum & 0xffffffff

    sum = (sum >> 16) + (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer


def packet_maker(id=42):
    checksum = 0
    # bbHHh = signed char, signed char, unsigned short, unsigned short, short
    # type (8), code (8), checksum (16), id (16), sequence (16) bit
    header = struct.pack("bbHHh", 8, 0, checksum, id, 1)
    payload = b'abcdefghijklmnopqrstuvwabcdefghi' # dummy payload
    checksum = calculate_checksum(header + payload)

    # replace checksum
    header = struct.pack("bbHHh", 8, 0, socket.htons(checksum), id, 1)
    packet = header + payload
    return packet


def ping_host(address, alive=False, timeout=2):
    m_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname("icmp"))
    m_socket.settimeout(int(timeout))

    packet = packet_maker()

    try:
        socket.gethostbyname(address)
    except:
        print("cannot found a host by that name, retry...")
        return

    start_time = time.time()
    while packet:
        send = m_socket.sendto(packet, (address, 1))
        packet = packet[send:]

    taken_time = receive_ping(m_socket, start_time, alive)
    taken_time = round(taken_time * 1000.0, 4)
    m_socket.close()
    return taken_time


def receive_ping(m_socket, start_time, alive):
    try:
        reply, addr = m_socket.recvfrom(1024)
        taken_time = time.time() - start_time
        if alive == True:
            print("I AM ALIVE!\n")
        return taken_time
    except:
        print("I am probably dead (or I'm ignoring you)...\n")
        return 1234


def rtt_calculator(address, number_of_packet):
    number_of_packet = int(number_of_packet)
    measurements = []
    while number_of_packet > 0:
        measurements.append(ping_host(address))
        number_of_packet -= 1
    min_rtt = min(measurements)
    max_rtt = max(measurements)
    average_rtt = sum(measurements) / len(measurements)
    return min_rtt, max_rtt, average_rtt


def tracert(address):
    log = []
    ttl = 1
    while True:
        end_time = []
        id = 41  # Arbitrary number
        m_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname("icmp"))
        m_socket.settimeout(4)  # default windows tracert is 4 sec
        m_socket.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, ttl)
        no_of_chances = 3
        DONE = False
        while no_of_chances > 0:
            try:
                id += 1  # If we don't increase id, server will block us!
                packet = packet_maker(id)
                m_socket.sendto(packet, (address, 1))  # dummy 1 port
                start_time = time.time()
                # Did we reach our destination?
                packet, return_address = m_socket.recvfrom(1024)
                end_time.append(round((time.time() - start_time) * 1000, 4))
                no_of_chances -= 1
                time.sleep(0.1)  # In another project that solved my send problem, python sends too fast
            except:
                # if socket give timeout exception:
                no_of_chances -= 1
                end_time.append("*")
                time.sleep(0.1)  # In another project that solved my send problem, python sends too fast
                continue
        if return_address[0] == address:
            DONE = True  # we reach our destination!
        try:
            # ip to website name
            m_socket.settimeout(0.5)
            website = socket.gethostbyaddr(return_address[0])[0]
        except:
            website = return_address[0]  # if no known name is available
        if end_time == ["*", "*", "*"]:
            print(f"TTL: {ttl}, RTT:{end_time} Request timed out.")
            log.append(f"TTL: {ttl}, RTT:{end_time} Request timed out.")
        else:
            print(f"TTL: {ttl}, RTT:{end_time}, Address: {website}, IP: {return_address[0]}")
            log.append(f"TTL: {ttl}, RTT:{end_time}, Address: {website}, IP: {return_address[0]}")
        if DONE:
            m_socket.close()
            break
        ttl += 1  # Change ttl and reach another host
    return log


# ENDLESS LOOP
print(f"Welcome ***{os.getlogin()}***! ")
while True:
    user_input = input("Write function name to use program, q to exit, help to open documentation!\n")
    if user_input == "q":
        exit(0)
    elif user_input == "help":
        with open("readme.txt") as doc:
            print(doc.read())
    elif "are you alive" in user_input:
        address = user_input.split()[3]
        try:
            timeout = user_input.split()[4]
        except:
            timeout = 2
        ping_host(address, True, timeout)
    elif "latency" in user_input:
        address = user_input.split()[1]
        try:
            no_of_packets = user_input.split()[2]
        except:
            no_of_packets = 4
        min_val, max_val, average_val = rtt_calculator(address, no_of_packets)
        print(f"Number of packets send: {no_of_packets} to address: {address}\n"
              f"Minimum time: {min_val} ms\n"
              f"Maximum time: {max_val} ms\n"
              f"Average time: {average_val} ms\n")
    elif "how to reach" in user_input or "tracert" in user_input:
        try:
            address = user_input.split()[3]
        except:
            address = user_input.split()[1]
        logs = tracert(address)
        user_input = input("Do you want to save these informations into log.txt? (y/n)\n")
        if user_input == "y":
            cur_time = str(date.today()) + " " + str(time.strftime("%H-%M-%S"))
            with open(f"log-{cur_time}.txt", "w") as log_file:
                log_file.write("Traceroute log")
                log_file.write(str(date.today()) + " " + str(time.strftime("%H:%M:%S")) + "\n\n")
                for i in range(0, len(logs)):
                    log_file.write(logs[i] + "\n")
        else:
            continue
    elif "hostname" in user_input:
        address = user_input.split()[1]
        try:
            m_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname("icmp"))
            m_socket.settimeout(4)
            print("name: ", socket.gethostbyaddr(address)[0])
            print("Address List: ", socket.gethostbyaddr(address)[2])
            print("")
        except:
            print("Could not connect to address!")
    else:
        print("No command found like that, try again.")

# resources
# http://www.tcpipguide.com/free/t_ICMPv4EchoRequestandEchoReplyMessages-2.htm
# https://docs.python.org/3/library/socket.html#socket-timeouts
