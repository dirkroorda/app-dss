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
    writing="hbo",
    textFormats={
        "layout-orig-full": "layoutOrig",
        "layout-trans-full": "layoutTrans",
        "layout-source-full": "layoutSource",
    },
)

TYPE_DISPLAY = dict(
    scroll=dict(features="biblical",),
    fragment=dict(features="biblical",),
    line=dict(features="biblical", children="word",),
    cluster=dict(template="{type}", children="sign", stretch=False,),
    word=dict(
        template=True,
        featuresBare="sp",
        features="lang lex cl ps gn nu st vs vt md",
        base=True,
        lineNumber="srcLn",
        wrap=False,
    ),
    lex=dict(
        template="{lex}", featuresBare="lexo", features="lex lexe", lexTarget="word",
    ),
)

INTERFACE_DEFAULTS = dict(lineNumbers=False,)


def deliver():
    return (globals(), dirname(abspath(__file__)))
