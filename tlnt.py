import telnetlib
import time


def to_bytes(line):
    return f"{line}\n".encode("utf-8")


#ip = input("IP: ")
#user = input("USER: ")
#passw = input("PASS: ")


with telnetlib.Telnet('192.168.8.21', 23, 1) as tn:
    time.sleep(1)
    tn.write(to_bytes('admin'))
    tn.write(to_bytes('mountainlion'))

    while True:

        print(tn.read_until(b"#", timeout=2).strip().decode('utf-8'), end='')
        inpt = input()
        tn.write(to_bytes(inpt.strip()+'\r'))


        '''tn.write(to_bytes(user))
        time.sleep(1)
        print(tn.read_until(b">", timeout=2).decode("utf-8"), end='')
        tn.write(to_bytes(passw))
        tn.write(to_bytes('exit'))
        print(tn.read)
        break'''