#!/usr/bin/env python
import libxml2
import sys

def getServers(xml):
    doc = libxml2.parseFile(xml)
    ctxt = doc.xpathNewContext()
    servers = ctxt.xpathEval("//FileZilla3/Servers/Server")

    print servers;

    for server in servers:
        host = server.xpathEval('Host')[0].content;
        port = server.xpathEval('Port')[0].content;
        user = server.xpathEval('User')[0].content;
        password = server.xpathEval('Pass')[0].content;

        #print password;
        
    doc.freeDoc()
    ctxt.xpathFreeContext()
 
sys.argv = ['generator.py', '/home/mtdavidson/.filezilla/sitemanager.xml'];

sitemanagerFile = sys.argv[1];

if __name__ == "__main__":
    getServers(sitemanagerFile)
