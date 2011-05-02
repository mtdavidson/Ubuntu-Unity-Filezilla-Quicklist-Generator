#!/usr/bin/env python
import libxml2
import sys

def getServers(xml):
    doc = libxml2.parseFile(xml)
    ctxt = doc.xpathNewContext()
    servers = ctxt.xpathEval("//FileZilla3/Servers/Server")

    print servers;

    for server in servers:
        host = server.xpathEval('Host')[0].content
        port = server.xpathEval('Port')[0].content
        user = server.xpathEval('User')[0].content
        password = server.xpathEval('Pass')[0].content

    doc.freeDoc()
    ctxt.xpathFreeContext()
 
sys.argv = ['generator.py', '/home/mtdavidson/.filezilla/sitemanager.xml'];

if len(sys.argv) != 2:
    sys.exit('Incorrect Number of Arguments');

if not os.path.exists(sys.argv[1]):
    #TODO: Check is file
    #TODO: Check is XML file
    sys.exit('Invalid file specified');

sitemanagerFile = sys.argv[2];
    
if __name__ == "__main__":
    getServers(sitemanagerFile)
