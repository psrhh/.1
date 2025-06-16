local shortport = require "shortport"

description = [[
Simple script to detect HTTP services on open ports.
]]

author = "Name"
license = "Same as Nmap--See https://nmap.org/book/man-legal.html"
categories = {"safe", "discovery"}

portrule = shortport.http

action = function(host, port)
    return "HTTP detected on port " .. port.number
end

