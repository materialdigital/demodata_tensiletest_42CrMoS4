import json
import os
import numpy as np

class UnitDict(dict):
    def __missing__(self, key):
        if key in self:
            return self[key]
        else:
            return key

udict = UnitDict({
    '%': 'percent',
    'mm\u00c2\u00b2': 'mm2',
    'mm²': 'mm2',
    'mm/s': 'mms-1'
})

lookup = {
    'Specimen name:': {'key': 'name', 'pattern': lambda v: {'value': v.rstrip(), 'datatype': 'string'}},
    'Specimen ID:': {'key': 'id', 'pattern': lambda v: {'value': v.rstrip(), 'datatype': 'string'}},
    'Material:': {'key': 'material', 'pattern': lambda v: {'value': v.rstrip(), 'datatype': 'string'}},
    'Specimen type:': {'key': 'specimen_type', 'pattern': lambda v: {'value': v.rstrip(), 'datatype': 'string'}},
    'Gauge diameter:': {'key': 'originaldiameter', 'pattern': lambda v, u: {'value': float(v), 'unit': udict[u.rstrip()], 'datatype': 'float'}},
    'Gauge length:': {'key': 'gaugelength', 'pattern': lambda v, u: {'value': float(v), 'unit': udict[u.rstrip()], 'datatype': 'float'}},
    'Parallel length:': {'key': 'parallellength', 'pattern': lambda v, u: {'value': float(v), 'unit': udict[u.rstrip()], 'datatype': 'float'}},
    'Original cross-section:': {'key': 'originalcrosssection', 'pattern': lambda v, u: {'value': float(v), 'unit': udict[u.rstrip()], 'datatype': 'float'}},
    'Cross-section after fracture:': {'key': 'crosssectionafterfracture', 'pattern': lambda v, u: {'value': float(v), 'unit': udict[u.rstrip()], 'datatype': 'float'}},
    'Yield stress at 0.2% plastic strain:': {'key': 'yield02', 'pattern': lambda v, u: {'value': float(v), 'unit': udict[u.rstrip()], 'datatype': 'float'}},
    'Yield stress at 1% plastic strain:': {'key': 'yield1', 'pattern': lambda v, u: {'value': float(v), 'unit': udict[u.rstrip()], 'datatype': 'float'}},
    'Ultimate tensile strength:': {'key': 'tensilestrength', 'pattern': lambda v, u: {'value': float(v), 'unit': udict[u.rstrip()], 'datatype': 'float'}},
    'Uniform elongation:': {'key': 'uniformelongation', 'pattern': lambda v, u: {'value': float(v), 'unit': udict[u.rstrip()], 'datatype': 'float'}},
    'Elongation after fracture:': {'key': 'elongationafterfracture', 'pattern': lambda v, u: {'value': float(v), 'unit': udict[u.rstrip()], 'datatype': 'float'}},
    'Reduction of area:': {'key': 'reductionofarea', 'pattern': lambda v, u: {'value': float(v), 'unit': udict[u.rstrip()], 'datatype': 'float'}},
    'Slope of linear-elastic region:': {'key': 'slopeoftheelasticpart', 'pattern': lambda v, u: {'value': float(v), 'unit': udict[u.rstrip()], 'datatype': 'float'}},
    'Crosshead seperation speed:': {'key': 'crossheadsepspeed', 'pattern': lambda v, u: {'value': float(v), 'unit': udict[u.rstrip()], 'datatype': 'float'}},
    'Strain rate:': {'key': 'strainrate', 'pattern': lambda v, u: {'value': float(v), 'unit': udict[u.rstrip()], 'datatype': 'float'}},
    'Test temperature:': {'key': 'temperature', 'pattern': lambda v, u: {'value': v.rstrip(), 'datatype': 'string'}},
    'Machine type:': {'key': 'machine_type', 'pattern': lambda v: {'value': v.rstrip(), 'datatype': 'string'}},
    'Standard:': {'key': 'standard', 'pattern': lambda v: {'value': v.rstrip(), 'datatype': 'string'}},
    'Date:': {'key': 'dateoftest', 'pattern': lambda v: {'value': v.split()[0], 'datatype': 'date'}},
    'Heat treatment batch:': {'key': 'heattreatmentbatch', 'pattern': lambda v: {'value': v.rstrip(), 'datatype': 'string'}}
}

def tocsvjson(id, skip_json=False):
    with open(f'original_data/{id}.csv') as f:
        d = {}
        csvlines = []
        mode = 'metadata'
        for line in f:
            if line.startswith('Time'):
                mode = 'tsdata'
            if mode == 'metadata':
                dset = line.split('\t')
                d.update({lookup[dset[0]]['key']: lookup[dset[0]]['pattern'](*dset[1:])})
            if mode == 'tsdata':
                csvlines.append(line.replace('\t', ','))
    if not skip_json: 
        with open(f'resources/{id}.json', 'w') as f:
            json.dump(d, f, indent=2)
    with open(f'resources/{id}.csv', 'w') as f:
        f.write(''.join(csvlines))

def create_dataset(id):
    with open('dataset_template.ttl_tmp', 'r', encoding='utf8') as inf:
        with open(f'datasets/{id}.ttl', 'w', encoding='utf8') as outf:
            for line in inf:
                outf.write(line.replace('{{id}}', id))

if __name__ == '__main__':
    for id in [f.split('.')[0] for f in os.listdir('./original_data')]:
        if not os.path.exists('resources'):
            os.mkdir('resources')
        if not os.path.exists('datasets'):
            os.mkdir('datasets')
        tocsvjson(id)
        create_dataset(id)
