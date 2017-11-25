#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
from pprint import pprint

OUTPUT_FILE = 'thiago_data2.json'


def main():
  domain = raw_input('Domain: ')
  tipe = raw_input('Type: ')
  tipe_2 = raw_input('2nd type: ')
  tipe_3 = raw_input('3nd type: ')
  things = raw_input('Source Notes (things to know?) : ')
  
  domain = unicode(domain, 'utf-8')
  tipe = unicode(tipe, 'utf-8')
  tipe_2 = unicode(tipe_2, 'utf-8')
  tipe_3 = unicode(tipe_3, 'utf-8')
  things = unicode(things, 'utf-8')
  
  
  data = json.load(open(OUTPUT_FILE))
  data[domain] = {u'type': tipe, u'2nd type': tipe_2, u'3rd type': tipe_3, u'Source Notes (things to know?)': things}
  
  with open(OUTPUT_FILE, 'w') as outfile:
    outfile.write(json.dumps(data, indent=2, sort_keys=True))
  


if __name__ == '__main__':
  main()
