# geograph_tranquillity

The script "selecting_documents.py" selects tranquillity-related descriptions from the Geograph data (http://data.geograph.org.uk/dumps/) available under a Creative Commons BY-SA 2.0 licence (https://creativecommons.org/licenses/by-sa/2.0/).
Tranquillity search terms are published in:
Wartmann, F.M., Tieskens, K.F., van Zanten, B.T., Verburg, P.H., 2019. Exploring tranquillity experienced in landscapes based on social media. Appl. Geogr. 113, 102112.

Additionally, the script "selecting_documents.py" creates files with x random descriptions extracted using each of the search terms.
These are further used for manual annotation.

"dependency.py" extract all dependencies marked as "amod" (adjectival modifiers). For this code you need Python 3.

"adding_coord_time.py" merges two datasets ( 'gridimage_text.tsv' and gridimage_base.tsv') together.
