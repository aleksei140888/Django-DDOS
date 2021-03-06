# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect

from Scripts.HTTP.httpFlood import HTTPFlood
from Scripts.TCP.tcpFlood import TCPFlood
from Scripts.UDP.udpFlood import UDPFlood
from Scripts.DNS.dnsFLood import DNSFlood
from Scripts.ICMP.icmpFlood import ICMPFlood

from Scripts.PDF.createPDF import CreatePDF
from Scripts.LIVE.isAlive import isAlive
from Scripts.RESOLVE.DomainResolve import Resolve



def redirect(request):
    return HttpResponseRedirect("index")

def index(request):
    return render( request , "index.html" , {})

def Http_Flood(request):
    if request.method == "POST":
        dst     = request.POST["dst"]
        dport    = 80
        flag    = "S"
        method = request.POST["method"]
        count   = request.POST["count"]

        if "com" in dst:
            tmp = Resolve(dst)
            dst = tmp.Get()

        attack = HTTPFlood(dst,dport,flag,method,count)
        attack.ThreadStart()

        gecici = isAlive(dst, dport)
        CreatePDF("HTTP {}".format(method), gecici)

        return render(request, "Http_Flood.html", {})
    elif request.method == "GET":
        return render(request, "Http_Flood.html", {})

def Tcp_Flood(request):
    if request.method == "POST":
        dst = request.POST["dst"]
        dport = request.POST["dport"]
        flag = request.POST["flag"]
        count = request.POST["count"]

        if "com" in dst:
            tmp = Resolve(dst)
            dst = tmp.Get()

        tmp = TCPFlood(dst,dport,flag,count)
        tmp.ThreadStart()

        gecici = isAlive(dst,dport)
        CreatePDF("TCP Flood",gecici)

        return render(request,"Tcp_Flood.html" , {})
    elif request.method == "GET":
        return render(request,"Tcp_Flood.html" , {})

def Udp_Flood(request):
    if request.method == "POST":
        dst = request.POST["dst"]
        dport = request.POST["dport"]
        count = request.POST["count"]

        if "com" in dst:
            tmp = Resolve(dst)
            dst = tmp.Get()

        tmp = UDPFlood(dst,dport,count)
        tmp.ThreadStart()

        gecici = isAlive(dst,dport)
        CreatePDF("UDP Flood",gecici)

        return render(request, "Udp_Flood.html", {})

    if request.method == "GET":
        return render(request, "Udp_Flood.html", {})

def Icmp_Flood(request):
    if request.method == "POST":
        dst   = request.POST["dst"]
        count = request.POST["count"]

        if "com" in dst:
            tmp = Resolve(dst)
            dst = tmp.Get()


        icmp = ICMPFlood(dst,count)
        icmp.ThreadStart()

        gecici = isAlive(dst, "ICMP")
        CreatePDF("ICMP Flood", gecici)

        return render(request,"Icmp_Flood.html")
    elif request.method == "GET":
        return render(request, "Icmp_Flood.html")

def Dns_Flood(request):
    if request.method == "POST":
        dst     = request.POST["dst"]
        qname   = request.POST["qname"]
        qtype   = request.POST["qtype"]
        count   = request.POST["count"]

        dns = DNSFlood(dst,qname,qtype,count)
        dns.ThreadStart()

        return render(request,"Dns_Flood.html")
    elif request.method == "GET":
        return render(request,"Dns_Flood.html")

