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

EXAMPLE_SECTION = "<code>1Q1 f1:1</code>"
EXAMPLE_SECTION_TEXT = "1Q1 f1:1"

DATA_DISPLAY = dict(
    noneValues={None, "unknown"},
    sectionSep1=" ",
    sectionSep2=":",
    writing="hbo",
    writingDir="rtl",
    fontName="Ezra SIL",
    font="SILEOT.ttf",
    fontw="SILEOT.woff",
    textFormats={
        "layout-orig-full": "layoutOrig",
        "layout-trans-full": "layoutTrans",
        "layout-source-full": "layoutSource",
    },
    browseNavLevel=2,
    browseContentPretty=False,
)

TYPE_DISPLAY = dict(
    scroll=dict(
        template="{scroll}",
        features="biblical",
        children="fragment",
        level=3, flow="col", wrap=False, stretch=False,
    ),
    fragment=dict(
        template="{fragment}",
        features="biblical",
        children="line",
        level=3, flow="col", wrap=False, strectch=False,
    ),
    line=dict(
        template="{line}",
        features="biblical",
        children="word",
        condense=True,
        level=2, flow="row", wrap=True, strectch=True,
    ),
    cluster=dict(
        template="{type}",
        children="sign",
        level=2, flow="row", wrap=True, strectch=False,
    ),
    word=dict(
        template=True,
        featuresBare="sp",
        features="lang lex cl ps gn nu st vs vt md",
        children="sign",
        base=True,
        lineNumber="srcLn",
        level=1, flow="row", wrap=False, strectch=True,
    ),
    lex=dict(
        template="{lex}",
        featuresBare="lexo",
        features="lex lexe",
        lexTarget="word",
        level=1, flow="col", wrap=False, strectch=True,
    ),
    sign=dict(
        template=True,
        level=0, flow="col", wrap=False, strectch=False,
    ),
)

INTERFACE_DEFAULTS = dict(
    lineNumbers=False,
)


def deliver():
    return (globals(), dirname(abspath(__file__)))
