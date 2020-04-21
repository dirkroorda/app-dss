from os.path import dirname, abspath

API_VERSION = 1

PROTOCOL = "http://"
HOST = "localhost"
PORT = dict(kernel=18987, web=8107)

ORG = "etcbc"
REPO = "dss"
CORPUS = "Dead Sea Scrolls"
VERSION = "0.6"
RELATIVE = "tf"

DOI_TEXT = "10.5281/zenodo.2652849"
DOI_URL = "https://doi.org/10.5281/zenodo.2652849"

DOC_URL = f"https://github.com/{ORG}/{REPO}/blob/master/docs/"
DOC_INTRO = "about.md"
CHAR_URL = f"https://annotation.github.io/text-fabric/Writing/Hebrew.html"
CHAR_TEXT = "Hebrew characters and transcriptions"

FEATURE_URL = f"{DOC_URL}/transcription.md"

MODULE_SPECS = (
    dict(
        org=ORG,
        repo="dss",
        relative=f"parallels/{RELATIVE}",
        corpus="Parallel Passages",
        docUrl=(
            "https://nbviewer.jupyter.org/github/etcbc/dss/"
            "blob/master/programs/parallels.ipynb"
        ),
        doiText="10.5281/zenodo.2652849",
        doiUrl="https://doi.org/10.5281/zenodo.2652849",
    ),
)

ZIP = [REPO] + [(m["org"], m["repo"], m["relative"]) for m in MODULE_SPECS]

BASE_TYPE = "word"
CONDENSE_TYPE = "line"

NONE_VALUES = {None, "unknown"}

STANDARD_FEATURES = None  # meaning all loadable features

EXCLUDED_FEATURES = set()

NO_DESCEND_TYPES = {"lex"}

EXAMPLE_SECTION = "<code>1Q1 f1:1</code>"
EXAMPLE_SECTION_TEXT = "1Q1 f1:1"

SECTION_SEP1 = " "
SECTION_SEP2 = ":"

WRITING = "hbo"
WRITING_DIR = "rtl"

FONT_NAME = "Ezra SIL"
FONT = "SILEOT.ttf"
FONTW = "SILEOT.woff"

TEXT_FORMATS = {
    "layout-orig-full": "layoutOrig",
    "layout-trans-full": "layoutTrans",
    "layout-source-full": "layoutSource",
}

BROWSE_NAV_LEVEL = 2
BROWSE_CONTENT_PRETTY = False

VERSE_TYPES = None

LEX = "lex"

TRANSFORM = None

CHILD_TYPE = dict(
    scroll="fragment",
    fragment="line",
    line="word",
    verse="word",
    half_verse="word",
    word="sign",
    cluster="sign",
)

SUPER_TYPE = None

TYPE_DISPLAY = dict(
    scroll=dict(
        template="{scroll}",
        bareFeatures="",
        features="biblical",
        level=3, flow="col", wrap=False, stretch=False,
    ),
    fragment=dict(
        template="{fragment}",
        bareFeatures="",
        features="biblical",
        level=3, flow="col", wrap=False, strectch=False,
    ),
    line=dict(
        template="{line}",
        bareFeatures="",
        features="biblical",
        level=2, flow="row", wrap=True, strectch=True,
    ),
    cluster=dict(
        template="{type}",
        bareFeatures="",
        features="",
        level=2, flow="row", wrap=True, strectch=False,
    ),
    word=dict(
        template=True,
        bareFeatures="sp",
        features="lang lex cl ps gn nu st vs vt md",
        level=1, flow="row", wrap=False, strectch=True,
    ),
    lex=dict(
        template=None,
        bareFeatures="lexo",
        features="lex lexe",
        level=1, flow="col", wrap=False, strectch=True,
    ),
    sign=dict(
        template=True,
        bareFeatures="",
        features="",
        level=0, flow="col", wrap=False, strectch=False,
    ),
)

INTERFACE_DEFAULTS = dict()

LINE_NUMBERS = dict(word="srcLn")


def deliver():
    return (globals(), dirname(abspath(__file__)))
