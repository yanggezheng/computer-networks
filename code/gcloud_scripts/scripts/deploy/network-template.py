def generate_config(context):
  resources = [{
      'name': context.env['name'],
      'type': 'compute.v1.network',
      'properties': {
          'routingConfig': {
              'routingMode': 'REGIONAL'
          },
          'autoCreateSubnetworks': False
      }
  }, {
      'name': context.env['name'] + '-subnetwork',
      'type': 'compute.v1.subnetwork',
      'properties': {
        'region': context.properties['region'],
        'network': '$(ref.' + context.env['name'] + '.selfLink)',
        'ipCidrRange': context.properties['ipCidrRange'],
        'privateIpGoogleAccess': False
      }
  }, {
      'name': context.env['name'] + '-firewall',
      'type': 'compute.v1.firewall',
      'properties': {
          'network': '$(ref.' + context.env['name'] + '.selfLink)',
          'sourceRanges': ['0.0.0.0/0'],
          'allowed': [{ 'IPProtocol': 'TCP' }, { 'IPProtocol': 'UDP' }]
      }
  }]
  return {'resources': resources}
