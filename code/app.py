from tf.applib.helpers import dh, NB
from tf.applib.api import setupApi
from tf.applib.links import outLink

EMPTY = "empty"

MODIFIERS = """
    lang
    script
    intl
    unc
    cor
    rem
    rec
    alt
    vac
""".strip().split()

URL_FORMAT = "https://www.deadseascrolls.org.il/explore-the-archive/search#q='{}'"


def notice(app):
    if int(app.api.TF.version.split(".")[0]) <= 7:
        print(
            f"""
Your Text-Fabric is outdated.
It cannot load this version of the TF app `{app.appName}`.
Recommendation: upgrade Text-Fabric to version 8.
Hint:

    pip3 install --upgrade text-fabric

"""
        )


class TfApp(object):
    def __init__(app, *args, _asApp=False, silent=False, **kwargs):
        setupApi(app, *args, _asApp=_asApp, silent=silent, **kwargs)
        notice(args[0])

    def webLink(app, n, text=None, className=None, _asString=False, _noUrl=False):
        api = app.api
        T = api.T

        (scroll, fragment, line) = T.sectionFromNode(n, fillup=True)
        passageText = app.sectionStrFromNode(n)
        href = "#" if _noUrl else URL_FORMAT.format(scroll)
        if text is None:
            text = passageText
            title = f"show this scroll in the Leon Levy library"
        else:
            title = passageText
        if _noUrl:
            title = None
        target = "" if _noUrl else None

        result = outLink(
            text,
            href,
            title=title,
            className=className,
            target=target,
            passage=passageText,
        )
        if _asString:
            return result
        dh(result)

    def fmt_layoutOrig(app, n):
        return app._wrapHtml(n, "glyph", "")

    def fmt_layoutTrans(app, n):
        return app._wrapHtml(n, "glyph", "e")

    def fmt_layoutSource(app, n):
        return app._wrapHtml(n, "glyph", "o")

    def _wrapHtml(app, n, ft, kind):
        api = app.api
        F = api.F
        Fs = api.Fs
        after = F.after.v(n) or ""
        isEmpty = F.type.v(n) == EMPTY
        material = NB if isEmpty else (Fs(f"{ft}{kind}").v(n) or "")
        classes = " ".join(f"{cf}{Fs(cf).v(n)}" for cf in MODIFIERS if Fs(cf).v(n))
        empty = " empty" if isEmpty else ""
        if classes:
            material = f'<span class="{classes}{empty}">{material}</span>'
        return f"{material}{after}"
