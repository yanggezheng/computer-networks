REGION = 'us-east4'
ZONE = 'us-east4-a'
MACHINE_TYPE = 'f1-micro'

def resource_name(resource: str):
  return 'nyu-networking-course-' + resource;

def generate_config(context):
  network_name = resource_name('vpc')

  resources = [{
      'name': resource_name('server'),
      'type': 'vm-template.py',
      'properties': {
          'machineType': MACHINE_TYPE,
          'zone': ZONE,
          'network': network_name,
          'privateIP': '10.0.1.1'
      }
  }, {
      'name': resource_name('client'),
      'type': 'vm-template.py',
      'properties': {
          'machineType': MACHINE_TYPE,
          'zone': ZONE,
          'network': network_name,
          'privateIP': '10.0.1.2'
      }
  }, {
      'name': context.env['project'],
      'type': 'storage.py'
  }, {
      'name': network_name,
      'type': 'network-template.py',
      'properties': {
        'region': REGION,
        'ipCidrRange': '10.0.0.0/16'
      }
  }]
  return {'resources': resources}
