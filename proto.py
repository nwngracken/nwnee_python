# Unsupported messages:
# BNDM - "Disconnect Me" 
# BNDP - "Disconnect Player"

import socket
from   struct import *
import sys

def send_bnes_recv_bner(
  ip_address,
  port,
  timeout_int = 2,
  recv_int    = 1476
):
  bner_dict = dict()

  # Data structure borrowed from
  # https://github.com/niv/neverwinter_utils.nim/blob/master/src/packets.nim 
  # commit 8374044cdc3e32b0a31b3c5a4dd4b784be947326
  # BNES* = object
  #   header: StaticValue["BNES"]
  #   port: uint16
  #   enumType: uint8

  bnes_bstr = pack(
    # <  little endian
    # 4s string of length 4
    # H  unsigned short
    # B  unsigned char
    '<4sHB',
    # header
    b'BNES',
    # port
    0x0000,
    # enumType
    0x00
  )

  nwnee_socket = socket.socket(
    socket.AF_INET, socket.SOCK_DGRAM
  )
  nwnee_socket.settimeout(timeout_int)

  nwnee_socket.sendto(bnes_bstr, (ip_address, port))
  try:
    bner_bstr, sender_address = nwnee_socket.recvfrom(recv_int)
  except socket.timeout:
    bner_dict = {
      error: 'Timeout ' + str(timeout_int) + ' expired ' + \
        'waiting for a response'
    }
    nwnee_socket.close()
    return bner_dict

  nwnee_socket.close()

  # Data structure borrowed from
  # https://github.com/niv/neverwinter_utils.nim/blob/master/src/packets.nim 
  # commit 8374044cdc3e32b0a31b3c5a4dd4b784be947326
  # BNER* = object
  #   header: StaticValue["BNER"]
  #   protocol: uint8
  #   port: uint16
  #   enumType: uint8
  #   sessionName: SizePrefixedString[uint8]

  # <  little endian
  # 4s string of length 4
  # B  unsigned char
  # H  unsigned short
  # B  unsigned char
  # B  unsigned char
  bfmt = '<4sBHBB'

  offset = 0
  size   = calcsize(bfmt)

  bner_dict['header'],                   \
  bner_dict['protocol'],                 \
  bner_dict['port'],                     \
  bner_dict['enumType'],                 \
  bner_dict['sessionNameSize'] = unpack(
    bfmt,
    bner_bstr[offset:offset + size]
  )

  offset = offset = size
  size   = bner_dict['sessionNameSize']

  bner_dict['sessionName'] = bner_bstr[offset:offset + size]

  return bner_dict

def send_bnlm_recv_bnlr(
  ip_address,
  port,
  timeout_int = 2,
  recv_int    = 1476
):
  bnlr_dict = dict()

  # Data structure borrowed from
  # https://github.com/niv/neverwinter_utils.nim/blob/master/src/packets.nim 
  # commit 8374044cdc3e32b0a31b3c5a4dd4b784be947326
  # BNLM* = object
  #   header: StaticValue["BNLM"]
  #   port: uint16
  #   messageNo: uint8
  #   sessionId: uint32

  bnlm_bstr = pack(
    # <  little endian
    # 4s string of length 4
    # H  unsigned short
    # B  unsigned char
    '<4sHBL',
    # header
    b'BNLM',
    # port
    0x0000,
    # messagNo
    0x01,
    # sessionId
    0x00000000
  )

  nwnee_socket = socket.socket(
    socket.AF_INET, socket.SOCK_DGRAM
  )
  nwnee_socket.settimeout(timeout_int)

  nwnee_socket.sendto(bnlm_bstr, (ip_address, port))
  try:
    bnlr_bstr, sender_address = nwnee_socket.recvfrom(recv_int)
  except socket.timeout:
    bnlr_dict = {
      error: 'Timeout ' + str(timeout_int) + ' expired ' + \
        'waiting for a response'
    }
    nwnee_socket.close()
    return bnlr_dict

  nwnee_socket.close()

  # Data structure borrowed from
  # https://github.com/niv/neverwinter_utils.nim/blob/master/src/packets.nim 
  # commit 8374044cdc3e32b0a31b3c5a4dd4b784be947326
  # BNLR* = object
  #   header: StaticValue["BNLR"]
  #   port: uint16
  #   messageNo: uint8
  #   sessionId: uint32

  # <  little endian
  # 4s string of length 4
  # H  unsigned short
  # B  unsigned char
  # B  unsigned long
  bfmt = '<4sHBL'

  offset = 0
  size   = calcsize(bfmt)

  bnlr_dict['header'],             \
  bnlr_dict['port'],               \
  bnlr_dict['messageNo'],          \
  bnlr_dict['sessionId'] = unpack(
    bfmt,
    bnlr_bstr
  )

  return bnlr_dict

def send_bnds_recv_bndr(
  ip_address,
  port,
  timeout_int = 2,
  recv_int    = 1476
):
  bndr_dict = dict()

  # Data structure borrowed from
  # https://github.com/niv/neverwinter_utils.nim/blob/master/src/packets.nim 
  # commit 8374044cdc3e32b0a31b3c5a4dd4b784be947326
  # BNDS* = object
  #   header: StaticValue["BNDS"]
  #   port: uint16

  bnds_bstr = pack(
    # <  little endian
    # 4s string of length 4
    # H  unsigned short
    '<4sH',
    # header
    b'BNDS',
    # port
    0x0000
  )

  nwnee_socket = socket.socket(
    socket.AF_INET, socket.SOCK_DGRAM
  )
  nwnee_socket.settimeout(timeout_int)

  nwnee_socket.sendto(bnds_bstr, (ip_address, port))
  try:
    bndr_bstr, sender_address = nwnee_socket.recvfrom(recv_int)
  except socket.timeout:
    bndr_dict = {
      error: 'Timeout ' + str(timeout_int) + ' expired ' + \
        'waiting for a response'
    }
    nwnee_socket.close()
    return bndr_dict

  nwnee_socket.close()

  # Data structure borrowed from
  # https://github.com/niv/neverwinter_utils.nim/blob/master/src/packets.nim 
  # commit 8374044cdc3e32b0a31b3c5a4dd4b784be947326
  # BNDR* = object
  #   header: StaticValue["BNDR"]
  #   port: uint16
  #   serverDescription: SizePrefixedString[uint32]
  #   moduleDescription: SizePrefixedString[uint32]
  #   serverVersion: SizePrefixedString[uint32]
  #   gameType: uint16

  # <  little endian
  # 4s string of length 4
  # H  unsigned short
  # L  unsigned long
  bfmt = '<4sHL'

  offset = 0
  size   = calcsize(bfmt)

  bndr_dict['header'],                          \
  bndr_dict['port'],                            \
  bndr_dict['serverDescriptionSize'] = unpack (
    bfmt,
    bndr_bstr[offset:offset + size]
  )

  offset = offset + size
  size   = bndr_dict['serverDescriptionSize']

  bndr_dict['serverDescription'] = \
    bndr_bstr[offset:offset + size]

  # < little endian
  # L unsigned long
  bfmt = '<L'

  offset = offset + size
  size   = calcsize(bfmt)

  bndr_dict['moduleDescriptionSize'], = unpack(
    bfmt,
    bndr_bstr[offset:offset + size]
  )

  offset = offset + size
  size   = bndr_dict['moduleDescriptionSize']

  bndr_dict['moduleDescription'] = \
    bndr_bstr[offset:offset + size]

  # < little endian
  # L unsigned long
  bfmt = '<L'

  offset = offset + size
  size   = calcsize(bfmt)

  bndr_dict['serverVersionSize'], = unpack(
    bfmt,
    bndr_bstr[offset:offset + size]
  )

  offset = offset + size
  size   = bndr_dict['serverVersionSize']

  bndr_dict['serverVersion'] = \
    bndr_bstr[offset:offset + size]

  # < little endian
  # H unsigned short
  bfmt = '<H'

  offset = offset + size
  size   = calcsize(bfmt)

  bndr_dict['gameType'], = unpack(
    bfmt,
    bndr_bstr[offset:offset + size]
  )

  return bndr_dict

def send_bnxi_recv_bnxr(
  ip_address,
  port,
  timeout_int = 2,
  recv_int    = 1476
):
  bnxr_dict = dict()

  # Data structure borrowed from
  # https://github.com/niv/neverwinter_utils.nim/blob/master/src/packets.nim 
  # commit 8374044cdc3e32b0a31b3c5a4dd4b784be947326
  # BNXI* = object
  #   header: StaticValue["BNXI"]
  #   port: uint16

  bnxi_bstr = pack(
    # <  little endian
    # 4s string of length 4
    # H  unsigned short
    '<4sH',
    # header
    b'BNXI',
    # port
    0x0000
  )

  nwnee_socket = socket.socket(
    socket.AF_INET, socket.SOCK_DGRAM
  )
  nwnee_socket.settimeout(timeout_int)

  nwnee_socket.sendto(bnxi_bstr, (ip_address, port))
  try:
    bnxr_bstr, sender_address = nwnee_socket.recvfrom(recv_int)
  except socket.timeout:
    bnxr_dict = {
      error: 'Timeout ' + str(timeout_int) + ' expired ' + \
        'waiting for a response'
    }
    nwnee_socket.close()
    return bnxr_dict

  nwnee_socket.close()

  # Data structure borrowed from
  # https://github.com/niv/neverwinter_utils.nim/blob/master/src/packets.nim 
  # commit 8374044cdc3e32b0a31b3c5a4dd4b784be947326
  # BNXR* = object
  #   header: StaticValue["BNXR"]
  #   port: uint16
  #   bnxiVersionNumber: uint8
  #   hasPassword: uint8
  #   minLevel: uint8
  #   maxLevel: uint8
  #   currentPlayers: uint8
  #   maxPlayers: uint8
  #   vaultMode: uint8
  #   pvp: uint8
  #   playerPause: uint8
  #   oneParty: uint8
  #   elc: uint8
  #   ilr: uint8
  #   xp: uint8
  #   moduleName: SizePrefixedString[uint8]


  # <  little endian
  # 4s string of length 4
  # H  unsigned short
  # B  unsigned char
  # B  unsigned char
  # B  unsigned char
  # B  unsigned char
  # B  unsigned char
  # B  unsigned char
  # B  unsigned char
  # B  unsigned char
  # B  unsigned char
  # B  unsigned char
  # B  unsigned char
  # B  unsigned char
  # B  unsigned char
  # B  unsigned char
  bfmt = '<4sHBBBBBBBBBBBBBB'

  offset = 0
  size   = calcsize(bfmt)

  bnxr_dict['header'],                  \
  bnxr_dict['port'],                    \
  bnxr_dict['bnxiVersionNumber'],       \
  bnxr_dict['hasPassword'],             \
  bnxr_dict['minLevel'],                \
  bnxr_dict['maxLevel'],                \
  bnxr_dict['currentPlayers'],          \
  bnxr_dict['maxPlayers'],              \
  bnxr_dict['vaultMode'],               \
  bnxr_dict['pvp'],                     \
  bnxr_dict['playerPause'],             \
  bnxr_dict['oneParty'],                \
  bnxr_dict['elc'],                     \
  bnxr_dict['ilr'],                     \
  bnxr_dict['xp'],                      \
  bnxr_dict['moduleNameSize'] = unpack(
    bfmt,
    bnxr_bstr[offset:offset + size]
  )

  offset = offset = size
  size   = bnxr_dict['moduleNameSize']

  bnxr_dict['moduleName'] = bnxr_bstr[offset:offset + size]

  return bnxr_dict
