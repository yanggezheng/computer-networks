COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'
GCS_MNT_DIR = "/mnt"

def mount_gcs_command(project: str):
  return f'gcsfuse {project} {GCS_MNT_DIR}'

def generate_config(context):
  resources = [{
      'name': context.env['name'],
      'type': 'compute.v1.instance',
      'properties': {
          'zone': context.properties['zone'],
          'machineType': ''.join([COMPUTE_URL_BASE, 'projects/',
                                  context.env['project'], '/zones/',
                                  context.properties['zone'], '/machineTypes/',
                                  context.properties['machineType']]),
          'disks': [{
              'deviceName': 'boot',
              'type': 'PERSISTENT',
              'boot': True,
              'autoDelete': True,
              'initializeParams': {
                  'sourceImage': 'projects/nyu-networking-course-base/global/images/course-image'
              }
          }],
          'networkInterfaces': [{
              'network': '$(ref.' + context.properties['network']
                         + '.selfLink)',
              'subnetwork': '$(ref.' + context.properties['network'] + '-subnetwork'
                         + '.selfLink)',
              'networkIP': context.properties['privateIP'],
              'accessConfigs': [{
                  'name': 'External NAT',
                  'type': 'ONE_TO_ONE_NAT'
              }]
          }],
          'serviceAccounts': [
            { 'scopes': ['https://www.googleapis.com/auth/devstorage.read_write'] }
          ],
          'metadata': {
            'items': [
              { 'key': 'startup-script', 'value': mount_gcs_command(context.env['project']) }
            ]
          }
      }
  }]
  return {'resources': resources}
