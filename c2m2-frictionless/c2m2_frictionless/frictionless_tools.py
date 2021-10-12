import os
import sys
import json
import shutil
import traceback
from dataclasses import asdict
from datapackage import DataPackage
from datapackage.exceptions import CastError

frictionless_path = os.path.dirname(__file__)

def cell_dumps(v):
  ''' Safely dump a string into a 'tsv' cell. *Without* quotes but *with* escape characters in the case of strings.
  '''
  if v is None:
    return ''
  elif type(v) == str:
    return json.dumps(v)[1:-1]
  else:
    return json.dumps(v)

def create_datapackage(schema, it, outdir):
  ''' Takes an iterator of dataclasses and writes a datapackage in the specified directory

  :param schema: The name of the frictionless datapackage module
  :param it: The iterator of dataclasses
  :param outdir: The directory to write the resulting datapackage
  :return: The instantiated datapackage object after writing.
  :rtype: datapackage.DataPackage
  '''
  # create output directory
  os.makedirs(outdir, exist_ok=True)
  shutil.copy(
    os.path.join(frictionless_path, schema, 'datapackage.json'),
    os.path.join(outdir, 'datapackage.json'),
  )
  fps = {}
  for obj in it:
    table = obj.__class__.__name__
    obj_dict = {k: cell_dumps(v) for k, v in asdict(obj).items()}
    if table not in fps:
      fps[table] = open(os.path.join(outdir, f"{table}.tsv"), 'w')
      print(*obj_dict.keys(), sep='\t', file=fps[table])
    print(*obj_dict.values(), sep='\t', file=fps[table])
  #
  pkg = DataPackage(os.path.join(outdir, 'datapackage.json'))
  # add empty files for any resources not addressed
  for rc in pkg.resources:
    if rc.name not in fps:
      with open(os.path.join(outdir, rc.descriptor['path']), 'w') as fw:
        print(*[field.name for field in rc.schema.fields], sep='\t', end='', file=fw)
  return pkg

def validate_datapackage(pkg):
  ''' Ensure datapackages can be read and satisfy all integrity and relation constraints

  :param pkg: The frictionless datapackage to validate
  '''
  for rc in pkg.resources:
    print(f"Checking {rc.name}...")
    try:
      rc.read(keyed=True)
      assert rc.check_integrity()
      assert rc.check_relations()
    except CastError as e:
      print(f"Failure ({rc.name}): {e.errors}.")
      traceback.print_exc(file=sys.stderr)
    except:
      print(f"Failure ({rc.name}).")
      traceback.print_exc(file=sys.stderr)
    else:
      print(f"Success ({rc.name}).")

