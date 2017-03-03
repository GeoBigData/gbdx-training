from gbdxtools import Interface
gbdx = Interface()

# register task with GBDX for use in a workflow
gbdx.task_registry.register(json_filename = 'clip-raster-definition.json')