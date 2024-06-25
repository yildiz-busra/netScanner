import scapy.all as scapy
import optparse

def getUserInput():
    parseObject = optparse.OptionParser()
    parseObject.add_option("-t", "--target", dest="ipAddress", help="target IP address to scan")
    return parseObject.parse_args()

def scanNetwork(ipAddress):

    arpRequestPacket = scapy.ARP(pdst=ipAddress)
    broadcastPacket = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined = arpRequestPacket/broadcastPacket
    (answered, unanswered) = scapy.srp(combined, timeout=1)
    answered.summary()

(userInput, arguments) = getUserInput()
if not userInput:
    print("Enter IP address")
scanNetwork(userInput.ipAddress)

