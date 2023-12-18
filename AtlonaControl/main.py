from atlonaControl import atlonaControl


if __name__ == '__main__':
    atlona = atlonaControl("10.74.12.157")
    blink = atlona.getBlink()
    broadcast = atlona.getBroadcast()
    # EDIDM = atlona.getEDIDM(3)
    getHelp = atlona.getHelp()
    IPCFG = atlona.getIPCFG()
    IPDHCP = atlona.getIPDHCP()
    IPLogin = atlona.getIPLogin()
    # TelnetPort = atlona.getTelnetPort()
    PowerState = atlona.getPowerState()
    Status = atlona.getStatus()
    Syslock = atlona.getSyslock()
    Type = atlona.getType(True)
    Version = atlona.getVersion()
    VOUTMute = atlona.getVOutMute(3)
    Output3State = atlona.getOutputState(3)
