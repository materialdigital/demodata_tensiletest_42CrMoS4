import argparse

def gen_html(writer, title, repo_owner, repo_name, rdfname, resources, version):
    writer.write('<!DOCTYPE html>\n')
    writer.write('<html>\n')
    writer.write(f'<title>{title:s}</title>\n')
    writer.write('<body>\n')
    writer.write(f'<h1>{title:s}</h1>\n')
    writer.write('<h2>RDF resources</h2>\n')
    writer.write('<ul>\n')
    writer.write(f'<li><a href="https://{repo_owner:s}.github.io/{repo_name:s}/{version}/{rdfname:s}.ttl">https://{repo_owner:s}.github.io/{repo_name:s}/{version}/{rdfname:s}.ttl</a></li>\n')
    writer.write(f'<li><a href="https://{repo_owner:s}.github.io/{repo_name:s}/{version}/{rdfname:s}.rdf">https://{repo_owner:s}.github.io/{repo_name:s}/{version}/{rdfname:s}.rdf</a></li>\n')
    writer.write('</ul>\n')
    writer.write('<h2>File resources</h2>\n')
    writer.write('<ul>\n')
    for resource in resources:
        writer.write(f'<li><a href="https://{repo_owner:s}.github.io/{repo_name:s}/{resource:s}">https://{repo_owner:s}.github.io/{repo_name:s}/{resource:s}</a></li>\n')
    writer.write('</ul>\n')
    writer.write('</body>\n')
    writer.write('<html>\n')

def make_parser():
    parser_ = argparse.ArgumentParser()
    parser_.add_argument('-t', '--title', required=True, help='Title for the index page')
    parser_.add_argument('-o', '--owner', required=True, help='Repo owner/group')
    parser_.add_argument('-n', '--name', required=True, help='Repo name')
    parser_.add_argument('-v', '--version', required=True, help='Ontology file version')
    parser_.add_argument('-r', '--rdfname', required=True, help='Name of the rdf files (without extension)')
    parser_.add_argument('-l', '--resourceslist', required=True, help='List of all resources (with extension)')
    parser_.add_argument('-f', '--outfile', required=True, help='Path of the target html file')
    return parser_

if __name__ == '__main__':
    parser = make_parser()
    args = parser.parse_args()

    with open(args.resourceslist, 'r', encoding='utf8') as f:
        resources_ = [line.strip() for line in f]

    html_args = {
        "title": args.title,
        "repo_owner": args.owner,
        "repo_name": args.name,
        "rdfname": args.rdfname,
        "version": args.version,
        "resources": resources_
    }

    with open(args.outfile, 'w', encoding='utf8') as f:
        gen_html(f, **html_args)
