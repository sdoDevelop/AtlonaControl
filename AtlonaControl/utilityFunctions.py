import telnetlib


def to_bytes(line):
    return f"{line}\n".encode("utf-8")


def sendTelnet(ip, port, command):
    with telnetlib.Telnet(ip) as telnet:
        print(ip, str(port), command)
        telnet.read_until(b'\n')
        telnet.write(to_bytes(command + "\r"))
        allReturn = []
        telnetReturn = '-'
        while telnetReturn != '':
            telnetReturn = telnet.read_until(b'\n', 0.1).decode()
            allReturn.append(telnetReturn)

            if 'FAILED' in telnetReturn:
                print(telnetReturn)
                raise ChildProcessError(telnetReturn)

        return ''.join(allReturn)
