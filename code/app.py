import os

from tf.core.helpers import mdhtmlEsc, htmlEsc, mdEsc
from tf.applib.helpers import dh
from tf.applib.display import prettyPre, getBoundary, getFeatures
from tf.applib.highlight import hlText, hlRep
from tf.applib.api import setupApi
from tf.applib.links import outLink

REPORT_DIR = 'reports'

SCROLL = 'scroll'
FRAGMENT = 'fragment'
LINE = 'line'
CLUSTER = 'cluster'
WORD = 'word'
SIGN = 'sign'

BOOK = 'book'
CHAPTER = 'chapter'
VERSE = 'verse'
HALFVERSE = 'halfverse'

BIBLICAL = 'biblical'
SRCLN = 'srcLn'
LANG = 'lang'
INTERLINEAR = 'intl'

CONTENT_FEATURES = '''
  glyph
  glyphe
  glypho
'''.strip().split()

FLAG_FEATURES = '''
    unc
'''.strip().split()

CLUSTER_FEATURES = '''
    unc
    cor
    rem
    rec
    alt
    vac
'''.strip().split()

LEX_FEATURES = '''
    lang
    lex
'''.strip().split()

MORPH_FEATURES = '''
    sp
    cl
    ps
    gn
    nu
    st
    vs
    vt
    md
'''.strip().split()

WORD_FEATURES = tuple([BIBLICAL] + LEX_FEATURES + MORPH_FEATURES)

MODIFIERS = tuple([LANG, INTERLINEAR] + FLAG_FEATURES + CLUSTER_FEATURES[1:])

URL_FORMAT = (
    "https://www.deadseascrolls.org.il/explore-the-archive/search#q='{}'"
)

SECTION = {SCROLL, FRAGMENT, LINE}


class TfApp(object):

  def __init__(app, *args, _asApp=False, silent=False, **kwargs):
    setupApi(app, *args, _asApp=_asApp, silent=silent, **kwargs)

    if app.api:
      app.reportDir = f'{app.repoLocation}/{REPORT_DIR}'

    if not _asApp:
      for cdir in (app.tempDir, app.reportDir):
        os.makedirs(cdir, exist_ok=True)

  def webLink(app, n, text=None, className=None, _asString=False, _noUrl=False):
    api = app.api
    T = api.T

    (scroll, fragment, line) = T.sectionFromNode(n, fillup=True)
    passageText = app.sectionStrFromNode(n)
    href = '#' if _noUrl else URL_FORMAT.format(scroll)
    if text is None:
      text = passageText
      title = f'show this {SCROLL} in the Leon Levy library'
    else:
      title = passageText
    if _noUrl:
      title = None
    target = '' if _noUrl else None

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
    return app._wrapHtml(n, 'glyph', '')

  def fmt_layoutTrans(app, n):
    return app._wrapHtml(n, 'glyph', 'e')

  def fmt_layoutSource(app, n):
    return app._wrapHtml(n, 'glyph', 'o')

  def _wrapHtml(app, n, ft, kind):
    api = app.api
    F = api.F
    Fs = api.Fs
    after = F.after.v(n) or ''
    material = Fs(f'{ft}{kind}').v(n) or ''
    classes = ' '.join(f'{cf}{Fs(cf).v(n)}' for cf in MODIFIERS if Fs(cf).v(n))
    if classes:
      material = f'<span class="{classes}">{material}</span>'
    return f'{material}{after}'

  def _plain(
      app,
      n,
      passage,
      isLinked,
      _asString,
      secLabel,
      **options,
  ):
    display = app.display
    d = display.get(options)

    _asApp = app._asApp
    api = app.api
    F = api.F
    L = api.L
    T = api.T

    nType = F.otype.v(n)
    result = passage
    if _asApp:
      nodeRep = f' <a href="#" class="nd">{n}</a> ' if d.withNodes else ''
    else:
      nodeRep = f' <i>{n}</i> ' if d.withNodes else ''

    rep = ''
    text = ''
    if nType == SIGN:
      text = hlText(app, [n], d.highlights, fmt=d.fmt)
    elif nType == WORD:
      text = hlText(app, L.d(n, otype=SIGN), d.highlights, fmt=d.fmt)
    elif nType in SECTION:
      if secLabel and d.withPassage:
        sep1 = app.sectionSep1
        sep2 = app.sectionSep2
        label = (
            '{}'
            if nType == SCROLL else
            f'{{}}{sep1}{{}}'
            if nType == FRAGMENT else
            f'{{}}{sep1}{{}}{sep2}{{}}'
        )
        rep = label.format(*T.sectionFromNode(n))
        rep = mdhtmlEsc(rep)
        rep = hlRep(app, rep, n, d.highlights)
        if isLinked:
          rep = app.webLink(n, text=f'{rep}&nbsp;', _asString=True)
      else:
        rep = ''
      if nType == LINE:
        text = hlText(app, L.d(n, otype=WORD), d.highlights, fmt=d.fmt)
      elif nType == FRAGMENT:
        rep += mdhtmlEsc(f'{nType} {F.fragment.v(n)}') if secLabel else ''
      elif nType == SCROLL:
        rep += mdhtmlEsc(f'{nType} {F.pnumber.v(n)}') if secLabel else ''
      rep = hlRep(app, rep, n, d.highlights)
      if text:
        text = hlRep(app, text, n, d.highlights)
    elif nType == 'lex':
      rep = mdhtmlEsc(F.lex.v(n))
      rep = hlRep(app, rep, n, d.highlights)
    else:
      rep = hlText(app, L.d(n, otype=SIGN), d.highlights, fmt=d.fmt)
    lineNumbersCondition = d.lineNumbers
    if text:
      tClass = display.formatClass[d.fmt].lower()
      text = f'<span class="{tClass}">{text}</span>'
      rep += text
    rep = app._addLink(
        n,
        rep,
        nodeRep,
        isLinked=isLinked and nType not in SECTION,
        lineNumbers=lineNumbersCondition,
    )
    result += rep

    if _asString or _asApp:
      return result
    dh(result)

  def _addLink(app, n, rep, nodeRep, isLinked=None, lineNumbers=True):
    F = app.api.F
    if isLinked:
      rep = app.webLink(n, text=rep, _asString=True)
    theLine = ''
    if lineNumbers:
      theLine = mdEsc(f' @{F.srcLn.v(n)} ')
    return f'{rep}{nodeRep}{theLine}'

  def _pretty(
      app,
      n,
      outer,
      html,
      firstSlot,
      lastSlot,
      **options,
  ):
    display = app.display
    d = display.get(options)

    goOn = prettyPre(
        app,
        n,
        firstSlot,
        lastSlot,
        d.withNodes,
        d.highlights,
    )
    if not goOn:
      return
    (
        slotType,
        nType,
        className,
        boundaryClass,
        hlAtt,
        nodePart,
        myStart,
        myEnd,
    ) = goOn

    api = app.api
    F = api.F
    L = api.L
    T = api.T
    otypeRank = api.otypeRank
    isHtml = options.get('fmt', None) in app.textFormats

    bigType = (
        not d.full
        and
        d.condenseType is not None and otypeRank[nType] > otypeRank[d.condenseType]
    )

    (hlClass, hlStyle) = hlAtt

    heading = ''
    featurePart = ''
    children = ()

    if bigType:
      children = ()
    elif nType == SCROLL:
      children = L.d(n, otype=FRAGMENT)
    elif nType == FRAGMENT:
      children = L.d(n, otype=LINE)
    elif nType == LINE:
      children = tuple(
          c
          for c in L.d(n)
          if F.otype.v(c) == WORD
      )
    elif nType == WORD:
      children = L.d(n, otype=SIGN)
    elif nType == CLUSTER:
      children = L.d(n, otype=SIGN)

    isText = False

    if nType == SCROLL:
      heading = htmlEsc(F.pnumber.v(n))
      heading += ' '
      heading += getFeatures(
          app,
          n,
          (BIBLICAL, SCROLL),
          plain=True,
          **options,
      )
    elif nType == FRAGMENT:
      heading = htmlEsc(F.fragment.v(n))
      featurePart = getFeatures(
          app,
          n,
          (BIBLICAL, FRAGMENT),
          **options,
      )
    elif nType == LINE:
      heading = htmlEsc(F.line.v(n))
      className = LINE
      theseFeats = (BIBLICAL, LINE)
      featurePart = getFeatures(
          app,
          n,
          theseFeats,
          **options,
      )
    elif nType == CLUSTER:
      heading = F.type.v(n)
      featurePart = getFeatures(
          app,
          n,
          (),
          **options,
      )
    elif nType == WORD:
      isText = True
      text = T.text(n, fmt=d.fmt, descend=True)
      heading = text if isHtml else htmlEsc(text)
      theseFeats = WORD_FEATURES
      if d.lineNumbers:
        theseFeats = (SRCLN,) + theseFeats
      featurePart = getFeatures(
          app,
          n,
          theseFeats,
          **options,
      )
    elif nType == 'lex':
      extremeOccs = getBoundary(api, n)
      linkOccs = ' - '.join(app.webLink(lo, _asString=True) for lo in extremeOccs)
      heading = f'<div class="h">{htmlEsc(F.lex.v(n))}</div>'
      occs = f'<div class="occs">{linkOccs}</div>'
      featurePart = getFeatures(
          app,
          n,
          ('voc_lex', 'gloss'),
          givenValue=dict(voc_lex=app.webLink(n, text=htmlEsc(F.voc_lex.v(n)), _asString=True)),
          **options,
      ) + occs
    elif nType == slotType:
      isText = True
      text = T.text(n, fmt=d.fmt)
      heading = text if isHtml else htmlEsc(text)
      featurePart = getFeatures(
          app,
          n,
          MODIFIERS,
          withName=True,
          **options,
      )
      if not outer and F.type.v(n) == 'empty':
        return

    tClass = display.formatClass[d.fmt].lower() if isText else app.defaultCls
    heading = f'<span class="{tClass}">{heading}</span>'

    if outer:
      typePart = app.webLink(n, text=f'{nType} {heading}', _asString=True)
    else:
      typePart = heading

    label = f'''
    <div class="lbl {className}">
        {typePart}
        {nodePart}
    </div>
''' if typePart or nodePart else ''

    html.append(
        f'''
<div class="contnr {className} {hlClass}" {hlStyle}>
    {label}
    <div class="meta">
        {featurePart}
    </div>
'''
    )
    if children:
      html.append(f'''
    <div class="children {className}">
''')

    for ch in children:
      app._pretty(
          ch,
          False,
          html,
          firstSlot,
          lastSlot,
          **options,
      )
    if children:
      html.append('''
    </div>
''')
    html.append('''
</div>
''')
