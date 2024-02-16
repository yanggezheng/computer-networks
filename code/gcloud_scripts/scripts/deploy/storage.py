
def generate_config(context):
  resources = [{
      'name': context.env['name'],
      'type': 'storage.v1.bucket'
  }]
  return {'resources': resources}
