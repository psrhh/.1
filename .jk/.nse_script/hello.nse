description = [[
A beginner-friendly NSE script that simply returns a test message.
Useful for learning NSE scripting basics.
]]

author = "Name"
license = "Same as Nmap -- See https://nmap.org/book/man-legal.html"
categories = {"discovery", "safe"}

-- Runs on all ports
portrule = function() return true end

-- Action to be performed when the script runs
action = function(host, port)
  return "Hello from NSE!"
end
