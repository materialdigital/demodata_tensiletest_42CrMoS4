import rdflib
import os

PMD = rdflib.Namespace('https://w3id.org/pmd/co/')
TTO = rdflib.Namespace('https://w3id.org/pmd/tto/')
QUDT = rdflib.Namespace('https://qudt.org/vocab/unit/')
EX = rdflib.Namespace('https://w3id.org/pmd/projects/refdataproject/')

g = rdflib.Graph()

g.bind('pmd', PMD)
g.bind('tto', TTO)
g.bind('qudt', QUDT)
g.bind('', EX)

g.parse('refdataproject_production.ttl', format='turtle')
g.parse('refdataproject_tensiletests.ttl', format='turtle')
for dataset_ttl in [os.path.join('datasets', f'{f}') for f in os.listdir('datasets')]:
    g.parse(dataset_ttl, format='turtle')

#print(f"Graph is connected: {g.connected()}")

g.serialize('refdataproject_combined.ttl', format='turtle')
g.serialize('refdataproject_combined.rdf', format='xml')

## create list of resources
resources = [str(row.o).replace("https://w3id.org/pmd/projects/refdataproject/", "") for row in g.query("""SELECT * WHERE {
    ?s dcat:downloadURL ?o
}""")]
with open('resources.txt', 'w', encoding='utf8') as f:
    f.write('\n'.join(resources))
