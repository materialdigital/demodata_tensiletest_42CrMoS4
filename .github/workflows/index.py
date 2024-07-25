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

    return tree


def make_parser():
    parser_ = argparse.ArgumentParser()
    parser_.add_argument('-t', '--template', required=True, help='Path to the template file')
    parser_.add_argument('-l', '--resourceslist', required=True, help='List of all resources (with extension)')
    parser_.add_argument('-f', '--outfile', required=True, help='Path of the target html file')
    parser_.add_argument('-b', '--resourcesbase', default='https://w3id.org/pmd/demodata/tensiletest_42CrMoS4/', help='URI for dereferencing resources')
    return parser_

if __name__ == '__main__':
    parser = make_parser()
    args = parser.parse_args()
    
    with open(args.resourceslist, 'r', encoding='utf8') as f:
        resources_ = [line.strip() for line in f]

    new_html = update_html(
        template_file=args.template,
        resources=resources_,
        resources_base=args.resourcesbase
    )

    new_html.write(args.outfile, method='html', pretty_print=True)
