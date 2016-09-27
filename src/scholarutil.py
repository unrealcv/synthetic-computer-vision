import sys, pickle, os, time, yaml
cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cur_dir, 'scholar_py'))
import scholar

cache_file = os.path.join(cur_dir, 'papers.pkl')
yaml_cache_file = os.path.join(cur_dir, 'papers_cache.yml')

def get_paper_data(querier, paper):
    if type(paper) is dict:
        title = paper.get('title')
        cluster_id = paper.get('cluster_id')
    elif type(paper) is str:
        title = paper
    else:
        raise "Input arg paper is of an invalid format %s" % repr(paper)


    if cluster_id:
        print 'Query by cluster_id'
        query = scholar.ClusterScholarQuery(cluster = cluster_id)
    else:
        print 'Query by title "%s"' % title
        query = scholar.SearchScholarQuery()
        query.set_phrase(title)

    query.set_num_page_results(1)
    # This is important, set this to 1 can reduce the possiblility of get blocked by google
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
    assert(cache != None)

    if cache.get('paper_list') == paper_list:
        print 'Use cache from file %s' % cache_file
        # Use cache to reduce the number of google scholar request
    else:
        # Update cache, instead of flushing a complete new one
        print 'Get data from google scholar'
        cache_paper_title = [p['title'] for p in cache['paper_list']]

        missing_paper = [p for p in paper_list if p['title'] not in cache_paper_title]
        missing_scholar_data = [get_paper_data(querier, v) for v in missing_paper]
        # update cache

        cache['paper_list'] += missing_paper
        cache['scholar_data'] += missing_scholar_data
        save_cache(cache_file, cache)

    save_cache(cache_file, cache) # Enforce to flush cache
    return cache['scholar_data']


def read_pickle_cache(cache_file):
    # Use pickle to implement cache
    print 'Load cache from file %s' % cache_file
    if not os.path.isfile(cache_file):
        empty_db = dict(paper_list = [], scholar_data = [])
        return empty_db

    with open(cache_file, 'r') as f:
        db = pickle.load(f)
        assert(db.get('paper_list'))
        assert(db.get('scholar_data'))
        assert(len(db['paper_list']) == len(db['scholar_data']))
        return db

def save_pickle_cache(cache_file, obj):
    print 'Save obj to cache %s' % cache_file
    with open(cache_file, 'w') as f:
        pickle.dump(obj, f)

read_cache = read_pickle_cache
save_cache = save_pickle_cache

def read_yaml_cache(cache_file):
    print 'Load cache from file %s' % cache_file
    if not os.path.isfile(cache_file):
        return None

    with open(cache_file, 'r') as f:
        return yaml.load(f)

def save_yaml_cache(cache_file, obj):
    print 'Save obj to cache %s' % cache_file
    with open(cache_file, 'w') as f:
        yaml.dump(obj, f)

