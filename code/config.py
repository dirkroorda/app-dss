from os.path import dirname, abspath

PROTOCOL = 'http://'
HOST = 'localhost'
PORT = dict(
    kernel=18987,
    web=8107,
)

OPTIONS = (
    ('lineNumbers', False, 'checkbox', 'linen', 'show line numbers'),
)


ORG = 'etcbc'
REPO = 'dss'
CORPUS = 'Dead Sea Scrolls'
VERSION = '0.5'
RELATIVE = 'tf'

DOI_TEXT = '10.5281/zenodo.2652849'
DOI_URL = 'https://doi.org/10.5281/zenodo.2652849'

DOC_URL = f'https://github.com/{ORG}/{REPO}/blob/master/docs/'
DOC_INTRO = 'about.md'
CHAR_URL = f'https://annotation.github.io/text-fabric/Writing/Hebrew.html'
CHAR_TEXT = 'Hebrew characters and transcriptions'

FEATURE_URL = f'{DOC_URL}/transcription.md'

MODULE_SPECS = (
    dict(
        org=ORG,
        repo='dss',
        relative=f'parallels/{RELATIVE}',
        corpus='Parallel Passages',
        docUrl=(
            'https://nbviewer.jupyter.org/github/etcbc/dss/'
            'blob/master/programs/parallels.ipynb'
        ),
        doiText='10.5281/zenodo.2652849',
        doiUrl='https://doi.org/10.5281/zenodo.2652849',
    ),
)

ZIP = [REPO] + [(m['org'], m['repo'], m['relative']) for m in MODULE_SPECS]

CONDENSE_TYPE = 'line'

NONE_VALUES = {None, 'unknown'}

STANDARD_FEATURES = None  # meaning all loadable features

EXCLUDED_FEATURES = set()

NO_DESCEND_TYPES = {'lex'}

EXAMPLE_SECTION = '<code>1Q1 f1:1</code>'
EXAMPLE_SECTION_TEXT = '1Q1 f1:1'

SECTION_SEP1 = ' '
SECTION_SEP2 = ':'

DEFAULT_CLS = 'txtn'
DEFAULT_CLS_ORIG = 'txtu'

FORMAT_CSS = dict(
    orig='txtu',
    trans='txte',
    source='txto',
)

CLASS_NAMES = None

FONT_NAME = 'Ezra SIL'
FONT = 'SILEOT.ttf'
FONTW = 'SILEOT.woff'

TEXT_FORMATS = {
    'layout-orig-full': 'layoutOrig',
    'layout-trans-full': 'layoutTrans',
    'layout-source-full': 'layoutSource',
}

BROWSE_NAV_LEVEL = 2
BROWSE_CONTENT_PRETTY = False


def deliver():
  return (globals(), dirname(abspath(__file__)))
