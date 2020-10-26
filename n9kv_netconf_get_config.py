#!/usr/bin/env python3

from ncclient import manager
import credentials
from lxml import etree
from ncclient.operations.rpc import RPCError


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

        oc_int1 = '''
        <interfaces xmlns="http://openconfig.net/yang/interfaces">
            <interface>
              <name>eth1/13</name>
              
            </interface>
        </interfaces>
        '''

        oc_int2 = '''
         <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
              <name>eth1/16</name>
              <type xmlns="urn:ietf:params:xml:ns:yang:iana-if-type"/>
             </interface>
        </interfaces>
        '''



        oc_bgp = '''
        <bgp xmlns="http://openconfig.net/yang/bgp">
            <global/>
        </bgp>
        '''

        oc_local_route = '''
        <local-routes xmlns="http://openconfig.net/yang/local-routing"/>
        '''

        try:
            oc_resp = cisco_manager.get_config('running',
                                               filter=('subtree', oc_int1))
            print(oc_resp)
            print('*' * 30)
        except RPCError as err:
            for attr in dir(err):
                print(attr, ':   ', getattr(err, attr))


if __name__ == '__main__':
    main()
