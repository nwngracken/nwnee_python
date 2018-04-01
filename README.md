# nwnee_python
python libraries for interfacing with Neverwinter Nights Extended Edition (NWNEE) servers

The functions in this "library" were created and tested under Python 3.5.2

# EXAMPLE

```python
#!/usr/bin/python3
from proto import *

def main():
  print('======== send_bnes_recv_bner() ========')
  for lhs, rhs in send_bnes_recv_bner(
    'nwnserver.com', 5121
  ).items():
    print("%-22s => %s" % (
      lhs,
      rhs.decode("utf-8")
      if isinstance(rhs, bytes)
      else str(rhs)
    )
  )
  print('')

  print('======== send_bnds_recv_bndr() ========')
  for lhs, rhs in send_bnds_recv_bndr(
    'nwnserver.com', 5121
  ).items():
    print("%-22s => %s" % (
      lhs,
      rhs.decode("utf-8")
      if isinstance(rhs, bytes)
      else str(rhs)
    )
  )
  print('')

  print('======== send_bnxi_recv_bnxr() ========')
  for lhs, rhs in send_bnxi_recv_bnxr(
    'nwnserver.com', 5121
  ).items():
    print("%-22s => %s" % (
      lhs,
      rhs.decode("utf-8")
      if isinstance(rhs, bytes)
      else str(rhs)
    )
  )

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
```

Output:
```

======== send_bnes_recv_bner() ========
enumType               => 0
header                 => BNER
port                   => 5121
protocol               => 85
sessionName            => "My dick-kicking NWN server"
sessionNameSize        => 7

======== send_bnds_recv_bndr() ========
header                 => BNDR
port                   => 5121
gameType               => 10
serverDescription      => 
serverDescriptionSize  => 0
moduleDescriptionSize  => 185
moduleDescription      => http://nwnserver.com
nwnserver@gmail.com
IRC    : irc.freenode.net #nwnserver
discord: https://discord.gg/6969696 

This is a really great server!
serverVersion          => 8166
serverVersionSize      => 4

======== send_bnxi_recv_bnxr() ========
bnxiVersionNumber      => 253
hasPassword            => 0
currentPlayers         => 23
vaultMode              => 0
minLevel               => 1
moduleNameSize         => 3
playerPause            => 0
pvp                    => 2
elc                    => 0
header                 => BNXR
ilr                    => 0
port                   => 5121
oneParty               => 0
moduleName             => DKS
maxPlayers             => 96
maxLevel               => 20
xp                     => 0
```
