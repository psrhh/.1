portrule = function(host, port)
  return port.protocol == "tcp" and port.number == 80
end

action = function(host, port)
  return "HTTP server detected on " .. host.ip
end