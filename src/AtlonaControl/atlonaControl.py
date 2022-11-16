import re

from apiFunctions import *


class atlonaControl:
    
    def __init__(self, ip, port=23):
        self.ip = ip
        self.port = port
        self.hostname = self.getHostName()

    def decodeTypeString(self):
        typeString = self.getType(True)
        return typeString

    # API Functions
    def resetAll(self):
        func_resetAll(self.ip, self.port)
        
    def getBlink(self):
        funcReturn = func_getBlink(self.ip, self.port)
        return funcReturn
    
    def setBlink(self, value):
        func_setBlink(self.ip, self.port, value)
        
    def getBroadcast(self):
        funcReturn = func_getBroadcast(self.ip, self.port)
        return funcReturn
    
    def setBroadcast(self, value):
        func_setBroadcast(self.ip, self.port, value)
        
    def clearPreset(self, preset):
        func_clearPreset(self.ip, self.port, preset)
        
    def setCSpara(self, baudRate, dataBits, parityBit, stopBits):
        func_setCSpara(self.ip, self.port, baudRate, dataBits, parityBit, stopBits)
        
    def getEDIDM(self, p_input):
        """
            Not working, getting command failed from matrix.

        :param p_input:
        :return:
        """
        funcReturn = func_getEDIDM(self.ip, self.port, p_input)
        return funcReturn
    
    def setEDIDM(self, p_input, edid):
        func_setEDIDM(self.ip, self.port, p_input, edid)

    def saveEDIDOut(self, output, memoryLocation):
        func_saveEDIDOut(self.ip, self.port, output, memoryLocation)
        
    def getHelp(self, commandName=''):
        funcReturn = func_getHelp(self.ip, self.port, commandName)
        return funcReturn
    
    def setHTTPPort(self, port):
        func_setHTTPPort(self.ip, self.port, port)
        
    def addUser(self, username, password):
        func_IPAddUser(self.ip, self.port, username, password)
        
    def delUser(self, username):
        func_IPDelUser(self.ip, self.port, username)
        
    def getIPCFG(self):
        funcReturn = func_getIPCFG(self.ip, self.port)
        return funcReturn
        
    def changePass(self, username, oldPassword, newPassword):
        func_IPChangePass(self.ip, self.port, username, oldPassword, newPassword)
        
    def getIPDHCP(self):
        funcReturn = func_getIPDHCP(self.ip, self.port)
        return funcReturn
    
    def setIPDHCP(self, value):
        func_setIPDHCP(self.ip, self.port, value)
        
    def getIPLogin(self):
        funcReturn = func_getIPLogin(self.ip, self.port)
        return funcReturn
    
    def setIPLogin(self, value):
        func_setIPLogin(self.ip, self.port, value)
        
    def getTelnetPort(self):
        """
            Not working for some reason
        :return:
        """
        funcReturn = func_getIPPort(self.ip, self.port)
        return funcReturn
    
    def setTelnetPort(self, port):
        func_setIPPort(self.ip, self.port, port)
        
    def setIPStatic(self, newIP, subnet, gateway):
        func_setIPStatic(self.ip, self.port, newIP, subnet, gateway)
        
    def setIRState(self, state):
        func_setIRState(self.ip, self.port, state)
        
    def setLockState(self, state):
        func_setLockState(self.ip, self.port, state)
        
    def mirrorHdmi(self, hdmiOutput, videoOutput):
        func_MirrorHdmi(self.ip, self.port, hdmiOutput, videoOutput)
        
    def mReset(self):
        func_MReset(self.ip, self.port)
        
    def setPowerState(self, state):
        func_setPowerState(self.ip, self.port, state)
        
    def getPowerState(self):
        funcReturn = func_getPowerState(self.ip, self.port)
        return funcReturn
    
    def recallPreset(self, preset):
        func_recall(self.ip, self.port, preset)
        
    def setRS232para(self, baudRate, dataBits, parityBit, stopBits):
        func_setRS232para(self.ip, self.port, baudRate, dataBits, parityBit, stopBits)
        
    def RS232zone(self, outputPort, Command):
        func_RS232zone(self.ip, self.port, outputPort, Command)
        
    def savePreset(self, preset):
        func_save(self.ip, self.port, preset)
        
    def sddpAnnounce(self):
        func_sddpAnnounce(self.ip, self.port)
        
    def setHostName(self, hostname):
        func_setHostName(self.ip, self.port, hostname)
        self.hostname = hostname
        
    def getHostName(self):
        funcReturn = func_getHostName(self.ip, self.port)
        regexEx = r":  (.*)\r"
        matched = re.findall(regexEx, funcReturn)
        return matched[0]
    
    def getStatus(self):
        funcReturn = func_status(self.ip, self.port)
        return funcReturn
    
    def statusOutput(self, output):
        funcReturn = func_statusOutput(self.ip, self.port, output)
        return funcReturn
    
    def getSyslock(self):
        funcReturn = func_getSyslock(self.ip, self.port)
        return funcReturn
    
    def setSyslock(self, state):
        func_setSyslock(self.ip, self.port, state)
        
    def getType(self, full):
        funcReturn = func_type(self.ip, self.port, full)
        return funcReturn
    
    def unMirror(self, hdmiOutput):
        func_unMirror(self.ip, self.port, hdmiOutput)
        
    def getVersion(self):
        funcReturn = func_version(self.ip, self.port)
        return funcReturn
    
    def setVOut(self, output, value):
        func_vOut(self.ip, self.port, output, value)
        
    def getVOutMute(self, zone):
        funcReturn = func_getVOutMute(self.ip, self.port, zone)
        return funcReturn
    
    def setVOutMute(self, zone, state):
        func_setVOutMute(self.ip, self.port, zone, state)
        
    def setOutputState(self, output, state):
        func_setOutputState(self.ip, self.port, output, state)
        
    def getOutputState(self, output):
        func_getOutputState(self.ip, self.port, output)
        
    def routeInput(self, p_input, p_output=None):
        func_routeInput(self.ip, self.port, p_input, p_output)
        