from os.path import dirname, abspath

API_VERSION = 1

PROVENANCE_SPEC = dict(
    org="etcbc",
    repo="dss",
    version="0.6",
    moduleSpecs=(
        dict(
            repo="dss",
            relative=f"parallels/tf",
            doi="10.5281/zenodo.2652849",
            corpus="Parallel Passages",
            docUrl="{nbUrl}/etcbc/dss/blob/master/programs/parallels.ipynb",
        ),
    ),
    doi="10.5281/zenodo.2652849",
    corpus="Dead Sea Scrolls",
    webBase="https://www.deadseascrolls.org.il/explore-the-archive",
    webUrl="{base}/search#q='{<1>}'",
    webHint="Show this scroll in the Leon Levy library",
)

DOCS = dict(docPage="about", featureBase="{docBase}", featurePage="transcription")

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
    scroll=dict(features="biblical"),
    fragment=dict(features="biblical"),
    line=dict(features="biblical", children="word"),
    cluster=dict(template="{type}", children="sign", stretch=False),
    word=dict(
        template=True,
        featuresBare="sp",
        features="lang lex cl ps gn nu st vs vt md",
        base=True,
        lineNumber="srcLn",
        wrap=False,
    ),
    lex=dict(
        template="{lex}", featuresBare="lexo", features="lex lexe", lexOcc="word",
    ),
)

INTERFACE_DEFAULTS = dict(lineNumbers=False)


def deliver():
    return (globals(), dirname(abspath(__file__)))
