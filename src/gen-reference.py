# Use scholar.py to format table
import sys, yaml, pickle, os, time, datetime, argparse
import bibtexparser
import scholarutil

def format_scholar_data(scholar_data):
    # Use paper's scholar data to generate table or bib file.
    for art in scholar_data:
        print art['title']
        # print art['Citations']
        print art['num_citations']
        print art.as_txt()
        print art.as_citation()

def format_as_md_row(paper):
    template = [
        # if exist, use 1, if not use '' or 2
        ('', '- ', ''),
        ('ID', '<div id="{ID}"/>', ''),
        ('author', '[{first_author}, et al.](# "{author}"),', ''), # Hover to see tooltip
        ('url', '"[{title}]({url})"', '"{title}"'),
        ('booktitle', '{booktitle}', ''),
        ('year', '{year}', ''),
        ('', '\n\n\t', ''),
        ('code', '([code]({code}))', ''),
        ('project', '([project]({project}))', ''),
        ('num_citations', '([citation:{num_citations}]({url_citations}))', '')
    ]

    row = ''
    for (k, t1, t2) in template:
        if k == '':
            row += t1
            continue

        if paper.get(k):
            row += t1.format(**paper) + ' '
        else:
            row += t2.format(**paper) + ' '

    return row

def format_by_year(papers):
    # Format the reference list
    print '-' * 80
    years = list(set([int(article['year']) for article in papers]))
    print years
    years.sort(reverse = True)

    sections = []
    for year in years:
        rows = [format_as_md_row(paper) for paper in papers if int(paper['year']) == year]
        section_head = '## %d \n(Total=%d)' % (year, len(rows))
        sections.append('\n'.join([section_head] + rows))

    content = '\n\n'.join(sections)
    print content
    return content

def load_paper_list(paper_list_file):
    with open(paper_list_file) as f:
        paper_list = yaml.load(f)
    return paper_list

def merge_data(paper_list, scholar_data):
    # Merge yml data with google scholar data
    assert(len(paper_list) == len(scholar_data))
    papers = []
    for v in range(len(paper_list)):
        paper = dict()
        # paper = paper_list[v]

        meta = scholar_data[v]
        # see __getitem__ of ScholarArticle
        attrs = dict([(key, meta.attrs[key][0]) for key in meta.attrs.keys()])
        paper.update(attrs)
        paper['citation_data'] = meta.citation_data

        bibdata = bibtexparser.loads(meta.citation_data)
        bibinfo = bibdata.entries[0]
        paper.update(bibdata.entries[0])

        paper.update(paper_list[v])
        # This should have the highest priority and overwrite others

        if len(papers) == 0:
            # Only do it once
            print 'Scholar data field %s' % attrs.keys()
            print 'Bib data fields %s' % bibinfo.keys()

        if paper.get('author'):
            paper['first_author'] = paper['author'].split('and')[0].strip()
        papers.append(paper)


    print 'Available data fields %s' % papers[0].keys()
    return papers

def main():
    paper_list_file = 'synthetic.yml'
    parser = argparse.ArgumentParser()
    parser.add_argument('yaml_file', default=paper_list_file)

    args = parser.parse_args()
    paper_list_file = args.yaml_file

    paper_list = load_paper_list(paper_list_file)

    scholar_data = scholarutil.get_scholar_data(paper_list)
    format_scholar_data(scholar_data)

    papers = merge_data(paper_list, scholar_data)

    # Make usage of our data
    # format_scholar_data(scholar_data)
    reference = format_by_year(papers)
    date = datetime.datetime.now().strftime('%D')
    # with open('reference.md', 'w') as f:
    #     f.write(format_by_year(papers))

    with open('README_raw.md', 'r') as f:
        template = f.read()
        readme = template.format(reference = reference, date = date)

    with open('../README.md', 'w') as f:
        f.write(readme)
    # format_scholar_data(scholar_data)


if __name__ == '__main__':
    main()
