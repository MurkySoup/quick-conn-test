#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Quick Connection Tester, Version 0.3-BETA (Do Not Distribute)
By Rick Pelletier (rpelletier@gannett.com), 30 September 2022

Note: limited error trapping.
"""


import sys
import socket
import argparse


def conn_test(target_host:str, target_port:int, timeout:int = 30):
  output = 'Connection successful'
  exit_val = 0

  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(timeout)
      s.connect((target_host, target_port))
      s.close
  except socket.error as msg:
    output = str(msg)
    exit_val = 1

  return output, exit_val


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-a', '--host', type=str, required=True, help='Host or IP address to test')
  parser.add_argument('-p', '--port', type=int, required=True, help='Port number to test')
  parser.add_argument('-t', '--timeout', type=int, required=False, help='Set timeout in seconds')
  args = parser.parse_args()

  if args.timeout:
    message, exit_val = conn_test(args.host, args.port, args.timeout)
  else:
    message, exit_val = conn_test(args.host, args.port)

  if exit_val == 0:
    print(message, file = sys.stdout)
  else:
    print(message, file = sys.stderr)

  sys.exit(exit_val)
else:
  sys.exit(1)

# end of script

