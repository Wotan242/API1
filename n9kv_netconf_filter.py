#!/usr/bin/env python3

from ncclient import manager
import credentials
from lxml import etree


def main():
    with manager.connect(host='10.10.201.91',
                         port=830,
                         username=credentials.user,
                         password=credentials.password,
                         hostkey_verify=False,
                         device_params={'name': 'nexus'},
                         allow_agent=False,
                         look_for_keys=False
                         ) as cisco_manager:

        int_name_filter = '''
        <interfaces xmlns="http://openconfig.net/yang/interfaces">
            <interface>
              <name>po12</name>
              <config>
                <enabled>
                 false
                </enabled>
                </config>
             </interface>
        </interfaces>
        '''

        int_names = cisco_manager.get(('subtree', int_name_filter))

        print(type(int_names))
        print('*' * 30)

        # print(etree.tostring(int_names.data))
        print(int_names)

if __name__ == '__main__':
    main()
