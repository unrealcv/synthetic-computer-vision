import os
cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cur_dir, 'scholar_py'))
import scholar
# Run a test of scholar.py to see whether I am able to retrieve data.
scholar.py -c 1 --author "albert einstein" --phrase "quantum theory"

title = "UnrealCV: Connecting Computer Vision to Unreal Engine"
query = scholar.SearchScholarQuery()
query.set_phrase(title)
