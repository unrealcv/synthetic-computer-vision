# Use scholar.py to format table
import sys, yaml, pickle, time
sys.path.append('scholar_py')
import scholar

def get_paper_data(querier, paper):
    title = paper.get('title')
    cluster_id = paper.get('cluster_id')

    if cluster_id:
        print 'Query by cluster_id'
        query = scholar.ClusterScholarQuery(cluster = cluster_id)
    else:
        print 'Query by title "%s"' % title
        query = scholar.SearchScholarQuery()
        query.set_phrase(title)

    querier.send_query(query)
    scholar.txt(querier, with_globals=True)

    articles = querier.articles
    time.sleep(1)
    # for art in articles:
    #     print(encode(art.as_txt()) + '\n')
    return articles[0] # Only return the top result

def get_scholar_data(querier, paper_list):
    scholar_data = [get_paper_data(querier, v) for v in paper_list]
    return scholar_data

def read_cache(cache_file):
    # Use pickle to implement cache
    return None

def save_cache(cache_file, obj):
    pass

def format_scholar_data(scholar_data):
    # Use paper's scholar data to generate table or bib file.
    pass

def txt(querier):
    max_label_len = 0
    if len(querier.articles) > 0:
        items = sorted(list(querier.articles[0].attrs.values()),
                       key=lambda item: item[2])
        max_label_len = max([len(str(item[1])) for item in items])

    # Get items sorted in specified order:
    items = sorted(list(querier.query.attrs.values()), key=lambda item: item[2])
    # Find largest label length:
    max_label_len = max([len(str(item[1])) for item in items] + [max_label_len])
    fmt = '[G] %%%ds %%s' % max(0, max_label_len-4)
    for item in items:
        if item[0] is not None:
            print(fmt % (item[1], item[0]))
    if len(items) > 0:
        print

    articles = querier.articles
    for art in articles:
        print(encode(art.as_txt()) + '\n')

def load_paper_list(paper_list_file):
    with open(paper_list_file) as f:
        paper_list = yaml.load(f)
    return paper_list

def main():
    querier = scholar.ScholarQuerier()
    settings = scholar.ScholarSettings()
    scholar.ScholarConf.LOG_LEVEL = 3 

    paper_list_file = 'synthetic.yml'
    paper_list = load_paper_list(paper_list_file)

    cache_file = 'papers.pkl'
    cache = read_cache(cache_file)
    if cache and cache.get('paper_list') == paper_list:
        print 'Use cache from file %s' % cache_file
        # Use cache to reduce the number of google scholar request
        scholar_data = cache.scholar_data
    else:
        print 'Get data from google scholar'
        scholar_data = get_scholar_data(querier, paper_list)
        # update cache
        cache = dict(paper_list = paper_list,
            scholar_data = scholar_data)
        save_cache(cache_file, cache)

    # Merge yml data with google scholar data
    assert(len(paper_list) == scholar_data)

    format_scholar_data(scholar_data)


if __name__ == '__main__':
    main()
