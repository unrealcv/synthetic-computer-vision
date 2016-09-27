import sys, pickle, os, time
cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cur_dir, 'scholar_py'))
import scholar

cache_file = 'papers.pkl'

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


def get_scholar_data(paper_list):
    querier = scholar.ScholarQuerier()
    settings = scholar.ScholarSettings()
    settings.set_citation_format(scholar.ScholarSettings.CITFORM_BIBTEX)
    querier.apply_settings(settings)
    scholar.ScholarConf.LOG_LEVEL = 3

    cache = read_cache(cache_file)
    if cache and cache.get('paper_list') == paper_list:
        print 'Use cache from file %s' % cache_file
        # Use cache to reduce the number of google scholar request
        scholar_data = cache['scholar_data']
    else:
        print 'Get data from google scholar'
        scholar_data = [get_paper_data(querier, v) for v in paper_list]
        # update cache
        cache = dict(paper_list = paper_list,
            scholar_data = scholar_data)
        save_cache(cache_file, cache)

    return scholar_data


def read_cache(cache_file):
    # Use pickle to implement cache
    print 'Load cache from file %s' % cache_file
    if not os.path.isfile(cache_file):
        return None

    with open(cache_file, 'r') as f:
        return pickle.load(f)

def save_cache(cache_file, obj):
    print 'Save obj to cache %s' % cache_file
    with open(cache_file, 'w') as f:
        pickle.dump(obj, f)
