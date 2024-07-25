import os
import argparse
from lxml import html
from lxml.cssselect import CSSSelector

def update_html(template_file, resources, resources_base):
    tree = html.parse(template_file)
    sel = CSSSelector('ul#fileresources')

    ulnode = [e for e in sel(tree)][0]
    for resource in resources[::-1]:
        linode = html.fromstring(f'<li><a href="{resources_base:s}{resource:s}">{resources_base:s}{resource:s}</a></li>\n')
        ulnode.insert(0, linode)

    return html.tostring(tree, pretty_print=True)


def make_parser():
    parser_ = argparse.ArgumentParser()
    parser_.add_argument('-t', '--template', required=True, help='Path to the template file')
    parser_.add_argument('-l', '--resourceslist', required=True, help='List of all resources (with extension)')
    parser_.add_argument('-f', '--outfile', required=True, help='Path of the target html file')
    parser_.add_argument('-b', '--resourcesbase', default='https://w3id.org/pmd/demodata/tensiletest_42CrMoS4/resources/', help='URI for dereferencing resources')
    return parser_

if __name__ == '__main__':
    parser = make_parser()
    args = parser.parse_args()
    
    with open(args.resourceslist, 'r', encoding='utf8') as f:
        resources_ = [line.strip() for line in f]

    new_html = update_html(
        template_file=os.path.join('.github', 'workflows', 'index.html'),
        resources=resources_,
        resources_base='https://w3id.org/pmd/demodata/tensiletest_42CrMoS4/resources/'
    )

    with open(args.outfile, 'w', encoding='utf8') as f:
        f.write(new_html)
