from utilityFunctions import sendTelnet


def func_resetAll(ip, port):
    """
        Resets the matrix to the factory-default one-to-one routing state.
        This command only resets the input/output routing:
        Input 1 > Output 1, Input 2 > Output 2, etc. No other settings are affected.

    :param ip:
    :param port:
    :return:
    """
    telnetReturn = sendTelnet(ip, port, 'All#')
    return telnetReturn


def func_getBlink(ip, port):
    """
        Gets the current power button blinking state.
        True = on
        False = off

    :param ip:
    :param port:
    :return:
    """
    telnetReturn = sendTelnet(ip, port, 'Blink sta')
    if 'off' in telnetReturn:
        return False
    else:
        return True


def func_setBlink(ip, port, value):
    """
        Enables or disables power button blink.
        True = on
        False = off

    :param ip:
    :param port:
    :param value:
    :return:
    """
    commandValue = 'on' if value else 'off'
    telnetReturn = sendTelnet(ip, port, f'Blink {commandValue}')
    return telnetReturn


def func_getBroadcast(ip, port):
    """
        Gets current broadcast mode.
        True = on
        False = off

    :param ip:
    :param port:
    :return: bool
    """
    telnetReturn = sendTelnet(ip, port, 'Broadcast sta')
    if 'off' in telnetReturn:
        return False
    else:
        return True


def func_setBroadcast(ip, port, value):
    """
        Enables or disables broadcast mode. By default, broadcast mode is set to off. When set to on, changes in the web
        GUI will also be affected on the control system (if connected), via TCP/IP. To separate control between web
        GUI and Telnet, set this feature off. on = enables broadcast mode; off = disables broadcast mode.
        True = on
        False = off

    :param ip:
    :param port:
    :param value: bool
    :return:
    """
    commandValue = 'on' if value else 'off'
    telnetReturn = sendTelnet(ip, port, f'Broadcast {commandValue}')
    return telnetReturn


def func_clearPreset(ip, port, preset):
    """
        Erases the specified preset

    :param ip:
    :param port:
    :param preset: Range 1 ... 50
    :return:
    """
    preset = str(preset)
    telnetReturn = sendTelnet(ip, port, f'Clear{preset}')
    return telnetReturn


def func_setCSpara(ip, port, baudRate, dataBits, parityBit, stopBits):
    """
        Sets the baud rate, data bits, parity bit, and stop bits for the RS-232 port on the AT-UHD-PRO3-66M. Use the sta
        argument to display the current serial port settings. Each argument must be separated by a comma; no spaces are
        permitted. Brackets must be used when executing this command.

    :param ip:
    :param port:
    :param baudRate: 2400, 4800, 9600, 19200, 38400, 57600, 115200
    :param dataBits: 7, 8
    :param parityBit: None, Odd, Even
    :param stopBits: 1, 2
    :return:
    """
    baudRate = str(baudRate)
    dataBits = str(dataBits)
    stopBits = str(stopBits)
    telnetReturn = sendTelnet(ip, port, f'CSpara[{baudRate},{dataBits},{parityBit},{stopBits}]')
    return telnetReturn


def func_getEDIDM(ip, port, p_input):
    """
        Gets the current edid for the given input.

    :param ip:
    :param port:
    :param p_input: 1 ... 6
    :return:
    """
    p_input = str(p_input)
    telnetReturn = sendTelnet(ip, port, f'EDIDMSet{p_input} sta')
    return telnetReturn


def func_setEDIDM(ip, port, p_input, edid):
    """
        Assigns an EDID to the specified input. The EDID can be one of the internal pre-programmed EDID selections or a
        custom EDID that can be stored in one of ten memory locations. A brief description of each pre-programmed EDID
        is listed in the table below. To display the EDID assigned to an input, use the sta argument. Do not use a space
        between the command and the first parameter.

    :param ip:
    :param port:
    :param p_input: 1 ... 6
    :param edid: default, save1 ... save10, int1 ... int23, sta
    :return:
    """
    p_input = str(p_input)
    telnetReturn = sendTelnet(ip, port, f'EDIDMSet{p_input} {edid}')
    return telnetReturn


def func_saveEDIDOut(ip, port, output, memoryLocation):
    """
        Save the EDID of the display (sink) to the specified memory location.

    :param ip:
    :param port:
    :param output: 1 ... 8
    :param memoryLocation: save1 .. save10
    :return:
    """
    output = str(output)
    telnetReturn = sendTelnet(ip, port, f'EDIDOut{output} {memoryLocation}')
    return telnetReturn


def func_getHelp(ip, port, commandName=''):
    """
        Displays the list of available commands. To obtain help on a specific command, enter the help command followed
        by the name of the command.

    :param ip:
    :param port:
    :param commandName: Command
    :return:
    """
    telnetReturn = sendTelnet(ip, port, f'help {commandName}')
    return telnetReturn


def func_setHTTPPort(ip, port, httpPort):
    """
        Sets the HTTP listening port for the AT-UHD-PRO3-66M

    :param ip:
    :param port:
    :param httpPort: 0 ...65535
    :return:
    """
    httpPort = str(httpPort)
    telnetReturn = sendTelnet(ip, port, f'HTTPPort {httpPort}')
    return telnetReturn


def func_IPAddUser(ip, port, username, password):
    """
    Adds a user for web GUI login and Telnet sessions. This command performs the same function as adding a user
    within the web GUI. Refer to User Manual for more information.

    :param ip:
    :param port:
    :param username: 20 char max
    :param password: 20 char max
    :return:
    """
    telnetReturn = sendTelnet(ip, port, f'IPAddUser {username} {password}')
    return telnetReturn


def func_getIPCFG(ip, port):
    """
        Displays the current network settings for the AT-UHD-PRO3-66M.

    :param ip:
    :param port:
    :return:
    """
    telnetReturn = sendTelnet(ip, port, 'IPCFG')
    return telnetReturn


def func_IPChangePass(ip, port, username, oldPassword, newPassword):
    """
        Changes the password for the specified user.

    :param ip:
    :param port:
    :param username:
    :param oldPassword:
    :param newPassword:
    :return:
    """
    telnetReturn = sendTelnet(ip, port, f'IPChangePass {username} {oldPassword} {newPassword}')
    return telnetReturn


def func_IPDelUser(ip, port, username):
    """
        Deletes the specified user.
        Deleted users will no longer be able to access the web GUI or initiate Telnet sessions.
        This command performs the same function as removing a user within the web GUI. Refer to the User Manual for
        more information.

    :param ip:
    :param port:
    :param username:
    :return:
    """
    telnetReturn = sendTelnet(ip, port, f'IPDelUser {username}')
    return telnetReturn


def func_getIPDHCP(ip, port):
    """
        Gets the current dhcp mode.
        True = on
        False = off

    :param ip:
    :param port:
    :return: bool
    """
    telnetReturn = sendTelnet(ip, port, 'IPDHCP sta')
    if 'off' in telnetReturn:
        return False
    else:
        return True


def func_setIPDHCP(ip, port, value):
    """
        Enables or disables DHCP mode on the AT-UHD-PRO3-66M. on = DHCP mode ON; off = DHCP mode OFF; sta =
        displays the current setting. If this feature is disabled, then a static IP address must be specified.
        The default setting is DHCP = ON.

    :param ip:
    :param port:
    :param value: bool
    :return:
    """
    commandValue = 'on' if value else 'off'
    telnetReturn = sendTelnet(ip, port, f'IPDHCP {commandValue}')
    return telnetReturn


def func_getIPLogin(ip, port):
    """
        Gets the state of the use of login credentials for telnet.
        True = Enabled
        False = Disabled

    :param ip:
    :param port:
    :return: bool
    """
    telnetReturn = sendTelnet(ip, port, 'IPLogin sta')
    if 'off' in telnetReturn:
        return False
    else:
        return True


def func_setIPLogin(ip, port, value):
    """
        Enables or disables the use of login credentials when initiating a Telnet session on the AT-UHD-PRO3-66M.
        If this feature is set to on, then the AT-UHD-PRO3-66M will prompt for both the username and password.
        Use the same credentials as the web GUI. on = login credentials required; off = no login required.
        Use the sta argument to display the current setting. The default setting is on.
        True = on
        False = off

    :param ip:
    :param port:
    :param value: bool
    :return:
    """
    commandValue = 'on' if value else 'off'
    telnetReturn = sendTelnet(ip, port, f'IPLogin {commandValue}')
    return telnetReturn


def func_getIPPort(ip, port):
    """
        Gets the current ip port for telnet

    :param ip:
    :param port:
    :return: int
    """
    telnetReturn = sendTelnet(ip, port, 'IPPort sta')
    scrap, port = telnetReturn.split(' ')
    return int(port)


def func_setIPPort(ip, port, IPPort):
    """
        Sets the Telnet listening port for the AT-UHD-PRO3-66M.

    :param ip:
    :param port:
    :param IPPort: 0 ... 65535, sta
    :return:
    """
    IPPort = str(IPPort)
    telnetReturn = sendTelnet(ip, port, f'IPPort {IPPort}')
    return telnetReturn


def func_setIPStatic(ip, port, newIp, subnet, gateway):
    """
        Sets the static IP address, subnet mask, and gateway (router) address of the AT-UHD-PRO3-66M. Before using
        this command, DHCP must be disabled on the AT-UHD-PRO3-66M. Refer to the IPDHCP command for more
        information. Each argument must be entered in dot-decimal notation and separated by a space. The default static
        IP address of the AT-UHD-PRO3-66M is 192.168.1.254.

    :param ip:
    :param port:
    :param newIp:
    :param subnet:
    :param gateway:
    :return:
    """
    telnetReturn = sendTelnet(ip, port, f'IPStatic {newIp} {subnet} {gateway}')
    return telnetReturn


def func_setIRState(ip, port, state):
    """
        Enables or disables ir window on front panel.
        True = on
        False = off

    :param ip:
    :param port:
    :param state: bool
    :return:
    """
    telnetCommand = 'IRON' if state else 'IROFF'
    telnetReturn = sendTelnet(ip, port, telnetCommand)
    return telnetReturn


def func_setLockState(ip, port, state):
    """
        Locks or Unlocks buttons on front panel
        True = Locked
        False = Unlocked

    :param ip:
    :param port:
    :param state:
    :return:
    """
    telnetCommand = 'Lock' if state else 'Unlock'
    telnetReturn = sendTelnet(ip, port, telnetCommand)
    return telnetReturn


def func_MirrorHdmi(ip, port, hdmiOutput, videoOutput):
    """
        Enables or disables mirroring for the specified video output. Refer to the User Manual for more information on
        mirroring. Use the UnMirror command to disable output mirroring.

    :param ip:
    :param port:
    :param hdmiOutput: 6, 8
    :param videoOutput: Out1, ... Out5, Out7
    :return:
    """
    hdmiOutput = str(hdmiOutput)
    telnetReturn = sendTelnet(ip, port, f'MirrorHdmi{hdmiOutput} {videoOutput}')
    return telnetReturn


def func_MReset(ip, port):
    """
        Resets unit to factory default settings

    :param ip:
    :param port:
    :return:
    """
    telnetReturn = sendTelnet(ip, port, 'MReset')
    return telnetReturn


def func_setPowerState(ip, port, state):
    """
        Turns power on off
        True = on
        False = off

    :param ip:
    :param port:
    :param state: bool
    :return:
    """
    telnetCommand = 'PWON' if state else 'PWOFF'
    telnetReturn = sendTelnet(ip, port, telnetCommand)
    return telnetReturn


def func_getPowerState(ip, port):
    """
        Returns power status
        True = on
        False = off

    :param ip:
    :param port:
    :return: bool
    """
    telnetReturn = sendTelnet(ip, port, 'PWSTA')
    if 'PWOFF' in telnetReturn:
        return False
    else:
        return True


def func_recall(ip, port, preset):
    """
        Loads specified routing preset.

    :param ip:
    :param port:
    :param preset: 1 ... 50
    :return:
    """
    preset = str(preset)
    telnetReturn = sendTelnet(ip, port, f'Recall{preset}')
    return telnetReturn


def func_setRS232para(ip, port, baudRate, dataBits, parityBit, stopBits):
    """
        Sets the baud rate, data bits, parity bit, and stop bits for RS-232 over the HDBaseT (ZONE OUT) ports. Each
        argument must be separated by a comma; no spaces are permitted. Brackets must be included when typing this
        command. Use the sta argument, without brackets and including a space, to display the current settings.

    :param ip:
    :param port:
    :param baudRate: 2400, 9600, 19200, 38400, 56000, 57600, 115200
    :param dataBits: 7, 8
    :param parityBit: None, Odd, Even
    :param stopBits: 1, 2
    :return:
    """
    baudRate = str(baudRate)
    dataBits = str(dataBits)
    stopBits = str(stopBits)
    telnetReturn = sendTelnet(ip, port, f'RS232para[{baudRate},{dataBits},{parityBit},{stopBits}]')
    return telnetReturn


def func_RS232zone(ip, port, outputPort, Command):
    """
        Sends commands to the connected display. Refer to the User Manual of the display device for a list of available
        commands. Brackets must be used when specifying the command argument. The command line must not contain
        any spaces.

    :param ip:
    :param port:
    :param outputPort: 1 ... 5, 7
    :param Command: String
    :return:
    """
    outputPort = str(outputPort)
    telnetReturn = sendTelnet(ip, port, f'RS232zone[{outputPort}][{Command}]')
    return telnetReturn


def func_save(ip, port, preset):
    """
        Saves the current routing state to the specified preset.

    :param ip:
    :param port:
    :param preset: 1 ... 50
    :return:
    """
    preset = str(preset)
    telnetReturn = sendTelnet(ip, port, f'Save{preset}')
    return telnetReturn


def func_sddpAnnounce(ip, port):
    """
        Manually sends an ssdp announcement. this is used in conjunction with Control4 devices
    :param ip:
    :param port:
    :return:
    """
    telnetReturn = sendTelnet(ip, port, 'sddp_announce')
    return telnetReturn


def func_setHostName(ip, port, hostname):
    """
        Sets the host name. This command is used in conjunction with the SDDP protocol. No spaces are permitted in the
        host name.

    :param ip:
    :param port:
    :param hostname:
    :return:
    """
    telnetReturn = sendTelnet(ip, port, f'set_host_name {hostname}')
    return telnetReturn


def func_getHostName(ip, port):
    """
        Displays the host name.

    :param ip:
    :param port:
    :return:
    """
    telnetReturn = sendTelnet(ip, port, 'show_host_name')
    return telnetReturn


def func_status(ip, port):
    """
        Displays the current routing status for each output
    :param ip:
    :param port:
    :return:
    """
    telnetReturn = sendTelnet(ip, port, 'Status')
    return telnetReturn


def func_statusOutput(ip, port, output):
    """
        Displays the current routing status for specified output
    :param ip:
    :param port:
    :param output: 1 ... 10
    :return:
    """
    output = str(output)
    telnetReturn = sendTelnet(ip, port, f'Statusx{output}')
    return telnetReturn


def func_getSyslock(ip, port):
    """
        Gets the state of ssh.
        True = Enabled
        False = Disabled

    :param ip:
    :param port:
    :return: bool
    """
    telnetReturn = sendTelnet(ip, port, 'syslock sta')
    if 'off' in telnetReturn:
        return False
    else:
        return True


def func_setSyslock(ip, port, state):
    """
        Enables or disables SSH. When enabled, this command shuts down the web server and closes all ports, except for
        SSH (TCP 22). Note that local RS-232 master port control will still be available.
        Use the sta argument to display the current state.
        True = on
        False = off

    :param ip:
    :param port:
    :param state: bool
    :return:
    """
    commandValue = 'on' if state else 'off'
    telnetReturn = sendTelnet(ip, port, f'syslock {commandValue}')
    return telnetReturn


def func_type(ip, port, full):
    """
        Displays the model information of the AT-UHD-PRO3-66M. The full argument may be specified to display the host
        name and firmware version. This argument is optional.

    :param ip:
    :param port:
    :param full: bool
    :return:
    """
    commandValue = 'full' if full else ''
    telnetReturn = sendTelnet(ip, port, f'Type {commandValue}')
    return telnetReturn


def func_unMirror(ip, port, hdmiOutput):
    """
        Disables mirroring on the specified HDMI output port.

    :param ip:
    :param port:
    :param hdmiOutput: 6, 8
    :return:
    """
    hdmiOutput = str(hdmiOutput)
    telnetReturn = sendTelnet(ip, port, f'UnMirror{hdmiOutput}')
    return telnetReturn


def func_version(ip, port):
    """
        Displays the current version of firmware.

    :param ip:
    :param port:
    :return:
    """
    telnetReturn = sendTelnet(ip, port, 'Version')
    return telnetReturn


def func_vOut(ip, port, output, value):
    """
        Sets the output channel volume, in decibels. Values for parameter Y can be specified numerically or can be
        incremental/decremental using the + or - character.

    :param ip:
    :param port:
    :param output: 1 ... 5, 7
    :param value: -79 ... 15, +, -
    :return:
    """
    output = str(output)
    value = str(value)
    telnetReturn = sendTelnet(ip, port, f'VOUT{output} {value}')
    return telnetReturn


def func_getVOutMute(ip, port, zone):
    """
        Gets the current muting state for the given zone
        True = on muted
        False = off Unmuted

    :param ip:
    :param port:
    :param zone: 1 ... 5, 7
    :return: bool
    """
    zone = str(zone)
    telnetReturn = sendTelnet(ip, port, f'VOUTMute{zone} sta')
    if 'off' in telnetReturn:
        return False
    else:
        return True


def func_setVOutMute(ip, port, zone, state):
    """
        Controls volume muting for the specified audio channel (zone).
        Use the sta argument to display the current muting state for the specified zone.
        True = on
        False = off

    :param ip:
    :param port:
    :param zone: 1 ... 5, 7
    :param state: bool
    :return:
    """
    zone = str(zone)
    commandValue = 'on' if state else 'off'
    telnetReturn = sendTelnet(ip, port, f'VOUTMute{zone} {commandValue}')
    return telnetReturn


def func_setOutputState(ip, port, output, state):
    """
        Enables or disables the specified output channel.
        True = enable
        False = disable

    :param ip:
    :param port:
    :param output:  1 ... 5, 7
    :param state: bool
    :return:
    """
    output = str(output)
    commandValue = 'on' if state else 'off'
    telnetReturn = sendTelnet(ip, port, f'x{output}$ {commandValue}')
    return telnetReturn


def func_getOutputState(ip, port, output):
    """
        Gets the current output state:
        True = Enabled
        False = Disabled

    :param ip:
    :param port:
    :param output: 1 ... 5, 7
    :return: bool
    """
    output = str(output)
    telnetReturn = sendTelnet(ip, port, f'x{output}$ sta')
    if 'off' in telnetReturn:
        return False
    else:
        return True


def func_routeInput(ip, port, p_input, p_output=None):
    """
        Routes the specified input to all outputs.
        if p_input is None then input will be routed to all outputs

    :param ip:
    :param port:
    :param p_input: 1 ... 6
    :param p_output: 1 ... 5, 7
    :return:
    """
    p_input = str(p_input)
    p_output = str(p_output)
    telnetReturn = sendTelnet(ip, port, f'x{p_input}AVx{p_output}')
    return telnetReturn
