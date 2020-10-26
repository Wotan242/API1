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

        

        descr_cfg1 = '''
        <nc:config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
          <interfaces xmlns="http://openconfig.net/yang/interfaces">
              <interface>
             
                  <name>eth1/35</name>
                 
                 <config >
                    <type>ianaift:ethernetCsmacd</type>
                    <name>eth1/35</name>
                 </config>
                     <subinterfaces nc:operation="merge">
                        <subinterface nc:operation="merge">
                            <index>3</index>
                               <config>
                               <index>3</index>
                               </config>

                          <ipv4 xmlns="http://openconfig.net/yang/interfaces/ip">
                            <addresses nc:operation="merge">
                               <address>
                                 
                                  <ip>1.2.3.12</ip>
                                  <config>
                                  <ip>1.2.3.12</ip>
                                  <prefix-length>26</prefix-length>
                                  </config>

                               </address>
                            </addresses>
                       
                        </ipv4>



                        </subinterface>



                        <subinterface>
                            <index>2</index>
                               <config>
                               <index>2</index>
                               </config>

                          <ipv4 xmlns="http://openconfig.net/yang/interfaces/ip">
                            <addresses nc:operation="merge">
                               <address>
                                 
                                  <ip>3.4.5.2</ip>
                                  <config>
                                  <ip>3.4.5.2</ip>
                                  <prefix-length>24</prefix-length>
                                  </config>

                               </address>
                            </addresses>
                       
                        </ipv4>



                        </subinterface>
                        



                     </subinterfaces>
                          




              </interface>
          </interfaces>
        </nc:config>
        '''



      



        bgp_cfg = '''
        <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
          <bgp xmlns="http://openconfig.net/yang/bgp">
            <global>
              <config>
                <as>57</as>
               <router-id>7.7.7.7</router-id>
              </config>
            </global>
          </bgp>
        </config>
        '''

        bgp_cfg_reset = '''
        <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
          <bgp xmlns="http://openconfig.net/yang/bgp">
          </bgp>
        </config>
        '''
        '''
        <bgp xmlns="http://openconfig.net/yang/bgp">
            <global>
                <config>
                    <as>50</as>
                    <router-id>1.2.3.4</router-id>
                </config>
            </global>
        </bgp>
    '''

        lcl_rt_cfg = '''
        <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <local-routes xmlns="http://openconfig.net/yang/local-routing">
                <static-routes>
                    <static>
                        <config>
                            <set-tag>0</set-tag>
                            <prefix>11.0.0.0/8</prefix>
                        </config>
                        <next-hops>
                            <next-hop>
                                <config>
                                    <index>null0+DROP+default</index>
                                    <metric>0</metric>
                                    <next-hop>DROP</next-hop>
                                </config>
                                <index>null0+DROP+default</index>
                                <interface-ref xmlns="http://openconfig.net/yang/interfaces">
                                    <config>
                                        <interface>null0</interface>
                                    </config>
                                </interface-ref>
                            </next-hop>
                        </next-hops>
                        <prefix>11.0.0.0/8</prefix>
                    </static>
                </static-routes>
            </local-routes>
        </config>
        '''

        try:
            resp = cisco_manager.edit_config(descr_cfg1, target='running',
                                             default_operation='merge')
            print(resp)
            print('*' * 30)
        except RPCError as err:
            for attr in dir(err):
                if not attr.startswith('__'):
                    print(attr, ':   ', getattr(err, attr))


if __name__ == '__main__':
    main()
