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
VERSION = '0.3'
RELATIVE = 'tf'

DOI_TEXT = '10.5281/zenodo.2652849'
DOI_URL = 'https://doi.org/10.5281/zenodo.2652849'

DOC_URL = f'https://github.com/{ORG}/{REPO}/blob/master/docs/'
DOC_INTRO = 'about.md'
CHAR_URL = f'https://annotation.github.io/text-fabric/Writing/Hebrew.html'
CHAR_TEXT = 'Hebrew characters and transcriptions'

FEATURE_URL = f'{DOC_URL}/transcription.md'

MODULE_SPECS = ()

ZIP = [REPO]

CONDENSE_TYPE = 'line'

NONE_VALUES = {None, 'unknown'}

STANDARD_FEATURES = None  # meaning all loadable features

EXCLUDED_FEATURES = set(
    '''
    fullo
    glypho
    lexo
    punco
    morpho
    srcLn
    '''
)
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
    'layout-orig-full': 'layoutUnicode',
    'layout-trans-full': 'layoutTrans',
    'layout-orig-extra': 'layoutUnicodeX',
    'layout-trans-extra': 'layoutTransX',
}

BROWSE_NAV_LEVEL = 2
BROWSE_CONTENT_PRETTY = False


def deliver():
  return (globals(), dirname(abspath(__file__)))
